import re
import pathlib

# Flag to print logs
LOG = True

# Change this to set the destination of all the questions
# PARENT_DIR must be an instance of pathlib.Path
PARENT_DIR:pathlib.Path = pathlib.Path(r"./All Questions/")
PARENT_DIR.mkdir(parents=True, exist_ok=True)

# Get auth_key by inspecting network calls
#   1. Open Chrome Devtools 
#   2. Network Tab
#   3. Inspect a request that requires auth_key(Ex: https://prod.api.algoexpert.io/api/problems/v1/run_json_tests)
#   4. find `authorization` header in the request headers section
AUTH_KEY = "eyJhbGciOiJIUzI1NiIsImtpZCI6IjdjYmM2ZWRhNzk1ZGM1YzMxZjJmOTk2Yzg0ODRkZTRiMGIxOTgwMmVmOTYwOWE3YzJmNDFmM2E0OTVhYjZmN2MiLCJ0eXAiOiJKV1QifQ.eyJTZXNzaW9uSUQiOiI4M2Q2ODVmNC0xNzRlLTQ3ZGYtYjI3Zi01YTU2ZTM3YmU5NDUiLCJNZXRhZGF0YSI6eyJwYXJ0aXRpb24iOiJtYWluIiwib2F1dGhfcHJvdmlkZXIiOiJnb29nbGUiLCJvYXV0aF91c2VyX2lkIjoiMTA1ODgxMTA4NjA2Mzc5MTA4OTgyIiwiZW1haWwiOiJpZmF0YWtoYXJmYkBnbWFpbC5jb20iLCJuYW1lIjoiSWZ0YWtoYXIgSHVzc2FpbiIsImF2YXRhcl91cmwiOiJodHRwczovL2xoMy5nb29nbGV1c2VyY29udGVudC5jb20vYS9BQVRYQUp5OFF4dVZnaWF4S3NUalhMMWc4SnpNbld3cWdWNEtWa0dxNm9SRD1zOTYtYyIsInJlZ2lvbiI6IkJEIiwicm9sZXMiOiJwcmVtaXVtdjEsc3lzdGVtc2V4cGVydHYxLHVzZXIifSwiR2VuZXJpY01ldGEiOnt9LCJleHAiOjE2MzY4MTczNTMsImp0aSI6ImI0ZWZlZDRhLWY1YTktNDY5Yy05ZGJjLWE4MGZkMmVlOGJjNiIsImlhdCI6MTYzNTYwNzc1MywiaXNzIjoiYWxnb2V4cGVydCIsInN1YiI6Imdvb2dsZXwwYzQ1NjI3OC01MjgxLTRiYWUtODI4Yi00YzFiYjMxOGQ1MmYifQ.mJRPFMPjuf9h6I16w0H6OAyAPj1piEYTUFt_gsY89ro"


# ================================================================
# Configurations for question_data downloader
RUN_question_data = False

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

DOWNLOAD_QUESTION_LIST = False # If previously downloaded then set False
# Question list endpoint
QUESTION_LIST_ENDPOINT = "https://prod.api.algoexpert.io/api/problems/v1/algoexpert/coding-questions/list"
QUESTION_LIST_FILE_NAME = 'question_list.json'

DOWNLOAD_QUESTION_DATA = True # If previously downloaded then set False
# Question metadata endpoint
QUESTION_DATA_ENDPOINT = "https://prod.api.algoexpert.io/api/problems/v1/algoexpert/coding-questions/get"

DOWNLOAD_QUESTION_TESTS = True # If previously downloaded then set False
# Question tests endpoint
QUESTION_TESTS_ENDPOINT = "https://prod.api.algoexpert.io/api/problems/v1/run_json_tests"

# Cooldown time between requests in seconds
COOLDOWN_TIME = 1

# Indentation spaces for formatting downloaded json responses
INDENTATION_SPACES = 2


# ================================================================
# Configurations for question_pdf downloader
RUN_question_pdf = False # If previously downloaded then set False

QUESTION_URL_PREFIX = "https://www.algoexpert.io/questions/"

TEMP_PDF_DOWNLOAD_DIR = pathlib.Path('./temp/')
TEMP_PDF_DOWNLOAD_DIR.mkdir(parents=True, exist_ok=True)


# Required to download pdf using already logged in session
CHROME_USER_DATA_DIR = pathlib.Path("C:\\Users\\Iftek\\AppData\\Local\\Google\\Chrome\\User Data")

