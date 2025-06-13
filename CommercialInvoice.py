

import pyautogui
import pytest
from OrderCopyUpload import documents

from LoginPage import *

# Fixture to initialize WebDriver
@pytest.fixture()
def driver():
    # Initialize ChromeOptions
    options = Options()

    # Setting preferences to disable password manager, notifications, etc.
    prefs = {
        "profile.password_manager_enabled": False,
        "credentials_enable_service": False,
        "profile.default_content_setting_values.notifications": 2
    }
    options.add_experimental_option("prefs", prefs)

    # Remove "Chrome is being controlled by automated test software" banner
    options.add_experimental_option("excludeSwitches", ["enable-automation"])

    # Disable the "Chrome Automation Extension"
    options.add_experimental_option('useAutomationExtension', False)

    # Hide the appyflo detection
    options.add_argument("--disable-blink-features=AutomationControlled")

    # Initialize the driver with options
    chrome_path = "D:\\New Python\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe"
    service = Service(chrome_path)
    driver = webdriver.Chrome(service=service, options=options)

    # Open the login page
    driver.get("https://staging.bharathexim.com/login")

    # Maximize the browser window
    driver.maximize_window()

    # Yield the driver to use it in the test
    yield driver

    # Quit the driver after the test is done
    driver.quit()

# Login function (assuming you have these methods defined)
def login(driver):
    username(driver)  # This function should set the username in the login form
    password(driver)  # This function should set the password in the login form
    perform_login(driver)  # This function performs the actual login
    perform_otp(driver)  # This function handles OTP, if applicable
    perform_login(driver)  # This might be a second login step
    time.sleep(35)
    documents(driver)


# Test to interact with Commercial Invoices

def test_commercial_pass(driver):
    login(driver)
    # click the invoice menu
    invoice = driver.find_element(By.XPATH, "(//h6[normalize-space()='Commercial Invoices'])[1]")
    invoice.click()
    # click the add new button
    Add_Button = driver.find_element(By.XPATH, "(//button[@class='upload-button btn btn-success ng-star-inserted'])")
    Add_Button.click()
    time.sleep(2)
    option = driver.find_element(By.XPATH, "(//input[@type='checkbox'])[2]")
    option.click()
    upload = driver.find_element(By.XPATH, "(//div[@class='dz-wrapper dropzone dz-multiple dz-clickable'])[1]")
    upload.click()
    time.sleep(2)  # Wait for the file dialog to open
    pyautogui.write(r"D:\Testing Plan for Web Application.pdf")
    pyautogui.press('enter')
    time.sleep(3)

def test_commercial_fail(driver):
    login(driver)
    # click the invoice menu
    invoice = driver.find_element(By.XPATH, "(//h6[normalize-space()='Commercial Invoices'])[1]")
    invoice.click()
    # click the add new button
    Add_Button = driver.find_element(By.XPATH, "(//button[@class='upload-button btn btn-success ng-star-inserted'])")
    Add_Button.click()
    time.sleep(2)
    option = driver.find_element(By.XPATH, "(//input[@type='checkbox'])[2]")
    option.click()
    upload = driver.find_element(By.XPATH, "(//div[@class='dz-wrapper dropzone dz-multiple dz-clickable'])[1]")
    upload.click()
    time.sleep(2)  # Wait for the file dialog to open
    pyautogui.write(r"D:\Downloads\2020_Taiwan_Tourism_Guide_Book_(E).pdf")
    pyautogui.press('enter')
    error_message=driver.find_element(By.XPATH, "(//div[@aria-label='File is too big (25.13MiB). Max filesize: 5MiB.'])[1]")
    print("Validation Message:", error_message)
    time.sleep(3)

