from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome("/usr/local/bin/chromedriver")
browser.get(link)

input1 = browser.find_element_by_name("firstname")
input1.send_keys("Abel")

input2 = browser.find_element_by_name("lastname")
input2.send_keys("Atlas")

input3 = browser.find_element_by_name("email")
input3.send_keys("abel.a@icloud.com")

#Getting directory by lesson2.2_step7.py
current_dir = os.path.abspath(os.path.dirname("/Users/aialatlasov/Desktop/"))
#Downloading file
file_name = "forlesson2.txt"
#Getting file's directory
file_path = os.path.join(current_dir, file_name)

#script for element
element = browser.find_element(By.CSS_SELECTOR, "[type = 'file']")
element.send_keys(file_path)

#this for submit button:
button = browser.find_element_by_css_selector("button.btn").click()

time.sleep(10)
browser.close()
browser.quit()
