from selenium import webdriver
import time
browser = webdriver.Chrome()
browser.get("https://github.com")
# time.sleep(2)
browser.set_window_size(1924,1268)
signin_link = browser.find_element_by_link_text("Sign in")
signin_link.click()
username_box = browser.find_element_by_id("login_field")
username_box.send_keys("bbikrambbasnet444@gmail.com")
password_box = browser.find_element_by_id("password")
password_box.send_keys("monkey don44")
password_box.submit()

# assert "BBIKRAM" in browser.page_source
profile_link = browser.find_element_by_class_name("user-profile-link")
link_label = profile_link.get_attribute("innerHTML")
assert "BBIKRAM" in link_label
browser.quit()