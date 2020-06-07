from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.get("https://facebook.com")
time.sleep(3)
browser.set_window_size(1226,1333)
time.sleep(3)
browser.maximize_window()
time.sleep(2)
browser.close()