from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pathlib
import shutil
import time
import pathlib
import sys


CURRENT_FILE_PATH = pathlib.Path(__file__).absolute()
# Adding parent directory to path in order to import from the added directories
sys.path.append(str(CURRENT_FILE_PATH.parent.parent))
sys.path.append(str(CURRENT_FILE_PATH.parent.parent.parent))

# Importing from the directories added to path earlier
from rename import make_file_name_valid
from question_directory_getter import get_question_dir
from file_helper import load_json_file_as_python_obj
from config import LOG, PARENT_DIR, TEMP_PDF_DOWNLOAD_DIR,\
    CHROME_USER_DATA_DIR, CHROME_PREFERENCES, QUESTION_LIST_FILE_NAME,\
    QUESTION_URL_PREFIX, QUESTION_STATEMENT_XPATH, HINT_EXPAND_WAIT_TIME,\
    LOAD_QUESTION_MAX_WAIT_TIME


CHROME_OPTIONS = webdriver.ChromeOptions()
CHROME_OPTIONS.add_argument(f"user-data-dir={str(CHROME_USER_DATA_DIR)}")

CHROME_OPTIONS.add_experimental_option('prefs', CHROME_PREFERENCES)
CHROME_OPTIONS.add_argument('--kiosk-printing')


with open(pathlib.Path(__file__).parent / 'script.js') as script:
    SCRIPT = script.read()


def main():
    # Open Chrome browser
    DRIVER = webdriver.Chrome(options=CHROME_OPTIONS)
    questions = load_json_file_as_python_obj(PARENT_DIR / QUESTION_LIST_FILE_NAME)['questions']
    questions.sort(key=lambda obj: obj.get('difficulty'))

    for idx, question in enumerate(questions, 1):
        question_name = question['name']
        if LOG:
            print(f"Downloading pdf: {idx} {question_name}")

        question_dir = get_question_dir(question_name, idx)
        
        # Navigate to target question
        DRIVER.get(f'{QUESTION_URL_PREFIX}{question_name}')
        WebDriverWait(DRIVER, LOAD_QUESTION_MAX_WAIT_TIME).until(EC.visibility_of_element_located((By.XPATH, QUESTION_STATEMENT_XPATH)))

        DRIVER.execute_script(SCRIPT)
        
        # Let the hints expand
        time.sleep(HINT_EXPAND_WAIT_TIME)
        
        # Download file
        DRIVER.execute_script('window.print();')

        # Move file from TEMP_PDF_DOWNLOAD_DIR to the question directory
        temp_pdf = next(TEMP_PDF_DOWNLOAD_DIR.glob('*.pdf')) # Get downloaded file
        shutil.move(temp_pdf, question_dir)
        if LOG:
            print("Success")

    # Close Chrome browser
    DRIVER.close()


if __name__ == '__main__':
    main()
