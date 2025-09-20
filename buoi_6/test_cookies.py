import pickle
import selenium.webdriver

# Save the current cookies as a Python object using pickle
driver = selenium.webdriver.Firefox()
driver.get("http://www.google.com")
pickle.dump(driver.get_cookies(), open("cookies.pkl", "wb"))

# And later to add them back
import pickle
import selenium.webdriver

driver = selenium.webdriver.Firefox()
driver.get("http://www.google.com")
cookies = pickle.load(open("cookies.pkl", "rb"))
for cookie in cookies:
    driver.add_cookie(cookie)
driver.quit()
