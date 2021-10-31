import pathlib
import sys

# Adding parent directory to path to import from the added parent directory
CURRENT_FILE_PATH = pathlib.Path(__file__).absolute()
sys.path.append(str(CURRENT_FILE_PATH.parent.parent))

from rename import make_file_name_valid
from config import PARENT_DIR

# This will be utilized to get the path to save and read question's data and solution
def get_question_dir(question_name:str, serial_number:int = 0, parent_dir:pathlib.Path=PARENT_DIR) -> pathlib.Path:
    serial_number = f"{serial_number}".rjust(3, '0')
    folder_name = make_file_name_valid(question_name)

    question_dir = parent_dir / f"{serial_number} {folder_name}"
    if not question_dir.exists():
        question_dir.mkdir()
    return question_dir
