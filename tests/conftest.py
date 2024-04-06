<<<<<<< HEAD
import zipfile
import os
import pytest
=======
import os
import zipfile
import pytest

>>>>>>> origin/master
import os.path

CURRENT_FILE = os.path.abspath(__file__)
CURRENT_DIR = os.path.dirname(CURRENT_FILE)
TMP_DIR = os.path.join(CURRENT_DIR, 'tmp')
print(TMP_DIR)


@pytest.fixture
<<<<<<< HEAD
def create_archive(scope='session', autouse=True):
=======
def create_archive():
>>>>>>> origin/master
    if not os.path.isdir('C:\\Users\\Admin\\Desktop\\getting-started-python-master\\qa_quru_homowork_7\\resourse'):
        os.makedirs('C:\\Users\\Admin\\Desktop\\getting-started-python-master\\qa_quru_homowork_7\\resourse')
    files = ['file.pdf', 'file.xlsx', 'file.csv']
    with zipfile.ZipFile('C:\\Users\\Admin\\Desktop\\getting-started-python-master\\qa_quru_homowork_7\\resourse\\file.zip', 'w') as zf:
        for file in files:
            add_file = os.path.join(file)
            zf.writestr(add_file, file)
<<<<<<< HEAD
    yield
=======
>>>>>>> origin/master
