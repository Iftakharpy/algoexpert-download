import pathlib


LOG = True

# Change this to set the destination of all the questions 
PARENT_DIR = pathlib.Path(r".")

# Get auth_key by inspecting network calls
#   1. Open Chrome Devtools 
#   2. Network Tab
#   3. Inspect a request that requires auth_key(Ex: https://prod.api.algoexpert.io/api/problems/v1/run_json_tests)
#   4. find `authorization` header in the request headers section
AUTH_KEY = "YOUR API KEY"

# Headers to send with request to https://algoexpert.io
REQUEST_HEADERS_FOR_ALGOEXPERT_SITE = {
    "authorization": AUTH_KEY,
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36",
    "accept": "*/*",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "en-US,en;q=0.9,bn;q=0.8",
    "cache-control": "no-cache",
    "content-type": "text/plain;charset=UTF-8",
    "origin": "https://www.algoexpert.io",
    "pragma": "no-cache",
    "referer": "https://www.algoexpert.io/",
    "sec-ch-ua": '"Google Chrome";v="95", "Chromium";v="95", ";Not A Brand";v="99"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "Windows",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
}

# Question list endpoint
DOWNLOAD_QUESTION_LIST = True # If previously downloaded then set False
QUESTION_LIST_ENDPOINT = "https://prod.api.algoexpert.io/api/problems/v1/algoexpert/coding-questions/list"
QUESTION_LIST_FILE_NAME = 'question_list.json'

# Question metadata endpoint
DOWNLOAD_QUESTION_DATA = True # If previously downloaded then set False
QUESTION_DATA_ENDPOINT = "https://prod.api.algoexpert.io/api/problems/v1/algoexpert/coding-questions/get"

# Question tests endpoint
DOWNLOAD_QUESTION_TESTS = True # If previously downloaded then set False
QUESTION_TESTS_ENDPOINT = "https://prod.api.algoexpert.io/api/problems/v1/run_json_tests"

# Cooldown time between requests in seconds
COOLDOWN_TIME = 1

# Indentation spaces for formatting downloaded json responses
INDENTATION_SPACES = 2
