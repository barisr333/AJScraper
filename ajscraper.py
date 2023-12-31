import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from dotenv import load_dotenv

load_dotenv()
options = webdriver.ChromeOptions()
options.add_argument('ignore-certificate-errors')
driver = webdriver.Chrome(options)
try:
    wait = WebDriverWait(driver, 30)
    action = ActionChains(driver)
    driver.get('https://www.alljobs.co.il')
    

finally:
    driver.quit()