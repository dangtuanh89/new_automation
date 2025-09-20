from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://daim-vn.com/")
'''
print(f'The url of current page is: {driver.current_url}')
print(f"The web's title is: {driver.title}")
print(f'The current window handle is: {driver.current_window_handle}')
print(f'The name of the browser is: {driver.name}')
print(f'The page source is: {driver.page_source}')
'''
# Mở thêm tab mới với Google
driver.execute_script("window.open('https://google.com');")
time.sleep(2)  # Đợi tab mới mở ra
print(f'The handles of all windows is: {driver.window_handles}')
driver.quit()