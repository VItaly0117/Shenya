import fitz
import pytesseract
from PIL import Image
import io
from deep_translator import GoogleTranslator
import time

# Налаштування Tesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
FONT_PATH = "C:/Windows/Fonts/arial.ttf"


def translate_pdf_final(input_pdf, output_pdf):
    doc = fitz.open(input_pdf)
    out_doc = fitz.open()
    translator = GoogleTranslator(source='en', target='uk')

    for page_num in range(len(doc)):
        print(f"Сторінка {page_num + 1}/{len(doc)}...")
        page = doc[page_num]
        page.set_rotation(270)  # Поворот як на скані

        new_page = out_doc.new_page(width=page.rect.width, height=page.rect.height)

        # Рендеримо фон (якість 2x для OCR)
        pix = page.get_pixmap(matrix=fitz.Matrix(2, 2))
        new_page.insert_image(new_page.rect, stream=pix.tobytes("jpg", jpg_quality=70))

        # Отримуємо дані по БЛОКАХ (block_num), а не по словах
        img = Image.open(io.BytesIO(pix.tobytes("png")))
        data = pytesseract.image_to_data(img, lang='eng', output_type=pytesseract.Output.DICT)

        scale_x, scale_y = page.rect.width / pix.width, page.rect.height / pix.height

        # Групуємо текст за номерами блоків
        blocks = {}
        for i in range(len(data['text'])):
            text = data['text'][i].strip()
            conf = int(data['conf'][i])
            b_id = data['block_num'][i]

            if text and conf > 40:  # Знижуємо поріг, щоб бачити все речення
                if b_id not in blocks:
                    blocks[b_id] = {'text': [], 'rect': None}

                blocks[b_id]['text'].append(text)
                x, y, w, h = data['left'][i], data['top'][i], data['width'][i], data['height'][i]
                r = fitz.Rect(x * scale_x, y * scale_y, (x + w) * scale_x, (y + h) * scale_y)

                if blocks[b_id]['rect'] is None:
                    blocks[b_id]['rect'] = r
                else:
                    blocks[b_id]['rect'] |= r

        # Перекладаємо та малюємо кожен блок
        for b_id in blocks:
            full_text = " ".join(blocks[b_id]['text'])

            # Ігноруємо зовсім дрібні блоки (імовірні формули або шум)
            if len(full_text) < 5: continue

            try:
                translated = translator.translate(full_text)
                rect = blocks[b_id]['rect']

                # Затираємо оригінал білим
                new_page.draw_rect(rect, color=(1, 1, 1), fill=(1, 1, 1))

                # Вставляємо переклад (шрифт 8 для компактності)
                new_page.insert_textbox(rect, translated,
                                        fontname="ukr", fontfile=FONT_PATH,
                                        fontsize=8, align=0)
            except Exception as e:
                print(f"Помилка блоку: {e}")
                continue

        # Щоб Google не забанив за швидкість
        time.sleep(0.5)

    out_doc.save(output_pdf, garbage=4, deflate=True)
    out_doc.close()


if __name__ == "__main__":
    translate_pdf_final("testbook.pdf", "fixed_v2.pdf")