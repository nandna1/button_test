from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

# Set the path for the GeckoDriver
gecko_driver_path = r"C:\Users\nanda\OneDrive\Desktop\geckodriver-v0.34.0-win32\geckodriver.exe"
# Set the path for the Firefox binary
firefox_binary_path = r"C:\Program Files\Mozilla Firefox\firefox.exe" 

# Set the default web page URL
default_web_page = 'https://www.google.com'

# Set Firefox options
options = Options()
options.binary_location = firefox_binary_path
options.add_argument("--start-maximized")  # Optional: Start Firefox maximized

# Initialize the WebDriver
service = Service(gecko_driver_path)
driver = webdriver.Firefox(service=service, options=options)

# Open the default web page
driver.get(default_web_page)

# Perform any additional actions here

# Close the browser
driver.quit()
