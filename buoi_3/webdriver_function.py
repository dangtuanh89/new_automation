from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://daim-vn.com/")
print(f"The web's title is: {driver.title}")
driver.get("https://google.com")
print(f"The web's title is: {driver.title}")

driver.back()
print(f"The web's title is: {driver.title}")

driver.forward()
print(f"The web's title is: {driver.title}")
driver.quit()

