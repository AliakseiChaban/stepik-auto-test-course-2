import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "https://suninjuly.github.io/math.html"


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)

    input_field = browser.find_element(By.ID, "answer")
    input_field.send_keys(y)

    checkbox_element = browser.find_element(By.ID, "robotCheckbox")
    checkbox_element.click()

    radio_element = browser.find_element(By.ID, "robotsRule")
    radio_element.click()

    btn_element = browser.find_element(By.CSS_SELECTOR, "button.btn")
    btn_element.click()

finally:
    time.sleep(10)
    browser.quit()
