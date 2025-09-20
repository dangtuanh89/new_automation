from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://daim-vn.com/")
print(f"The web's url is: {driver.current_url}")
driver.refresh()
print(f"The web's url after refresh is: {driver.current_url}")
driver.quit()