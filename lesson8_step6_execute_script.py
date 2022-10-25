from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.ID, 'input_value')
    x = x_element.text
    y = calc(x)

    result = browser.find_element(By.CSS_SELECTOR, 'input')
    result.send_keys(y)

    button1 = browser.find_element(By.ID, 'robotCheckbox')
    button1.click()

    button2 = browser.find_element(By.ID, 'robotsRule')
    browser.execute_script("return arguments[0].scrollIntoView(true);", button2)
    button2.click()

    button3 = browser.find_element(By.CSS_SELECTOR, 'button')
    button3.click()


finally:
    time.sleep(10)
    browser.quit()

