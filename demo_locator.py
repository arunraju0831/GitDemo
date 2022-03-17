from selenium import webdriver
import time
# Invokes chromedriver.exe file for invoking websites
driver = webdriver.Chrome(executable_path="C:\\Users\\arunraju.m\\Softwares\\chromedriver_win32\\chromedriver.exe")

driver.get("http://www.solsavi.in")  # Enters Solsavi website

driver.find_element_by_id("grad1").click()  # Clicks Get Started button

driver.find_element_by_id("example-text-input").send_keys("600088")  # Enters pincode

# Change the for value
# driver.find_element_by_xpath("//label[@for='radio-Industrial']").click()
driver.find_element_by_xpath("//label[@for='radio-Industrial']").click()  # Clicks Consumer types

driver.find_element_by_xpath("//label[@for='radio-Low Tension (LT)']").click()  # Voltage field

# while driver.
driver.find_element_by_css_selector("span[class='mat-button-wrapper']").click()  # Next button

