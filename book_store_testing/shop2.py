from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("http://practice.automationtesting.in/")
driver.implicitly_wait(5)
driver.maximize_window()

# Переход на вкладку Shop
shop_tab = driver.find_element_by_link_text("Shop")
shop_tab.click()
# Добавление книги в корзину
html5_webapp_development_book = driver.find_element_by_css_selector(".post-182 > a h3")
html5_webapp_development_book.click()
html5_webapp_development_book_add_btn = driver.find_element_by_css_selector(".single_add_to_cart_button")
html5_webapp_development_book_add_btn.click()
# Проверка количества товаров в корзине
basket_item_value = driver.find_element_by_css_selector(".wpmenucart-contents .cartcontents")
basket_item_value_text = basket_item_value.text
assert basket_item_value_text == "1 Item"
# Проверка стоимости товаров в корзине
basket_price_value = driver.find_element_by_css_selector(".wpmenucart-contents .amount")
basket_price_value_text = basket_price_value.text
assert basket_price_value_text == "₹180.00"
basket_btn = driver.find_element_by_class_name("wpmenucart-contents")
basket_btn.click()
# Получение содержимого subtotal
subtotal_price = WebDriverWait(driver, 10).until(
EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".cart-subtotal .woocommerce-Price-amount"), "₹180.00"))
# Получение содержимого total
total_price = WebDriverWait(driver, 10).until(
EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".order-total .woocommerce-Price-amount"), "₹189.00"))
driver.quit()