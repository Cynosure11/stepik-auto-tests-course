from selenium import webdriver
import math
import time

link = "http://suninjuly.github.io/alert_accept.html"
browser = webdriver.Chrome("/usr/local/bin/chromedriver")
browser.get(link)

#click on botton
button = browser.find_element_by_xpath("//button[text()='I want to go on a magical journey!']")
button.click()

#accept alert in window
alert = browser.switch_to.alert
alert.accept()

#sum of this math
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
x_element = browser.find_element_by_id("input_value")
x = x_element.text
y = calc(x)
input1 = browser.find_element_by_id("answer")
input1.send_keys(y)

#click on Submit .btn
button = browser.find_element_by_css_selector("button.btn").click()

#get your code on terminal
alert = browser.switch_to.alert
alert_text = alert.text

time.sleep(8)
browser.close()

