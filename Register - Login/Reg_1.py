from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import re

# ***** Register Page Automation *****

# Keep Chrome open after execution
options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

# Open Eklipse website
driver.get("--")
driver.maximize_window()
time.sleep(2)

# Check if landing page is loaded
if 'eklipse.gg' in driver.current_url.lower():
    print('✅ Landing page appears')
else:
    print('❌ Landing page does not appear')
    driver.quit()

try:
    # Click "Sign Up For Free" button
    register_button = driver.find_element(By.LINK_TEXT, 'Sign Up For Free')
    register_button.click()
    time.sleep(2)
    print("✅ Navigated to the registration page")

    # Test data
    name = "test2 Automation"
    email = "test2.as@example.com"
    password = "TestPassword123!"

    # Email format validation
    email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if not re.match(email_pattern, email):
        print("❌ Invalid email format")
        driver.quit()
        exit()

    # Fill in registration form
    driver.find_element(By.NAME, "name").send_keys(name)
    driver.find_element(By.NAME, "email").send_keys(email)
    driver.find_element(By.NAME, "password").send_keys(password)
    driver.find_element(By.NAME, "password_confirmation").send_keys(password)
    print("✅ Form filled successfully")

    # MANUAL PAUSE: CAPTCHA validation
    input("🛑 Please check the 'I'm not a robot' checkbox, then press ENTER...")
    input("🛑 Complete the image verification, then press ENTER...")

    try:
        # Click the Sign Up button
        signup_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        signup_button.click()

        # Wait until redirected to home page
        try:
            WebDriverWait(driver, 10).until(
                lambda d: "--" in d.current_url.lower()
            )
            print("✅ Successfully signed up and redirected to Home:", driver.current_url)
        except:
            print("❌ Failed to redirect to the Home page. Possible error during sign up.")
            print("🔍 Current URL:", driver.current_url)
            input("🛑 Press ENTER to manually close the browser after checking.")
            driver.quit()

    except Exception as e:
        print(f"❌ Failed to click the Sign Up button: {e}")
        driver.quit()

except Exception as e:
    print(f"❌ Registration failed: {e}")
    driver.quit()
