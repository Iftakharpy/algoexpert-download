import pathlib

# Change this to set the destination of all the questions 
PARENT_DIR = pathlib.Path(r"I:\Courses\AlgoExpert\AlgoExpert\Coding Interview Questions")

# Get auth_key by inspecting network calls
#   1. Open Chrome Devtools 
#   2. Network Tab
#   3. Inspect a request that requires auth_key(Ex: https://prod.api.algoexpert.io/api/problems/v1/run_json_tests)
#   4. find `authorization` header in the request headers section
AUTH_KEY = "YOUR AUTH KEY"
