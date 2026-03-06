import fitz  # PyMuPDF
import pytesseract
from PIL import Image
import io
import argostranslate.package
import argostranslate.translate
import os

from sympy.codegen.ast import none

# --- НАЛАШТУВАННЯ ШЛЯХІВ ---
# Розкоментуй і вкажи шлях до tesseract.exe, якщо він не в системних змінних
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Шлях до шрифту (обов'язково .ttf з підтримкою кирилиці)
FONT_PATH = "C:/Windows/Fonts/arial.ttf"


def setup_translation():
    print("Перевірка мовної моделі...")
    argostranslate.package.update_package_index()
    available_packages = argostranslate.package.get_available_packages()
    package_to_install = next(
        filter(lambda x: x.from_code == "en" and x.to_code == "uk", available_packages)
    )
    if not any(p.from_code == "en" and p.to_code == "uk" for p in argostranslate.package.get_installed_packages()):
        print("Завантаження пакета EN->UK...")
        argostranslate.package.install_from_path(package_to_install.download())
    print("Модель готова.")


def translate_pdf_vertical_split(input_path, output_path):
    setup_translation()
    doc = fitz.open(input_path)
    out_doc = fitz.open()

    for page_num in range(len(doc)):
        print(f"Обробка фізичної сторінки {page_num + 1}/{len(doc)}...")
        page = doc[page_num]

        # 1. ПОВОРОТ: Якщо текст на скані боком, повертаємо на 90 градусів за годинниковою
        # Якщо текст вже стоїть рівно, цей рядок можна закоментувати
        page.set_rotation(270)

        # Створюємо нову сторінку в вихідному документі
        new_page = out_doc.new_page(width=page.rect.width, height=page.rect.height)

        # Визначаємо межу розділу (горизонтальна лінія посередині)
        mid_y = page.rect.height / 2

        # Дві зони: Верхня сторінка і Нижня сторінка
        regions = [
            fitz.Rect(0, 0, page.rect.width, mid_y),  # Верх
            fitz.Rect(0, mid_y, page.rect.width, page.rect.height)  # Низ
        ]

        for rect in regions:
            # 2. OCR ТА ОБРОБКА ЧАСТИНИ
            # Беремо зображення конкретної частини
            pix = page.get_pixmap(matrix=fitz.Matrix(2, 2), clip=rect)
            img = Image.open(io.BytesIO(pix.tobytes("png")))

            # Накладаємо оригінальне зображення на нову сторінку
            new_page.insert_image(rect, pixmap=pix, overlay=False)

            # Розпізнаємо текст
            data = pytesseract.image_to_data(img, lang='eng', output_type=pytesseract.Output.DICT)

            scale_x = rect.width / pix.width
            scale_y = rect.height / pix.height

            last_block = -1
            block_text = []
            block_rect = None

            for i in range(len(data['text'])):
                text = data['text'][i].strip()
                b_id = data['block_num'][i]
                conf = int(data['conf'][i])

                if text and conf > 40:
                    if b_id != last_block and block_text:
                        # Важливо: додаємо зміщення rect.y0, щоб текст не "стрибав" на початок сторінки
                        draw_translated_block(new_page, block_text, block_rect, rect.x0, rect.y0)
                        block_text = []
                        block_rect = None

                    block_text.append(text)
                    x, y, w, h = data['left'][i], data['top'][i], data['width'][i], data['height'][i]
                    r = fitz.Rect(x * scale_x, y * scale_y, (x + w) * scale_x, (y + h) * scale_y)
                    block_rect = r if block_rect is None else block_rect | r
                    last_block = b_id

            # Обробка останнього блоку в частині
            draw_translated_block(new_page, block_text, block_rect, rect.x0, rect.y0)

        # Чекпоінт кожні 20 сторінок для 440-сторінкового документа
        if (page_num + 1) % 20 == 0:
            out_doc.save(f"progress_checkpoint.pdf")
            print("--- Чекпоінт збережено ---")

    # Замість простого out_doc.save(output_path)
    out_doc.save(output_path, garbage=4, deflate=True, clean=True)
    print(f"Успішно завершено! Файл: {output_path}")


def draw_translated_block(page, text_list, relative_rect, offset_x, offset_y):
    if not text_list or relative_rect is None:
        return

    # Корекція координат відносно всієї сторінки
    final_rect = relative_rect + (offset_x, offset_y, offset_x, offset_y)
    original_text = " ".join(text_list)

    try:
        translated = argostranslate.translate.translate(original_text, "en", "uk")
        # Затираємо оригінал білим фоном
        page.draw_rect(final_rect, color=(1, 1, 1), fill=(1, 1, 1))
        # Вставляємо переклад
        page.insert_textbox(final_rect, translated,
                            fontname="ukr", fontfile=FONT_PATH,
                            fontsize=8, align=0)
    except:
        pass


if __name__ == "__main__":
    translate_pdf_vertical_split("testbook.pdf", "translated_book.pdf")