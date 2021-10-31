from downloaders.rename import make_file_name_valid
from downloaders.question_directory_getter import get_question_dir
from downloaders.file_helper import load_json_file_as_python_obj
from .starter_solve_file_writter import write_starter_solve_file_for_question, write_sandbox_file_for_question
from .starter_test_file_writter import write_test_file_for_question

import pathlib
import sys

# Adding parent directory to path to import from the added parent directory
CURRENT_FILE_PATH = pathlib.Path(__file__).absolute()
sys.path.append(str(CURRENT_FILE_PATH.parent.parent))

from config import PRACTICE_ENVIRONMENT_ROOT_DIR, PREFERRED_LANGUAGE_FILE_EXTENSION,\
    LOG, PARENT_DIR, QUESTION_LIST_FILE_NAME


def main():
    question_list_file_path = PARENT_DIR / QUESTION_LIST_FILE_NAME
    questions = load_json_file_as_python_obj(question_list_file_path)

    questions:list = questions['Problems']
    questions.sort(key=lambda obj: obj.get('difficulty'))
    
    for idx, question in enumerate(questions, 1):
        question_name = question['name']
        file_name = make_file_name_valid(question_name)
        question_dir = get_question_dir(question_name, idx)
        question_data_path = question_dir / f'{file_name}_data.json'
        question_tests_path = question_dir / f'{file_name}_tests.json'
        
        if LOG:
            print(f"Preparing practice files for: {idx} {question_name}")

        # Prepare file paths to write starting file and tester file
        question_practice_dir = get_question_dir(question_name, idx, PRACTICE_ENVIRONMENT_ROOT_DIR)
        file_name = file_name.replace(' ', '_')
        # Build path for starting file
        starting_solve_file_name = f"{file_name}.{PREFERRED_LANGUAGE_FILE_EXTENSION}"
        starting_solve_file_path = question_practice_dir / starting_solve_file_name
        # Build path for starting file
        sandbox_file_name = f"{file_name}_sandbox.{PREFERRED_LANGUAGE_FILE_EXTENSION}"
        sandbox_file_path = question_practice_dir / sandbox_file_name
        # Build path for tester file
        tester_file_name = f"{file_name}_test.{PREFERRED_LANGUAGE_FILE_EXTENSION}"
        tester_file_path = question_practice_dir / tester_file_name

        if LOG:
            print(f"Writing starter file")
        # Writing starting code to starting_solve_file_path
        question_data_object = load_json_file_as_python_obj(question_data_path)
        write_starter_solve_file_for_question(question_data_object, starting_solve_file_path)
        if LOG:
            print(f"Writing sandbox file")
        # Writing starting code to starting_solve_file_path
        question_data_object = load_json_file_as_python_obj(question_data_path)
        write_sandbox_file_for_question(question_data_object, sandbox_file_path)
        
        if LOG:
            print(f"Writing tester code")
        # Writing tester code to starting_solve_file_path
        question_tests_data_object = load_json_file_as_python_obj(question_tests_path)
        write_test_file_for_question(question_data_object, question_tests_data_object, module_to_test=file_name, destination_file_path=tester_file_path)
        if idx>=10:
            break

if __name__=="__main__":
    main()
