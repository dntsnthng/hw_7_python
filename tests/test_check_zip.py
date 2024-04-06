from openpyxl.reader.excel import load_workbook
from zipfile import ZipFile
from pypdf import PdfReader
from tests.conftest import ZIP_FILE


def test_check_pdf_file():
    with ZipFile(ZIP_FILE) as zf:
        reader = PdfReader(zf.open('file.pdf'))

        assert 'sobaka@mail.ru' in reader.pages[0].extract_text()

def test_check_xlsx_file():
    with ZipFile(ZIP_FILE) as zf:
        with zf.open('file.xlsx') as file:
            workbook = load_workbook(file)
            sheet = workbook.active
            assert sheet.cell(row=4, column=3).value == 'password'


def test_check_csv_file():
    with ZipFile(ZIP_FILE) as zf:
        with zf.open('file.csv') as file:
            sheet = file.read().decode('utf-8-sig')
            assert '1' in sheet