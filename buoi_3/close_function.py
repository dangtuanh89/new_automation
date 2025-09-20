from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://daim-vn.com/")
driver.execute_script("window.open('https://google.com')")
time.sleep(2)
driver.switch_to.window(driver.window_handles[1])
print(f"The web's title is: {driver.title}")
driver.close()