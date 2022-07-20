import requests
import pathlib
import json
import time
import sys


CURRENT_FILE_PATH = pathlib.Path(__file__).absolute()
# Adding parent directory to path in order to import from the added directories
sys.path.append(str(CURRENT_FILE_PATH.parent.parent))
sys.path.append(str(CURRENT_FILE_PATH.parent.parent.parent))

# Importing from the directories added to path earlier
from rename import make_file_name_valid
from question_directory_getter import get_question_dir
from file_helper import load_json_file_as_python_obj, write_python_object_to_file
from config import PARENT_DIR, REQUEST_HEADERS_FOR_ALGOEXPERT_SITE,\
    DOWNLOAD_QUESTION_LIST, DOWNLOAD_QUESTION_DATA, DOWNLOAD_QUESTION_TESTS,\
    QUESTION_LIST_ENDPOINT, QUESTION_LIST_FILE_NAME, \
    QUESTION_DATA_ENDPOINT, QUESTION_TESTS_ENDPOINT, \
    COOLDOWN_TIME, INDENTATION_SPACES, LOG


# Get list of all questions
def get_list_of_all_questions(url=QUESTION_LIST_ENDPOINT) -> requests.Response:
    response = requests.post(url, headers=REQUEST_HEADERS_FOR_ALGOEXPERT_SITE)
    return response

# Get meta data for specified question
def get_question_data(question_name:str, url=QUESTION_DATA_ENDPOINT) -> requests.Response:
    question = {'name': question_name}
    response = requests.post(url, data=json.dumps(question), headers=REQUEST_HEADERS_FOR_ALGOEXPERT_SITE)
    return response

# Get all the tests and solutions for the specified question
def run_tests_get_response(submission_question:dict, url=QUESTION_TESTS_ENDPOINT) -> requests.Response:
    response = requests.post(url, data=json.dumps(submission_question), headers=REQUEST_HEADERS_FOR_ALGOEXPERT_SITE)
    return response


def main():
    question_list_file_path = PARENT_DIR / QUESTION_LIST_FILE_NAME
    if DOWNLOAD_QUESTION_LIST:
        if LOG:
            print("Downloading question list")
        response = get_list_of_all_questions()

        questions = response.json()
        write_python_object_to_file(questions, question_list_file_path, INDENTATION_SPACES)
    else:
        if LOG:
            print(f"Loading question list from {str(question_list_file_path)}")
        questions = load_json_file_as_python_obj(question_list_file_path)

    questions:list = questions['questions']
    questions.sort(key=lambda obj: obj.get('difficulty'))
    
    for idx, question in enumerate(questions, 1):
        question_name = question['name']
        file_name = make_file_name_valid(question_name)
        question_dir = get_question_dir(question_name, idx)
        question_data_path = question_dir / f'{file_name}_data.json'
        question_tests_path = question_dir / f'{file_name}_tests.json'

        if LOG:
            print(f"Question data: {idx} {question_name}")

        # cooldown
        time.sleep(COOLDOWN_TIME)
        if DOWNLOAD_QUESTION_DATA:
            if LOG:
                print(f"Downloading data")
            
            response = get_question_data(question_name)
            question_data = response.json()
            write_python_object_to_file(question_data, question_data_path)
            
            if LOG:
                print("Success")

        elif DOWNLOAD_QUESTION_TESTS:
            if LOG:
                print("Loading data")
            question_data = load_json_file_as_python_obj(question_data_path)
            if LOG:
                print("Success")

        # cooldown
        time.sleep(COOLDOWN_TIME)
        if DOWNLOAD_QUESTION_TESTS:
            if LOG:
                print("Downloading tests")
            
            question_submission = {
                "language": "python",
                "questionName": question_data['name'],
                "userSolution": question_data['resources']['python']['solutions'][0],
                "questionVersion": question_data['version'],
                "product": "algoexpert"
            }
            response = run_tests_get_response(question_submission)
            question_test_data = response.json()
            write_python_object_to_file(question_test_data, question_tests_path)

            if LOG:
                print("Success")
            

if __name__=='__main__':
    main()
