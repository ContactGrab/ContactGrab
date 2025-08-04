from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import requests

# --- Setup Chrome Driver ---
options = Options()
options.add_argument("--headless")  # Run in headless mode
driver = webdriver.Chrome(options=options)

# --- Target Post ---
url = "https://www.instagram.com/p/POST_SHORTCODE/"

driver.get(url)
time.sleep(5)  # Wait for the content to load

# --- Get Image or Video ---
try:
    media = driver.find_element(By.XPATH, "//img[@decoding='auto']")
    media_url = media.get_attribute("src")
except:
    media = driver.find_element(By.XPATH, "//video")
    media_url = media.get_attribute("src")

print("Media URL:", media_url)

# --- Download the File ---
response = requests.get(media_url)
file_name = "instagram_content.jpg" if ".jpg" in media_url else "instagram_content.mp4"

with open(file_name, 'wb') as f:
    f.write(response.content)

print("Downloaded:", file_name)

driver.quit()
