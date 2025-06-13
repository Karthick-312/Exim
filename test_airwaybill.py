import pytest
from src.login.login import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
def wait_for_loader_to_disappear(driver, timeout=45):
    WebDriverWait(driver, timeout).until(
        EC.invisibility_of_element_located((By.CLASS_NAME, "loading-main"))
    )


def test_Airwaybillcopy_pass(driver):
    login(driver)
    wait_for_loader_to_disappear(driver)
    document_element = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "(//a[normalize-space()='Documents'])[1]"))
    )
    wait_for_loader_to_disappear(driver)
    document_element.click()
#Click Airwaybillcopy
    Airwaybillcopy = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "(//h6[@class='nav-link p-0'])[4]"))
    )
    wait_for_loader_to_disappear(driver)
    Airwaybillcopy.click()
#Click View icon
    view = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "(//a[@popup-close='PDF_VIEW'])[1]"))
    )
    wait_for_loader_to_disappear(driver)
    view.click()
 #Click Download icon
    download = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, "(//div[@class='pdfv-control ng-star-inserted'])[1]"))
    )
    wait_for_loader_to_disappear(driver)
    download.click()
#Click Close the download button
    close = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "(//app-custom-model[@id='PDF_VIEW']//div[@class='modal-header']//button[2]//*[name()='svg']//*[name()='path' and contains(@class,'ng-star-in')]"))
    )
    wait_for_loader_to_disappear(driver)
    close.click()
    time.sleep(10)
#Click Edit Icon
    Edit = (WebDriverWait(driver, 21).until
            (EC.element_to_be_clickable((By.XPATH, "(//i[contains(@class, 'fa-pencil-square-o') and contains(@popup-close, 'EditSummaryPage')])[1]")))
            )
    wait_for_loader_to_disappear(driver)
    Edit.click()
    wait_for_loader_to_disappear(driver)
    #time.sleep(10)
#Update
    Update = (WebDriverWait(driver, 21).until(EC.element_to_be_clickable((By.XPATH, "(//button[@class='btn btn-primary submit-button ng-star-inserted'])[1]"))))
    wait_for_loader_to_disappear(driver)
    Update.click()
    wait_for_loader_to_disappear(driver)

    # click the add new button
    Add_Button = driver.find_element(By.XPATH, "(//button[@class='upload-button btn btn-success ng-star-inserted'])")
    wait_for_loader_to_disappear(driver)
    Add_Button.click()
    time.sleep(2)