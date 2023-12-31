import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

options = webdriver.ChromeOptions()
options.add_argument('ignore-certificate-errors')
driver = webdriver.Chrome(options)
try:
    wait = WebDriverWait(driver, 10)
    action = ActionChains(driver)
    driver.get('https://www.alljobs.co.il')

    # Field selection
    wait.until(EC.presence_of_element_located(
        (By.XPATH, "//div[contains(text(), 'בחרו תחום')]")
    )).click()

    # Select 'Software'
    wait.until(EC.presence_of_element_located(
        (By.XPATH, '//div[@id=235]')
    )).click()

    driver.find_element(By.XPATH, "//button[@id='CategorySearch']").click()
    time.sleep(10)
finally:
    driver.quit()