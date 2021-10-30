# Prerequisites
1. `authorization` header; this is required to interact with any endpoint.
2. Add all other headers from the chrome devtools which are optional but might be good idea to avoid bot detection.

Example of Headers for every requests sent to the AlgoExpert backend:
```json
{
    "authorization": "YOUR AUTH_KEY FROM CHROME DEVTOOLS",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36",
    "accept": "*/*",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "en-US,en;q=0.9,bn;q=0.8",
    "cache-control": "no-cache",
    "content-type": "text/plain;charset=UTF-8",
    "origin": "https://www.algoexpert.io",
    "pragma": "no-cache",
    "referer": "https://www.algoexpert.io/",
    "sec-ch-ua": "\"Google Chrome\";v=\"95\", \"Chromium\";v=\"95\", \";Not A Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "Windows",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
}
```

# Get full list of questions

HTTP Endpoint: `https://prod.api.algoexpert.io/api/problems/v1/algoexpert/coding-questions/list` 

Request Method: `POST` 

# Get data about question

HTTP Endpoint: `https://prod.api.algoexpert.io/api/problems/v1/algoexpert/coding-questions/get` 

Request Method: `POST` 

Request Body: 
``` json
{   
    "name": "Target question name"
}
```

---
# Get test cases for question

## Request 

HTTP Endpoint: `https://prod.api.algoexpert.io/api/problems/v1/run_json_tests` 

Request Method: `POST` 

Request Body: 
```json
{
    "language": "python",
    "questionName": "Two Number Sum",
    "userSolution": "def twoNumberSum(array, targetSum):\n    ns = {}\n    for n in array:\n        pm = targetSum - n\n        if pm in ns:\n            return [pm, n]\n        else:\n            ns[n] = True\n    return []",
    "questionVersion": 0,
    "product": "algoexpert"
}
```

Note: In HTTP POST request the data in the body must be string

---
# Auto format json files
To auto format json files follow these steps
1. Open command line/terminal/shell
2. Change working directory to the parent directory of all json files
3. Run on command line `npm init`
4. Run on command line `npm i prettier`
5. Add following script in package.json: `"pretty": "prettier --write \"./**/*.{js,jsx,json}\""`
6. Run `npm run pretty`
