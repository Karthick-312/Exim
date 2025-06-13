from selenium.webdriver import Keys
from Exim.EximExport.Config import *

def Shippingbillupload(driver,file_path=r"D:\New Python\samplePDFFile.pdf"):
    # Click the Shipping Bill menu
    safe_click(driver, "(//h6[normalize-space()='Shipping Bill'])[1]")
    # CLick the add new button
    safe_click(driver, "(//button[normalize-space()='ADD NEW'])[1]")
    # Select the pi/po number
    safe_click(driver, "(//input[@type='checkbox'])[2]")
    # File Upload
    force_click_with_actions(driver, "(//div[@class='dz-wrapper dropzone dz-multiple dz-clickable'])[1]", file_path)
    time.sleep(3)

def Shippingbilldata(driver):
    #click the sb date
    safe_click(driver,"(//input[@type='date'])[3]")
    safe_send_keys(driver, (By.XPATH, "(//input[@type='date'])[3]"), "1004")
    actions = ActionChains(driver)
    actions.send_keys(Keys.TAB).perform()
    actions.send_keys("2025").perform()
    # click the Sb no
    safe_click(driver, "(//input[@type='text'])[3]")
    # Enter the Sbno
    safe_send_keys(driver, (By.XPATH, "(//input[@type='text'])[3]"), "7176113992")
    # Enter the Adcode
    safe_click(driver, "(//input[@type='text'])[4]")
    safe_send_keys(driver, (By.XPATH, "(//input[@type='text'])[4]"), "402966071")
    time.sleep(1)
    # Click the consignee dropdown
    safe_click(driver, "(//input[@type='text'])[6]")
    time.sleep(1)
    # select the consignee
    safe_click(driver, "(//span[normalize-space()='HUSCO INTERNATIONAL'])[2]")
    time.sleep(1)
    # click the Country of final destination
    safe_click(driver, "(//input[@type='text'])[7]")
    # Enter the country of final destination
    safe_send_keys(driver, (By.XPATH, "(//input[@type='text'])[7]"), "Chennai")
    time.sleep(1)
    # Click the Explorator code
    safe_click(driver, "(//input[@type='text'])[8]")
    # Enter the Explorator code
    safe_send_keys(driver, (By.XPATH, "(//input[@type='text'])[8]"), "Delhi")
    time.sleep(1)
    # Click the SB Value
    safe_click(driver, "(//input[@type='textbox'])[1]")
    # Enter the Sb value
    safe_send_keys(driver, (By.XPATH, "(//input[@type='textbox'])[1]"), "1000")
    time.sleep(1)
    # Click the freight value
    safe_click(driver, "(//input[@type='textbox'])[2]")
    # enter the frieght value
    safe_send_keys(driver, (By.XPATH, "(//input[@type='textbox'])[2]"), "100")
    time.sleep(1)
    # IEC name
    safe_click(driver, "(//input[@type='text'])[10]")
    # Enter the IEC Name
    safe_send_keys(driver, (By.XPATH, "(//input[@type='text'])[10]"), "0")
    time.sleep(1)
    # Click the IEC code
    safe_click(driver, "(//input[@type='text'])[11]")
    # enter the IEC code
    safe_send_keys(driver, (By.XPATH, "(//input[@type='text'])[11]"), "12345S")
    time.sleep(1)
    # Click the insurance value
    safe_click(driver, "(//input[@type='textbox'])[3]")
    # Enter the insurance value
    safe_send_keys(driver, (By.XPATH, "(//input[@type='textbox'])[3]"), "0")
    time.sleep(1)
    # Click the LEO date
    safe_click(driver, "(//input[@type='date'])[4]")
    safe_send_keys(driver, (By.XPATH, "(//input[@type='date'])[4]"), "1004")
    actions = ActionChains(driver)
    actions.send_keys(Keys.TAB).perform()
    actions.send_keys("2025").perform()
    time.sleep(1)
    #Click and enetr the port code
    safe_click(driver,"(//input[@type='text'])[12]")
    safe_send_keys(driver,(By.XPATH,"(//input[@type='text'])[12]"),"INMAA4")
    # Click the invoice dropdown
    safe_click(driver, "(//span[@class='ng-arrow-wrapper'])[3]")
    time.sleep(1)
    # select the invoices
    safe_click(driver, "(//span[@class='ng-option-label ng-star-inserted'])[1]")
    time.sleep(1)
    '''# click the type
    safe_click(driver, "(//input[@type='text'])[14]")
    time.sleep(1)
    # select the type
    safe_click(driver, "(//span[normalize-space()='Direct Dispatch'])[1]")
    time.sleep(1)'''
    #submit the data
    safe_click(driver,"(//button[@id='ShippingBill'])[1]")
    time.sleep(2)
    #to print the message
    toast_message = get_toast_alert_text(driver)
    print("message:" + toast_message)


def test_pass(driver):
    output_path = r"D:\New Python\Recorded Videos\ShippingBill.mp4"
    # Sets the file path where the screen recording video will be saved.
    stop_event = Event()
    # Creates a threading.Event object called stop_event.
    t = Thread(target=record_screen, args=(output_path, stop_event))
    # Creates a new thread t:
    #                       The thread will run the record_screen function.
    #                       Passes the arguments (output_path, stop_event) to that function.
    t.start()
    # Starts the screen recording thread
    # The screen is now being recordedin the background
    try:
        Shippingbillupload(driver, file_path=r"D:\New Python\samplePDFFile.pdf")
        Shippingbilldata(driver)
    finally:
        stop_event.set()
        # Signals the recording thread to stop capturing by setting the event flag.The record_screen function’s loop checks this event and will exit cleanly.
        t.join(timeout=8)
        # Waits (blocks) for the recording thread t to finish.
        if t.is_alive():
            # Checks if the recording thread is still running (didn’t stop in time).
            print("⚠️ Recording thread did not stop in time.")
        else:
            print(f"✅ Screen recording saved to: {output_path}")
        try:
            driver.quit()
            # CLose the browser
            print("✅ Driver quit successfully.")
        except Exception as e:
            print(f"❌ Driver quit failed: {e}")


def test_fail(driver):
    Shippingbillupload(driver,file_path=r"D:\Downloads\pkpadmin,+1008-4741-1-CE (2).pdf")
    longfilewarningmessage(driver)