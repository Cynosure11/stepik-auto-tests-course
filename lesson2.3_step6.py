from selenium import webdriver
import math
import time

link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome("/usr/local/bin/chromedriver")
browser.get(link)

#Script get new page
button = browser.find_element_by_xpath("//button[text()='I want to go on a magical journey!']")
button.click()
browser.switch_to_window(browser.window_handles[1])
#Можно было 
#new_window = browser.window_handles[1]
#browser.switch_to.window(new_window)

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

time.sleep(5)
browser.close()