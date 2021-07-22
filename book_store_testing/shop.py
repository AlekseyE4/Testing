from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("http://practice.automationtesting.in/")
driver.implicitly_wait(5)
driver.maximize_window()

# Логин
my_account_menu = driver.find_element_by_link_text("My Account")
my_account_menu.click()
user_name_field = driver.find_element_by_id("username")
user_name_field.send_keys("test@email.com")
password_field = driver.find_element_by_id("password")
password_field.send_keys("SomeHardPassword123!@#!@#")
login_btn = driver.find_element_by_name("login")
login_btn.click()
# Переход на вкладку Shop
shop_tab = driver.find_element_by_link_text("Shop")
shop_tab.click()
# Проверка сортировки по умолчанию
items_selector = driver.find_element_by_name("orderby")
items_selector_default = items_selector.get_attribute("value")
if items_selector_default == "menu_order":
    print("Выбрана сортировка по умолчанию")
else:
    print("Выбрана сортировка НЕ по умолчанию")
# Сортировка от большего к меньшему и проверка
select = Select(items_selector)
select.select_by_value("price-desc")
items_selector = driver.find_element_by_name("orderby")
items_selector_low = items_selector.get_attribute("value")
if items_selector_low == "price-desc":
    print("Выбрана сортировка по убыванию")
else:
    print("Выбрана сортировка НЕ по убыванию")
driver.quit()

