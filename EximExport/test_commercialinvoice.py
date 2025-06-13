from selenium.webdriver import Keys
from Exim.EximExport.Config import *

def Commercialinvoiceupload(driver,file_path=r"D:\Testing Plan for Web Application.pdf"):
    #Click the Commercial Invoice menu
    safe_click(driver,"(//h6[normalize-space()='Commercial Invoices'])[1]")
    #CLick the add new button
    safe_click(driver,"(//button[normalize-space()='ADD NEW'])[1]")
    #Select the pi/po number
    safe_click(driver,"(//input[@type='checkbox'])[2]")
    #File Upload
    force_click_with_actions(driver,"(//div[@class='dz-wrapper dropzone dz-multiple dz-clickable'])[1]",file_path)
    time.sleep(3)

def Commercialinvoicedata(driver):
    #Enter the commercialinvoice number
    safe_click(driver,"(//input[@type='text'])[3]")
    safe_send_keys(driver,(By.XPATH,"(//input[@type='text'])[3]"),"73438833322")
    # Enter the Invoice date
    safe_click(driver,"(//input[@type='date'])[3]")
    safe_send_keys(driver, (By.XPATH, "(//input[@type='date'])[3]"), "1004")
    actions = ActionChains(driver)
    actions.send_keys(Keys.TAB).perform()
    actions.send_keys("2025").perform()
    #Enter the commercial invoice amount
    safe_click(driver,"(//input[@type='textbox'])[1]")
    safe_send_keys(driver,(By.XPATH,"(//input[@type='textbox'])[1]"),"1000")
    #CLick the type dropdown
    safe_click(driver,"(//span[@class='ng-arrow-wrapper'])[3]")
    #selct the type
    safe_click(driver,"(//span[normalize-space()='Direct Dispatch'])[1]")
    #Click the submit button
    safe_click(driver,"(//button[@id='ExportCommercialInvoices'])[1]")
    #to print the message
    toast_message = get_toast_alert_text(driver)
    print("message:" + toast_message)

def test_pass(driver):
    output_path = r"D:\New Python\Recorded Videos\CommercialInvoice.mp4"
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
        Commercialinvoiceupload(driver, r"D:\Testing Plan for Web Application.pdf")
        Commercialinvoicedata(driver)
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
    Commercialinvoiceupload(driver,r"D:\Downloads\pkpadmin,+1008-4741-1-CE (1).pdf")
    longfilewarningmessage(driver)