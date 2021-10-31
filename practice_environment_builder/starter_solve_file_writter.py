import pathlib
import sys

# Adding parent directory to path to import from the added parent directory
CURRENT_FILE_PATH = pathlib.Path(__file__).absolute()
sys.path.append(str(CURRENT_FILE_PATH.parent.parent))

from config import PREFERRED_LANGUAGE_RESOURCE_KEY


def write_starter_solve_file_for_question(question_object: pathlib.Path, destination_file_path:pathlib.Path, resource_key=PREFERRED_LANGUAGE_RESOURCE_KEY):
    with open(destination_file_path, "w", encoding="utf-8") as starter_solve_file:
        starter_code = question_object["resources"][resource_key]["startingCode"]
        starter_solve_file.write(starter_code)

def write_sandbox_file_for_question(question_object: pathlib.Path, destination_file_path:pathlib.Path, resource_key=PREFERRED_LANGUAGE_RESOURCE_KEY):
    with open(destination_file_path, "w", encoding="utf-8") as starter_solve_file:
        starter_code = question_object["resources"][resource_key]["sandboxCode"]
        starter_solve_file.write(starter_code)
