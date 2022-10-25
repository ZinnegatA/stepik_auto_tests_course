from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    element1 = browser.find_element(By.XPATH, '//label[contains(text(), "First name")]/following-sibling::input')
    element2 = browser.find_element(By.XPATH, '//label[contains(text(), "Last name")]/following-sibling::input')
    element3 = browser.find_element(By.XPATH, '//label[contains(text(), "Email")]/following-sibling::input')
    for el in element1, element2, element3:
        el.send_keys("Ответ")

    time.sleep(5)
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    time.sleep(1)

    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()
