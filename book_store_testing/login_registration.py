from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://practice.automationtesting.in/")
driver.implicitly_wait(5)
driver.maximize_window()

my_account_menu = driver.find_element_by_link_text("My Account")
my_account_menu.click()
email_field = driver.find_element_by_id("reg_email")
email_field.send_keys("test@email.com")
password_field = driver.find_element_by_id("reg_password")
password_field.send_keys("SomeHardPassword123!@#!@#")
register_btn = driver.find_element_by_name("register")
register_btn.click()
driver.quit()