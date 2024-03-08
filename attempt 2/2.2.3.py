import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    number_1 = browser.find_element(By.ID, "num1")
    number_2 = browser.find_element(By.ID, "num2")
    a = int(number_1.text)
    b = int(number_2.text)
    c = a + b

    dropdown_element = Select(browser.find_element(By.ID, "dropdown"))
    dropdown_element.select_by_value(str(c))

    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

finally:
    time.sleep(5)
    browser.quit()
