import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/alert_accept.html"

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    button_element = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button_element.click()

    confirm_allert = browser.switch_to.alert
    confirm_allert.accept()

    input_value = browser.find_element(By.ID, "input_value")
    x = int(input_value.text)
    y = calc(x)

    input_field = browser.find_element(By.ID, "answer")
    input_field.send_keys(y)

    submit_btn_element = browser.find_element(By.CSS_SELECTOR, "button.btn")
    submit_btn_element.click()

finally:
    time.sleep(10)
    browser.quit()
