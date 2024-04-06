import os
import shutil
import zipfile
import pytest

import os.path

CURRENT_FILE = os.path.abspath(__file__)
CURRENT_DIR = os.path.dirname(CURRENT_FILE)
TMP_DIR = os.path.join(CURRENT_DIR, 'tmp')
RESOURCES_FILE = os.path.abspath(__file__)
RESOURCES_DIR = os.path.dirname(RESOURCES_FILE)
RSR_DIR = os.path.join(RESOURCES_DIR, 'resourse')




@pytest.fixture
def create_archive(scope="session", autouse=True):
    if not os.path.isdir('C:\\Users\\Admin\\Desktop\\getting-started-python-master\\qa_quru_homowork_7\\resourse'):
        os.makedirs('C:\\Users\\Admin\\Desktop\\getting-started-python-master\\qa_quru_homowork_7\\resourse')
    with zipfile.ZipFile('C:\\Users\\Admin\\Desktop\\getting-started-python-master\\qa_quru_homowork_7\\resourse\\file.zip', 'w') as zf:
        for file in "file.pdf", "file.csv", "file.xlsx":
            add_file = os.path.join('C:\\Users\\Admin\\Desktop\\getting-started-python-master\\qa_quru_homowork_7\\tmp', file)
            zf.write(add_file, os.path.basename(add_file))
    yield
    shutil.rmtree('C:\\Users\\Admin\\Desktop\\getting-started-python-master\\qa_quru_homowork_7\\resourse\\file.zip')