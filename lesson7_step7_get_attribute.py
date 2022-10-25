from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    chest = browser.find_element(By.CSS_SELECTOR, 'img').get_attribute('valuex')
    x = calc(chest)

    result = browser.find_element(By.CSS_SELECTOR, 'input')
    result.send_keys(x)

    button1 = browser.find_element(By.ID, 'robotCheckbox')
    button1.click()

    button2 = browser.find_element(By.ID, 'robotsRule')
    button2.click()

    button3 = browser.find_element(By.CSS_SELECTOR, 'button')
    button3.click()

finally:
    time.sleep(10)
    browser.quit()