CHROME_SETTINGS_APPSTATE = "{\"version\":2,\"recentDestinations\":[{\"id\":\"Save as PDF\",\"origin\":\"local\",\"account\":\"\",\"capabilities\":{\"printer\":{\"color\":{\"option\":[{\"is_default\":true,\"type\":\"STANDARD_COLOR\",\"vendor_id\":\"2\"}]},\"media_size\":{\"option\":[{\"height_microns\":1189000,\"name\":\"ISO_A0\",\"width_microns\":841000,\"custom_display_name\":\"A0\"},{\"height_microns\":841000,\"name\":\"ISO_A1\",\"width_microns\":594000,\"custom_display_name\":\"A1\"},{\"height_microns\":594000,\"name\":\"ISO_A2\",\"width_microns\":420000,\"custom_display_name\":\"A2\"},{\"height_microns\":420000,\"name\":\"ISO_A3\",\"width_microns\":297000,\"custom_display_name\":\"A3\"},{\"height_microns\":297000,\"is_default\":true,\"name\":\"ISO_A4\",\"width_microns\":210000,\"custom_display_name\":\"A4\"},{\"height_microns\":210000,\"name\":\"ISO_A5\",\"width_microns\":148000,\"custom_display_name\":\"A5\"},{\"height_microns\":355600,\"name\":\"NA_LEGAL\",\"width_microns\":215900,\"custom_display_name\":\"Legal\"},{\"height_microns\":279400,\"name\":\"NA_LETTER\",\"width_microns\":215900,\"custom_display_name\":\"Letter\"},{\"height_microns\":431800,\"name\":\"NA_LEDGER\",\"width_microns\":279400,\"custom_display_name\":\"Tabloid\"}]},\"page_orientation\":{\"option\":[{\"type\":\"PORTRAIT\"},{\"type\":\"LANDSCAPE\"},{\"is_default\":true,\"type\":\"AUTO\"}]}},\"version\":\"1.0\"},\"displayName\":\"Save as PDF\",\"extensionId\":\"\",\"extensionName\":\"\",\"icon\":\"cr:insert-drive-file\"},{\"id\":\"Microsoft Print to PDF\",\"origin\":\"local\",\"account\":\"\",\"capabilities\":{\"printer\":{\"color\":{\"option\":[{\"is_default\":true,\"type\":\"STANDARD_COLOR\",\"vendor_id\":\"2\"},{\"type\":\"STANDARD_MONOCHROME\",\"vendor_id\":\"1\"}]},\"copies\":{\"default\":1,\"max\":1},\"dpi\":{\"option\":[{\"horizontal_dpi\":600,\"is_default\":true,\"vertical_dpi\":600}]},\"media_size\":{\"option\":[{\"custom_display_name\":\"Letter\",\"height_microns\":279400,\"name\":\"NA_LETTER\",\"vendor_id\":\"1\",\"width_microns\":215900},{\"custom_display_name\":\"Tabloid\",\"height_microns\":431800,\"name\":\"NA_LEDGER\",\"vendor_id\":\"3\",\"width_microns\":279400},{\"custom_display_name\":\"Legal\",\"height_microns\":355600,\"name\":\"NA_LEGAL\",\"vendor_id\":\"5\",\"width_microns\":215900},{\"custom_display_name\":\"Statement\",\"height_microns\":215900,\"name\":\"NA_INVOICE\",\"vendor_id\":\"6\",\"width_microns\":139700},{\"custom_display_name\":\"Executive\",\"height_microns\":266700,\"name\":\"NA_EXECUTIVE\",\"vendor_id\":\"7\",\"width_microns\":184100},{\"custom_display_name\":\"A3\",\"height_microns\":420000,\"name\":\"ISO_A3\",\"vendor_id\":\"8\",\"width_microns\":297000},{\"custom_display_name\":\"A4\",\"height_microns\":297000,\"is_default\":true,\"name\":\"ISO_A4\",\"vendor_id\":\"9\",\"width_microns\":210000},{\"custom_display_name\":\"A5\",\"height_microns\":210000,\"name\":\"ISO_A5\",\"vendor_id\":\"11\",\"width_microns\":148000},{\"custom_display_name\":\"B4 (JIS)\",\"height_microns\":364000,\"name\":\"JIS_B4\",\"vendor_id\":\"12\",\"width_microns\":257000},{\"custom_display_name\":\"B5 (JIS)\",\"height_microns\":257000,\"name\":\"JIS_B5\",\"vendor_id\":\"13\",\"width_microns\":182000}]},\"page_orientation\":{\"option\":[{\"is_default\":true,\"type\":\"PORTRAIT\"},{\"type\":\"LANDSCAPE\"},{\"type\":\"AUTO\"}]},\"supported_content_type\":[{\"content_type\":\"application/pdf\"}]},\"version\":\"1.0\"},\"displayName\":\"Microsoft Print to PDF\",\"extensionId\":\"\",\"extensionName\":\"\",\"icon\":\"print-preview:print\"}],\"isCssBackgroundEnabled\":true,\"customMargins\":{},\"dpi\":{\"horizontal_dpi\":600,\"is_default\":true,\"vertical_dpi\":600,\"name\":\"600 dpi\"},\"isHeaderFooterEnabled\":false,\"isLandscapeEnabled\":true,\"marginsType\":1,\"mediaSize\":{\"height_microns\":297000,\"is_default\":true,\"name\":\"ISO_A4\",\"width_microns\":210000,\"custom_display_name\":\"A4\"}}"

CHROME_PREFERENCES = {
    'printing.print_preview_sticky_settings.appState': CHROME_SETTINGS_APPSTATE,
    'savefile.default_directory': str(TEMP_PDF_DOWNLOAD_DIR.absolute())
}

LOAD_QUESTION_MAX_WAIT_TIME = 20

# Required to wait until the question statement is loaded
QUESTION_STATEMENT_XPATH = '//*[@id="root"]/div/div[6]/div[6]/div/div/div/div/div/div[2]/div[3]/div/div[2]/div'

# Time to wait to le the hints to expand
HINT_EXPAND_WAIT_TIME = 3.5

# ================================================================
# Configurations for question_pdf downloader
RUN_question_solution_videos = True # If previously downloaded then set False

ALLOWED_ORIGIN_FOR_VIDEOS = "https://www.algoexpert.io/"
REQUEST_HEADERS_FOR_VIMEO_SITE = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9,bn;q=0.8",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Host": "player.vimeo.com",
    "Pragma": "no-cache",
    "Referer": ALLOWED_ORIGIN_FOR_VIDEOS,
    "sec-ch-ua": '"Google Chrome";v="95", "Chromium";v="95", ";Not A Brand";v="99"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "Windows",
    "Sec-Fetch-Dest": "iframe",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "cross-site",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36",
}

VIDEO_URLS_REGEX = re.compile(r"(?:\")(?P<url>https://vod-progressive.+?mp4)(?:\")(?:.+?)\"quality\":\"(?P<quality>.+?)\"", re.MULTILINE)
