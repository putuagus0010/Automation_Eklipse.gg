from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import re   

# ***** Account Setting Page Automation *****

# Setup Chrome
options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

# Go to Eklipse
driver.get("--")
driver.maximize_window()
time.sleep(2)

# Check landing page
if 'eklipse.gg' in driver.current_url.lower():
    print('✅ Landing Page Appears')
else:
    print('❌ Failed to open Landing Page')
    driver.quit()

try:
    # Click "Sign In" button
    sign_in_button = driver.find_element(By.LINK_TEXT, 'Sign In')
    sign_in_button.click()
    time.sleep(2)
    print("✅ Navigated to Sign In Page")

    # Credentials
    email = "putuagus001000@gmail.com"
    password = "1234@Lima"

    # Fill form
    driver.find_element(By.ID, "username").send_keys(email)
    driver.find_element(By.ID, "password").send_keys(password)
    print("✅ Email and Password entered")

    # Submit login
    login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    login_button.click()
    time.sleep(5)

    # Check if login success
    if 'home' in driver.current_url.lower():
        print("✅ Login Successful, Home Page Opened")
    else:
        print("❌ Login Failed or Wrong Credentials")
        driver.quit()

    # MANUAL PAUSE: CAPTCHA validation
    input("🛑 Close Level Up to Premium Today!")
    input("🛑 Skip For Now")

    try:
        # Wait to make sure navbar is loaded
        time.sleep(3)

        # Click user icon to open dropdown
        profile_icon = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "ic-user"))
        )
        profile_icon.click()
        time.sleep(5)

        # Click 'Account Settings' from dropdown
        account_settings = driver.find_element(By.XPATH, "//button[contains(., 'Account Settings')]")
        account_settings.click()
        print("✅ Account Settings clicked")

    except Exception as dropdown_error:
        print(f"❌ Failed to open Account Settings: {dropdown_error}")
        driver.quit()
        
except Exception as e:
    print(f"❌ Error during login: {e}")
    driver.quit()
