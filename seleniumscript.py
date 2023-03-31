from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import StaleElementReferenceException
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

#Instructions:
#1. Make python virtual enviornment
#2. Activate virtual enviornment 
#3. pip install selenium
#4. create questions.txt, where each line is a new question
#5. put login credentials in variables
#6.  python3 seleniumscript.py in terminal

#adding Chrome Profile Path
#set chromedriver.exe path

#Replace Login Credentials:
mail_address = "EMAIL_ADDRESS"
password = "PASSWORD"


options = webdriver.ChromeOptions()
options.add_argument('user-data-dir=/Users/ganeshdanke/Library/Application Support/Google/Chrome')
options.add_argument('profile-directory=Profile 8')

driver = webdriver.Chrome(executable_path="/Applications/Google_Chrome.app")
driver.get("https://accounts.google.com/ServiceLogin?elo=1")
driver.implicitly_wait(0.2)
wait = WebDriverWait(driver, 10)

x = wait.until(EC.presence_of_element_located(("xpath", "//input[@type='email']")))
x = driver.find_element("xpath", "//input[@type='email']")
x.send_keys(mail_address)
x.send_keys(Keys.ENTER)

time.sleep(15)

x = wait.until(EC.presence_of_element_located(("xpath", "//input[@type='password']")))
x = driver.find_element("xpath", "//input[@type='password']")
x.send_keys(password)
x.send_keys(Keys.ENTER)


time.sleep(15)

driver.implicitly_wait(0.2)
driver.get("https://www.google.com/")
time.sleep(.5)


file1 = open('questions.txt', 'r')
File = file1.readlines()
time.sleep(1)

def runSearches(list):
    if list:
        wait = WebDriverWait(driver, 1)
        m = wait.until(EC.presence_of_element_located((By.NAME, 'q')))
        m = driver.find_element("name", "q")
        m = wait.until(EC.presence_of_element_located((By.NAME, 'q')))
        m.send_keys(list[0])
        m = wait.until(EC.presence_of_element_located((By.NAME, 'q')))
        time.sleep(1)
        #m.send_keys(Keys.ENTER)
        time.sleep(1)
        driver.get("https://www.google.com/")
        time.sleep(1)
        return runSearches(list[1:])
    else:
        print("done")

runSearches(File)

  






