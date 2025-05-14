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
# driver.quit()

# ***** Access Registration/ Login *****


login_button = driver.find_element(By.CLASS_NAME, "btn-login")
login_button.click()


# # Cari field Username dan masukkan teks (salah)
# username_field = driver.find_element(By.type, "search")
# username_field.send_keys("student")  # Username salah

# # Cari field Password dan masukkan teks (salah)
# password_field = driver.find_element(By.ID, "password")
# password_field.send_keys("wrong_pass")  # Password salah

# # Tekan tombol login
# login_button = driver.find_element(By.ID, "submit")
# login_button.click()

# # Tunggu beberapa detik
# time.sleep(3)

# # Coba cari pesan error
# try:
#     error_message = driver.find_element(By.ID, "error").text
#     print(f"Login gagal: {error_message}")
# except:
#     print("Tidak ada pesan error ditemukan.")

# # Tunggu sebelum menutup browser
# time.sleep(3)
# driver.quit()
