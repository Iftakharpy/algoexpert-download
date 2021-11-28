import json
from pathlib import Path
from selenium.webdriver import FirefoxOptions, Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyperclip as clip

# Configs
FIREFOX_PROFILE_PATH = "/home/iftakhar/.mozilla/firefox/c8w8ks2g.default-release"
QUESTIONS_DIR = Path(r"/home/iftakhar/Desktop/AlgoExpert/Coding Interview Questions")

# Set profile
firefox_options = FirefoxOptions()
firefox_options.profile = FIREFOX_PROFILE_PATH

def submit_question(driver:Firefox, url:str, solution:str, LOAD_QUESTION_MAX_WAIT_TIME=10):
    driver.get(url)

    input_area_xpath = "/html/body/div[2]/div/div[4]/div[6]/div/div[3]/div/div[1]/div/div[4]/div[1]/div"
    
    WebDriverWait(driver, LOAD_QUESTION_MAX_WAIT_TIME).until(EC.visibility_of_element_located((By.XPATH, input_area_xpath)))

    input_area = driver.find_element(By.XPATH, input_area_xpath)
    input_area.click()
    actions = ActionChains(driver) 
    
    # Select all text
    actions.key_down(Keys.CONTROL)
    actions.key_down("a")
    actions.perform()

    # Clear selected text
    actions.key_down(Keys.BACKSPACE)
    actions.perform()
    
    # Copy solution to clipboard
    clip.copy(solution)

    # Paste Copied text
    actions.key_down(Keys.CONTROL)
    actions.key_down("v")
    actions.perform()

    # run_code_btn_xpath = "//button[span[contains(text(),'Run Code')]]"
    # run_code_btn = driver.find_element(By.XPATH, run_code_btn_xpath)
    # run_code_btn.click()
    
    submit_code_btn_xpath = "//button[span[contains(text(),'Submit Code')]]"
    submit_code_btn = driver.find_element(By.XPATH, submit_code_btn_xpath)
    submit_code_btn.click()

    # Wait for result
    result_xpath = "//p[contains(text(), 'Congratulations')]"
    WebDriverWait(driver, LOAD_QUESTION_MAX_WAIT_TIME).until(EC.visibility_of_element_located((By.XPATH, result_xpath)))


def main():
    # Run browser
    browser = Firefox(options=firefox_options)
    
    questions = list(QUESTIONS_DIR.glob("*/*_data.json"))
    questions.sort()

    for question_path in questions:
        with open(question_path) as f:
            question_data = json.load(f)

            question_name = question_data['name']
            url = f"https://www.algoexpert.io/questions/{question_name}"
            solution:str = question_data['resources']['python']['solutions'][0]
            solution = solution[57:]

            print(f"Submitting: {question_path}")
            submit_question(browser, url, solution)
    
    # Quit browser
    browser.quit()

if __name__ == "__main__":
    main()
