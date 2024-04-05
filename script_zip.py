from zipfile import ZipFile




with ZipFile("file.zip", 'w') as zip_file: # создаем архив
    ZipFile.write("TMP_DIR", arcname='file.pdf') # добавляем файл в архив
    ZipFile.close() # закрываем архив