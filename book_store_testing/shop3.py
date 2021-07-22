from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("http://practice.automationtesting.in/")
driver.implicitly_wait(7)
driver.maximize_window()

# Переход на вкладку Shop
shop_tab = driver.find_element_by_link_text("Shop")
shop_tab.click()
driver.execute_script("window.scrollBy(0, 300);")
# Добавление книги в корзину
html5_webapp_development_book = driver.find_element_by_css_selector(".post-182 .add_to_cart_button")
html5_webapp_development_book.click()
time.sleep(3)
html5_webapp_development_book = driver.find_element_by_css_selector(".post-180 .add_to_cart_button")
html5_webapp_development_book.click()
basket_btn = driver.find_element_by_class_name("wpmenucart-contents")
basket_btn.click()
time.sleep(5)
remove_first_item_btn = driver.find_element_by_class_name("remove")
remove_first_item_btn.click()
undo_btn = driver.find_element_by_link_text("Undo?")
undo_btn.click()
quantity_field = driver.find_element_by_css_selector("tbody > tr:nth-child(1) .product-quantity input")
quantity_field.clear()
quantity_field.send_keys("3")
update_basket = driver.find_element_by_name("update_cart")
update_basket.click()
quantity_field = driver.find_element_by_css_selector("tbody > tr:nth-child(1) .product-quantity input")
quantity_field_value = quantity_field.get_attribute("value")
assert quantity_field_value == '3'
time.sleep(5)
apply_coupon = driver.find_element_by_name("apply_coupon")
apply_coupon.click()
error_message = driver.find_element_by_css_selector(".woocommerce-error")
error_message_text = error_message.text
assert error_message_text == 'Please enter a coupon code.'
driver.quit()