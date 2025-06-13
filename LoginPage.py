from threading import Thread, Event
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pyotp
import time
from Exim.ScreenRecording import record_screen


def start_driver():
    chrome_path = "D:\\New Python\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe"
    service = Service(chrome_path)
    options = Options()
    prefs = {
        "profile.password_manager_enabled": False,
        "credentials_enable_service": False
    }
    options.add_experimental_option("prefs", prefs)
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--disable-notifications")
    driver = webdriver.Chrome(service=service, options=options)
    return driver


def login(driver):
    driver.get("https://staging.bharathexim.com/login")
    time.sleep(2)
    alert = driver.switch_to.alert
    alert.accept()
    driver.maximize_window()
    time.sleep(1)


def username(driver):
    email_input = driver.find_element(By.XPATH, "(//input[@placeholder='Enter email id'])[1]")
    email_input.send_keys("Ddttester3@gmail.com")


def password(driver):
    password_input = driver.find_element(By.XPATH, "(//input[@placeholder='Enter password'])[1]")
    password_input.send_keys("test@1234")


def perform_login(driver):
    login_button = driver.find_element(By.XPATH, "(//button[normalize-space()='Login'])[1]")
    login_button.click()
    time.sleep(1)


def perform_otp(driver):
    totp_secret = "IM6HU6SGKASXUYZI"
    totp = pyotp.TOTP(totp_secret)
    otp = totp.now()
    print("Generated OTP:", otp)
    time.sleep(1)
    autherntication = driver.find_element(By.XPATH, "(//input[@placeholder='Enter 6 digit Google Auth OTP'])[1]")
    autherntication.send_keys(otp)
    time.sleep(1)


if __name__ == "__main__":
    output_path = r"D:\New Python\Recorded Videos\Login_page.mp4"
    stop_event = Event()
    t = Thread(target=record_screen, args=(output_path, stop_event))
    t.start()

    driver = None
    try:
        driver = start_driver()
        login(driver)
        username(driver)
        password(driver)
        perform_login(driver)
        perform_otp(driver)
        perform_login(driver)
    finally:
        if driver:
            driver.quit()
        stop_event.set()  # Signal recording to stop
        t.join()
        print(f"Screen recording saved to: {output_path}")
