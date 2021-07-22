from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("http://practice.automationtesting.in/")
driver.implicitly_wait(7)
driver.maximize_window()

# Переход на вкладку Shop
shop_tab = driver.find_element_by_link_text("Shop")
shop_tab.click()
driver.execute_script("window.scrollBy(0, 300);")
html5_webapp_development_book = driver.find_element_by_css_selector(".post-182 .add_to_cart_button")
html5_webapp_development_book.click()
# Переход в корзину
basket_btn = driver.find_element_by_class_name("wpmenucart-contents")
basket_btn.click()
checkout_btn = WebDriverWait(driver, 10).until(
EC.element_to_be_clickable((By.CLASS_NAME, "checkout-button")))
checkout_btn.click()
# Заполнение обязательных полей
first_name = WebDriverWait(driver, 10).until(
EC.element_to_be_clickable((By.ID, "billing_first_name")))
first_name.send_keys("John")
last_name = driver.find_element_by_id("billing_last_name")
last_name.send_keys("Snow")
email = driver.find_element_by_id("billing_email")
email.send_keys("test@email.com")
phone = driver.find_element_by_id("billing_phone")
phone.send_keys("877777777777")
country = driver.find_element_by_id("s2id_billing_country")
country.click()
country_search = driver.find_element_by_id("s2id_autogen1_search")
country_search.send_keys("Christmas Island")
country_second_field = driver.find_element_by_class_name("select2-match")
country_second_field.click()
address = driver.find_element_by_id("billing_address_1")
address.send_keys("The Wall")
city = driver.find_element_by_id("billing_city")
city.send_keys("Winterfell")
state = driver.find_element_by_id("billing_state")
state.send_keys("North")
postcode = driver.find_element_by_id("billing_postcode")
postcode.send_keys("100200300")
driver.execute_script("window.scrollBy(0, 600);")
# Выбор способа оплаты: чек
time.sleep(5)
payment_check = driver.find_element_by_id("payment_method_cheque")
payment_check.click()
place_order_btn = driver.find_element_by_id("place_order")
place_order_btn.click()
# Проверка что появилось сообщение об успешном заказе
success_message = WebDriverWait(driver, 10).until(
EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".woocommerce-thankyou-order-received"),
"Thank you. Your order has been received."))
# Проверка что выбран платёжный способ: чек
payment_method_message = WebDriverWait(driver, 10).until(
EC.text_to_be_present_in_element((By.CSS_SELECTOR, "tfoot > tr:nth-child(3) > td"), "Check Payments"))
driver.quit()