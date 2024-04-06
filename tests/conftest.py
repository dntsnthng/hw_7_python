import os
import shutil
import zipfile
import pytest

import os.path

CURRENT_FILE = os.path.dirname(__file__)
CURRENT_DIR = os.path.dirname(CURRENT_FILE)
TMP_DIR = os.path.join(CURRENT_DIR, 'tmp')
RSR_DIR = os.path.join(CURRENT_DIR, 'resource')
ZIP_FILE = os.path.join(RSR_DIR, 'test.zip')



@pytest.fixture(scope="session", autouse=True)
def create_archive():
    if not os.path.isdir(RSR_DIR):
        os.makedirs(RSR_DIR)

    with zipfile.ZipFile(ZIP_FILE, 'w') as zf:
        for file in os.listdir(TMP_DIR):
            add_file = os.path.join(TMP_DIR, file)
            zf.write(add_file, os.path.basename(add_file))
    yield

    shutil.rmtree(RSR_DIR)

