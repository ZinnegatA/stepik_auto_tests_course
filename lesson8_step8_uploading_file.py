from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    elements = browser.find_elements(By.CLASS_NAME, 'form-control')
    for el in elements:
        el.send_keys('answer')

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'task.txt')
    element = browser.find_element(By.ID, 'file')
    element.send_keys(file_path)

    submit = browser.find_element(By.CSS_SELECTOR, 'button')
    submit.click()

finally:
    time.sleep(10)
    browser.quit()
