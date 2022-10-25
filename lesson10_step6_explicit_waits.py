from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
    )
    browser.find_element(By.ID, 'book').click()
    res = browser.find_element(By.CSS_SELECTOR, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", res)
    text = browser.find_element(By.ID, 'input_value').text
    result = browser.find_element(By.CSS_SELECTOR, 'input')
    result.send_keys(calc(text))
    browser.find_element(By.ID, 'solve').click()

finally:
    time.sleep(5)
    browser.quit()
