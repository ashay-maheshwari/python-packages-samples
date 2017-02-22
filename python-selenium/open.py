from selenium import webdriver

linked_in_url = "https://www.linkedin.com/"
driver = webdriver.Firefox()
driver.get(linked_in_url)


inputElement = driver.find_element_by_id("login-email")
inputElement.send_keys("aashay")

