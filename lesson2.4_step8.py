from selenium import webdriver

#import libraries
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time

#Getting WebDriver
browser = webdriver.Chrome("/usr/local/bin/chromedriver")
browser.get("http://suninjuly.github.io/explicit_wait2.html")

#Wait until 100$
option1 = WebDriverWait(browser, 12).until(
         EC.text_to_be_present_in_element((By.ID, "price"), "100"))
option2 = browser.find_element_by_id("book")
option2.click()

#math is real magic!
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
x_element = browser.find_element_by_id("input_value")
x = x_element.text
y = calc(x)
input1 = browser.find_element_by_id("answer")
input1.send_keys(y)

#click button
button = browser.find_element_by_id("solve").click()


time.sleep(5)
browser.close()