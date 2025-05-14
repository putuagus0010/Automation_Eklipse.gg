from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

# ***** Access Landing Page *****

# To Keep Chrome open after the script is finished
options = Options()
options.add_experimental_option("detach", True)

# Inisialisasi WebDriver
driver = webdriver.Chrome(options=options)

# Open Chrome and access to eklipse.gg
driver.get("https://eklipse.gg")
driver.maximize_window()

# Wait a few seconds for the page to be ready
time.sleep(2)

# Verify that the search result contains the text "eklipse.gg"
assert "eklipse.gg" in driver.page_source.lower()

# Verify that access was successful and exit
print("✅ Test Success: Landing Page eklipse.gg Appears.")
input("Press Enter to exit...")
driver.quit()
