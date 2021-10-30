import pathlib
import json
import sys

# Adding parent directory to path to import from the added parent directory
CURRENT_FILE_PATH = pathlib.Path(__file__).absolute()
sys.path.append(str(CURRENT_FILE_PATH.parent.parent))

from rename import make_file_name_valid
from config import INDENTATION_SPACES


def write_python_object_to_file(obj:object, file_path:pathlib.Path, indent=INDENTATION_SPACES):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(json.dumps(obj, indent=indent))

def load_json_file_as_python_obj(file_path:pathlib.Path):
    with open(file_path, 'r', encoding="utf-8") as file:
        python_obj = json.load(file)
    return python_obj
