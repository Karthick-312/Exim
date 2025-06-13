import time
import pyotp
import openpyxl
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


def start_driver():
    chrome_path = "D:\\New Python\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe"
    service = Service(chrome_path)
    options = Options()
    prefs = {
        "profile.password_manager_enabled": False,
        "credentials_enable_service": False
    }
    #Disable Chrome Save Password popup
    options.add_experimental_option("prefs", prefs)
    #Remove the message on "Chome is being controlled by automated test software""
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    options.add_argument("--disable-blink-features=AutomationControlled")
    #Remove the Chrome notification popup
    options.add_argument("--disable-notifications")
    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()
    return driver


def login(driver):
    driver.get("https://staging.bharathexim.com/login")
    time.sleep(2)
    #handle the alert
    try:
        alert = driver.switch_to.alert
        alert.accept()
    except:
        pass
    time.sleep(2)


def enter_username(driver, username):
    email_input = driver.find_element(By.XPATH, "(//input[@placeholder='Enter email id'])[1]")
    email_input.clear()
    email_input.send_keys(username)


def enter_password(driver, password):
    password_input = driver.find_element(By.XPATH, "(//input[@placeholder='Enter password'])[1]")
    password_input.clear()
    password_input.send_keys(password)


def perform_login(driver):
    login_button = driver.find_element(By.XPATH, "(//button[normalize-space()='Login'])[1]")
    login_button.click()


def perform_otp(driver):
    totp_secret = "MZKFUOJYFE2FOQZG"  # Replace with actual secret
    totp = pyotp.TOTP(totp_secret)
    otp = totp.now()
    print("Generated OTP:", otp)
    time.sleep(3)
    otp_input = driver.find_element(By.XPATH, "(//input[@placeholder='Enter 6 digit Google Auth OTP'])[1]")
    otp_input.send_keys(otp)
    time.sleep(2)


def read_login_data(file_path):
    #Load the Excel file
    wb = openpyxl.load_workbook(file_path)
    #Get the active sheet and read the data
    sheet = wb.active
    #To store the empty data
    data = []
    # Read the data from the Excel sheet(skip header row)
    for row in sheet.iter_rows(min_row=2, values_only=True):  # Skip header
        data.append((row[0], row[1]))
        #return the list of login credentials
    return data


# Main Execution Block
if __name__ == "__main__":
    login_data = read_login_data("D:\\Python Practices\\Login_Data.xlsx")
    for username, password in login_data:
        print(f"\nLogging in with: {username}")
        driver = start_driver()
        login(driver)
        enter_username(driver, username)
        enter_password(driver, password)
        perform_login(driver)
        perform_otp(driver)
        perform_login(driver)
        time.sleep(5)
        driver.quit()
