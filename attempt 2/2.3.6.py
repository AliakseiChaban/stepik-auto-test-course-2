from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

link = "http://suninjuly.github.io/redirect_accept.html"


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.CSS_SELECTOR, "button.trollface").click()

    new_tab = browser.window_handles[1]
    browser.switch_to.window(new_tab)

    x_value = browser.find_element(By.ID, "input_value")
    x = calc(x_value.text)

    inp_field = browser.find_element(By.ID, "answer")
    inp_field.send_keys(x)

    smbt_btn = browser.find_element(By.XPATH, "//button[text()='Submit']")
    smbt_btn.click()

finally:
    time.sleep(10)
    browser.quit()
