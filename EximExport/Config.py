import pyautogui
import pytest
from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from Exim.LoginPage import *


def wait_for_loader_to_disappear(driver, timeout=45):
    try:
        WebDriverWait(driver, timeout).until(
            EC.invisibility_of_element_located((By.CLASS_NAME, "loading-overlay visible"))
        )
        WebDriverWait(driver, timeout).until(
            EC.invisibility_of_element_located((By.CLASS_NAME, "loading-overlay"))
        )
        WebDriverWait(driver, timeout).until(
            EC.invisibility_of_element_located((By.CLASS_NAME, "loading-main"))
        )
        WebDriverWait(driver, timeout).until(
            EC.invisibility_of_element_located((By.CLASS_NAME, "loader"))
        )
    except TimeoutException:
        print("[Timeout] Loader did not disappear within time")


def safe_click(driver, xpath, timeout=45):
    try:
        wait_for_loader_to_disappear(driver)
        element = WebDriverWait(driver, timeout).until(
            EC.element_to_be_clickable((By.XPATH, xpath))
        )
        element.click()
        wait_for_loader_to_disappear(driver)
    except TimeoutException:
        print(f"[Timeout] Element {xpath} not clickable after {timeout}s")
    except Exception as e:
        print(f"[Error] Clicking {xpath}: {str(e)}")


def safe_send_keys(driver, xpath, value, timeout=45):
    try:
        wait_for_loader_to_disappear(driver)
        element = WebDriverWait(driver, timeout).until(
            EC.visibility_of_element_located(xpath)
        )
        element.clear()
        element.send_keys(value)
        wait_for_loader_to_disappear(driver)
    except TimeoutException:
        print(f"[Timeout] Could not send keys to {xpath}")
    except Exception as e:
        print(f"[Error] send_keys on {xpath}: {str(e)}")


def force_click_with_actions(driver, xpath, filepath=r"D:\Testing Plan for Web Application.pdf"):
    try:
        #waits untill the loader
        wait_for_loader_to_disappear(driver)
        time.sleep(2)
        element = driver.find_element(By.XPATH, xpath)
        #scroll into viewto find the element
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        #using mouse actions to perform the file upload
        ActionChains(driver).move_to_element(element).click().perform()
        time.sleep(1)
        pyautogui.write(filepath)
        pyautogui.press('enter')
    except Exception as e:
        print(f"[Error] Force click failed: {e}")


def importoption(driver):
    wait_for_loader_to_disappear(driver, timeout=45)
    safe_click(driver, "(//div[@class='dot'])[1]")


@pytest.fixture(scope="session")
def driver():
    # provide the chrome driver path
    #chrome_path = "D:\New Python\chromedriver-win64\chromedriver-win64\chromedriver.exe"
    #service = Service(chrome_path)
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
    #Disable the "Chrome Automation Extension," which is automatically installed when using
    options.add_experimental_option('useAutomationExtension', False)
    #to hide from websites that you're using appyflo.
    options.add_argument("--disable-blink-features=AutomationControlled")
    #options.add_argument("--window-size=1400,3000")
    driver = webdriver.Chrome(options=options)
    driver.get("https://staging.bharathexim.com/login")
    # to maximize the window
    driver.maximize_window()
    login(driver)
    #importoption(driver)
    documents(driver)
    #transactions(driver)
    yield driver
    driver.quit()


def login(driver):
    username(driver)
    password(driver)
    perform_login(driver)
    perform_otp(driver)
    perform_login(driver)
    time.sleep(2)


def documents(driver):
    safe_click(driver, "(//a[normalize-space()='Documents'])[1]")

def transactions(driver):
    safe_click(driver,"(//a[normalize-space()='Transactions'])[1]")

def longfilewarningmessage(driver):
    error_message = driver.find_element(By.XPATH,
                                        "(//div[@aria-label='File is too big (25.13MiB). Max filesize: 5MiB.'])[1]")
    print("Validation Message:", error_message)


def view(driver):
    safe_click(driver, "(//i[@class='fa fa-eye PopupOpen view-icon ng-tns-c428-69'])[1]")


def edit(driver):
    safe_click(driver, "(//i[@class='fa fa-pencil-square-o PopupOpen edit-icon ng-tns-c428-69'])[1]")


def get_toast_alert_text(driver):
    try:
        # Wait for the toast message to be visible (max 10 seconds)
        toast = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'toast') or contains(text(),'Successfully')]"))
        )
        print("Toast message:", toast.text)
        return toast.text
    except:
        print("Toast message not found")
        return None