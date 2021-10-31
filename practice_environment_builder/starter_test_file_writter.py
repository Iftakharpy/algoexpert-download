import pathlib
import sys
import re

# Adding parent directory to path to import from the added parent directory
CURRENT_FILE_PATH = pathlib.Path(__file__).absolute()
sys.path.append(str(CURRENT_FILE_PATH.parent.parent))

from config import PREFERRED_LANGUAGE_RESOURCE_KEY

PYTHON_FUNCTION_NAME_REGEX = re.compile(r"def \s*(\w+)\s*\(")



def get_tester_code(question_object:dict|list, question_tests_object:dict|list, module_to_test:str):
    # Getting function name to import from the module_to_test
    function_to_test = PYTHON_FUNCTION_NAME_REGEX.search(question_object['resources']['python']['startingCode']).group(1)

    # Getting test case information
    test_case_objects = question_tests_object['JSONTests']
    expected_results = [result["Expected"] for result in question_tests_object['TestResults']]

    # Preparing test cases
    test_cases = []
    for serial, test_object in enumerate(zip(test_case_objects, expected_results), 1):
        actual_test, expected_result = test_object
        test_case = f"""def test_{function_to_test}_case_{serial}():
    assert {function_to_test}({', '.join([f'{kwarg[0]}={repr(kwarg[1])}' for kwarg in actual_test.items()]) }) == {repr(expected_result)}
"""
        test_cases.append(test_case)

    # Preparing tester code
    tester_code = f"""from {module_to_test} import {function_to_test}"""
    tester_code += "\n\n"
    for test_case in test_cases:
        tester_code += f"{test_case}\n"
        
    return tester_code


def write_test_file_for_question(question_object:dict|list, question_tests_object:dict|list, module_to_test:str, destination_file_path:pathlib.Path):
    code_to_write = get_tester_code(question_object, question_tests_object, module_to_test)
    with open(destination_file_path, "w", encoding="utf-8") as test_file:
        test_file.write(code_to_write)
