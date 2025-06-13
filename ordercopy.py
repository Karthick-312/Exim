import pyautogui
import pytest
from LoginPage import *
from OrderCopyUpload import documents

@pytest.fixture

def driver():
    # provide the chrome driver path
    chrome_path = "D:\\New Python\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe"
    service = Service(chrome_path)
    options = Options()
    # Stops Chrome from asking, "Do you want to save this password?"
    prefs = {
        "profile.password_manager_enabled": False,
        "credentials_enable_service": False,
        "profile.default_content_setting_values.notifications": 2
    }
    options.add_experimental_option("prefs", prefs)
    # These settings remove banners like "Chrome is being controlled by automated test software"
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    #Disable the "Chrome Automation Extension," which is automatically installed when using appyflo.
    options.add_experimental_option('useAutomationExtension', False)
    #to hide from websites that you're using appyflo.
    options.add_argument("--disable-blink-features=AutomationControlled")
    #options.add_argument("--window-size=1400,3000")
    driver = webdriver.Chrome(service=service, options=options)
    driver.get("https://staging.bharathexim.com/login")
    # to maximize the windo
    driver.maximize_window()
    yield driver
    driver.quit()

def login(driver):
    username(driver)
    password(driver)
    perform_login(driver)
    perform_otp(driver)
    perform_login(driver)

#Pass a test case
def test_pass(driver):
    login(driver)
    time.sleep(45)
    documents(driver)
    # click the PI/PO order copy menu
    openordercopy = driver.find_element(By.XPATH, "(//h6[normalize-space()='PI / PO / Order Copy'])[1]")
    openordercopy.click()
    time.sleep(1)
    # Click add a new button
    addnew = driver.find_element(By.XPATH, "(//button[normalize-space()='ADD NEW'])[1]")
    addnew.click()
    time.sleep(1)
    upload = driver.find_element(By.XPATH, "(//div[@class='dz-wrapper dropzone dz-multiple dz-clickable'])[1]")
    upload.click()
    time.sleep(1)  # Wait for the file dialog to open
    pyautogui.write(r"D:\Testing Plan for Web Application.pdf")
    pyautogui.press('enter')
    time.sleep(2)

# Fail a test case
def test_fail(driver):
    login(driver)
    time.sleep(45)
    documents(driver)
    time.sleep(1)
    # click the PI/PO order copy menu
    openordercopy = driver.find_element(By.XPATH, "(//h6[normalize-space()='PI / PO / Order Copy'])[1]")
    openordercopy.click()
    time.sleep(1)
    # Click add a new button
    addnew = driver.find_element(By.XPATH, "(//button[normalize-space()='ADD NEW'])[1]")
    addnew.click()
    time.sleep(1)
    upload = driver.find_element(By.XPATH, "(//div[@class='dz-wrapper dropzone dz-multiple dz-clickable'])[1]")
    upload.click()
    time.sleep(1)  # Wait for the file dialog to open
    pyautogui.write(r"D:\Downloads\pkpadmin,+432-2321-1-CE.pdf")
    pyautogui.press('enter')
    error_message=driver.find_element(By.XPATH, "(//div[@aria-label='File is too big (25.13MiB). Max filesize: 5MiB.'])[1]")
    print("Validation Message:", error_message)

