# Prerequisites
1. `authorization` header this is required to interact with any endpoint.
2. Add all other headers from the chrome devtools which are optional but might be good idea to avoid bot detection.

# Get data about question
| HTTP endpoint        | HTTP method           | Body |
| ------------- |:-------------:| :----- |
| `https://prod.api.algoexpert.io/api/problems/v1/algoexpert/coding-questions/get`| `POST` | `{'name': "Target question name"}` |


# Get test cases for question
| HTTP endpoint        | HTTP method           | Body |
| ------------- |:-------------:| :----- |
| `https://prod.api.algoexpert.io/api/problems/v1/run_json_tests`| `POST` | [body](#run_json_tests_body) |

## [Body for run_json_tests endpoint](run_json_tests_body)
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

# Auto format json files
To auto format json files follow these steps
1. Open command line/terminal/shell
2. Change working directory to the parent directory of all json files
3. Run on command line `npm init`
4. Run on command line `npm i prettier`
5. Add following script in package.json: `"pretty": "prettier --write \"./**/*.{js,jsx,json}\""`
6. Run `npm run pretty`
