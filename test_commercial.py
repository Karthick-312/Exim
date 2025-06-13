import pytest
from selenium.webdriver import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.login.login import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import subprocess

def upload_file_linux(driver, input_locator, file_path, timeout=20):
    # Wait for the file-input to be in the DOM
    file_input = WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located(input_locator)
    )
    # Un-hide it (if styled hidden by the dropzone)
    driver.execute_script(
        """
        arguments[0].style.display = 'block';
        arguments[0].style.visibility = 'visible';
        arguments[0].style.height = '1px';
        arguments[0].style.width = '1px';
        """,
        file_input
    )
    # Send the absolute path
    file_input.send_keys(file_path)
    return file_input

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
    # Hide the Selenium detection
    options.add_argument("--disable-blink-features=AutomationControlled")
    # Initialize the driver with options
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
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
    username(driver)
    password(driver)
    perform_login(driver)
    perform_otp(driver)
    perform_login(driver)


def wait_for_loader_to_disappear(driver, timeout=40):
    WebDriverWait(driver, timeout).until(
        EC.invisibility_of_element_located((By.CLASS_NAME, "loading-main"))
    )

def test_commercial_pass(driver):
    login(driver)
    document_element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "(//a[normalize-space()='Documents'])[1]"))
    )
    wait_for_loader_to_disappear(driver)
    document_element.click()
    invoice = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "(//h6[normalize-space()='Commercial Invoices'])[1]"))
    )
    wait_for_loader_to_disappear(driver)
    invoice.click()
    # click the add new button
    Add_Button = driver.find_element(By.XPATH, "(//button[@class='upload-button btn btn-success ng-star-inserted'])")
    wait_for_loader_to_disappear(driver)
    Add_Button.click()
    time.sleep(2)
    option = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable(
            (By.XPATH,
             "(//input[@type='checkbox'])[2]")
        )
    )
    wait_for_loader_to_disappear(driver)
    option.click()
    file_input_locator = (By.CSS_SELECTOR, "input[type='file']")
    upload_file_linux(driver, file_input_locator, "/home/sathish/Desktop/Aug.pdf")

    # Assert that the filename appears in the dropzone preview
    # uploaded_label = WebDriverWait(driver, 20).until(
    #     EC.visibility_of_element_located(
    #         (By.XPATH, "//div[contains(@class,'dz-filename')]/span[text()='Aug.pdf']")
    #     )
    # )
    #assert uploaded_label.is_displayed(), "File upload preview did not appear"
    time.sleep(10)

    # upload = driver.find_element(By.XPATH, "(//div[@class='dz-wrapper dropzone dz-multiple dz-clickable'])[1]")
    # wait_for_loader_to_disappear(driver)
    # upload.click()
    # time.sleep(2)  # Wait for the file dialog to open
    # pyautogui.write(r"/home/sathish/Desktop/Aug.pdf")
    # pyautogui.press('enter')
    commercial = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, "(//input[@class='form-control ng-untouched ng-pristine ng-valid'])[1]"))
    )
    wait_for_loader_to_disappear(driver)
    commercial.send_keys("50296605772")
    time.sleep(2)
    date = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "(//input[@class='form-control ng-untouched ng-pristine ng-valid'])[2]")))
    date.send_keys("08-08-2023")
    time.sleep(2)
    wait_for_loader_to_disappear(driver)
    amount = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "(//input[@type='textbox'])[1]"))
    )
    wait_for_loader_to_disappear(driver)
    amount.send_keys("1000")
    #time.sleep(2)
    dropdown = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "(//input[@type='text'])[4]")))
    dropdown.click()
    dropdown.send_keys("Advance Payment")
    dropdown.send_keys(Keys.ENTER)
    #time.sleep(20)
    submit = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "(//button[@id='ExportCommercialInvoices'])"))
    )
    submit.click()
    time.sleep(10)