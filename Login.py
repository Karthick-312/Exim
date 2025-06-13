import time
from selenium.webdriver.common.by import By

def login(driver, username, password):
    """Perform login with provided credentials."""
    driver.get("https://staging.bharathexim.com/login")
    time.sleep(2)

    # Handle alert
    try:
        alert = driver.switch_to.alert
        alert.accept()
    except:
        pass  # No alert present
    driver.maximize_window()
    time.sleep(1)

    # Enter credentials
    email_input = driver.find_element(By.XPATH, "(//input[@placeholder='Enter email id'])[1]")
    email_input.send_keys(username)

    password_input = driver.find_element(By.XPATH, "(//input[@placeholder='Enter password'])[1]")
    password_input.send_keys(password)

    # Click Login (you might need to adjust this selector)
    login_button = driver.find_element(By.XPATH, "//button[contains(text(),'Login')]")
    login_button.click()
    time.sleep(3)
