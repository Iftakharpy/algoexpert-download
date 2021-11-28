# algoexpert-download
Downloads all questions and solutions using python from https://www.algoexpert.io/questions 

# Requirements
1. Update variables that are `directory/file paths` according to your preferences or to make compatible with your environment in `config.py`.
2. Update `AUTH_KEY` in the `config.py` file to download list of questions and question data [more info][question-data-readme].
3. Install requirements to download questions as pdf file and to download solution videos.
4. More on [question pdf][question-pdf-readme]
5. More on [question solution videos][question-solution-videos-readme]
6. [submit.py][solution-submitter] is a simple script to submit solutions using firefox browser
   Requirements:
    1. [firefox browser][firefox-browser]
    2. [geokodriver][firefox-geokodriver]
    3. Add the directory to `PATH` where [geokodriver][firefox-geokodriver] binary is located
    4. Install `xclip` using `sudo apt-get install xclip` command for linux users
    5. Login to your algoexpert account in firefox browser before running [submit.py][solution-submitter] script
    6. Also update `FIREFOX_PROFILE_PATH` and `QUESTIONS_DIR` according to your environment
7. Install requirements using `pip install -r requirements.txt`


[question-data-readme]: ./downloaders/question_data/README.md
[question-pdf-readme]: ./downloaders/question_pdf/README.md
[question-solution-videos-readme]: ./downloaders/question_solution/README.md
[solution-submitter]: ./submit.py
[firefox-browser]: https://www.mozilla.org/en-US/firefox/new/
[firefox-geokodriver]: https://github.com/mozilla/geckodriver/releases
