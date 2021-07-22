from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://practice.automationtesting.in/")
driver.execute_script("window.scrollTo(0, 600)")
ruby = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div/div/div/div[2]/div/div/div/div/div[2]/div[1]/div/div/ul/li/a[1]/h3")
ruby.click()
reviews = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div/div[3]/ul/li[2]/a")
reviews.click()
stars = driver.find_element_by_class_name("star-5")
stars.click()
comment = driver.find_element_by_id("comment")
comment.send_keys("Nice book")
author = driver.find_element_by_id("author")
author.send_keys("Alee")
email = driver.find_element_by_id("email")
email.send_keys("alee@mail.ru")
submit = driver.find_element_by_id("submit")
submit.click()

