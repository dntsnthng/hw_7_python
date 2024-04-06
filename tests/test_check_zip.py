import zipfile
import csv

def test_csv(create_archive):
    with zipfile.ZipFile('C:\\Users\\Admin\\Desktop\\getting-started-python-master\\qa_quru_homowork_7\\resoursefile.zip') as zip_file: # открываем архив
        with zip_file.open('file.csv') as csv_file: # открываем файл в архиве
            content = csv_file.read().decode('utf-8-sig') # читаем содержимое файла и декодируем его если в файле есть символы не из английского алфавита
            csvreader = list(csv.reader(content.splitlines())) # читаем содержимое файла и преобразуем его в список
            second_row = csvreader[1] # получаем вторую строку

            assert second_row[0] == '1'  # проверка значения элемента в первом столбце второй строки
            assert second_row[1] == '1'  # проверка значения элемента во втором столбце второй строки