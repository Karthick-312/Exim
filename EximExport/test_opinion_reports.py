from selenium.webdriver import Keys

from Exim.EximExport.Config import *

def opinionreportupload(driver,file_path=r"D:\Testing Plan for Web Application.pdf"):
    #CLick the Insurance Policy menu
    safe_click(driver,"(//h6[normalize-space()='Opinion Reports'])[1]")
    # CLick the add new button
    safe_click(driver,"(//button[normalize-space()='ADD NEW'])[1]")
    time.sleep(2)
    # select the dta in grid
    safe_click(driver, "(//input[@type='checkbox'])[2]")
    # File Upload
    force_click_with_actions(driver, "(//div[@class='dz-wrapper dropzone dz-multiple dz-clickable'])[1]", file_path)
    time.sleep(2)

def opinionreportdata(driver):
    #Click and enter the opinion report number
    safe_click(driver,"(//input[@type='text'])[3]")
    safe_send_keys(driver,(By.XPATH,"(//input[@type='text'])[3]"),"345556")
    #Select the opinion report date
    safe_click(driver,"(//input[@type='date'])[3]")
    safe_send_keys(driver, (By.XPATH, "(//input[@type='date'])[3]"), "3112")
    actions = ActionChains(driver)
    actions.send_keys(Keys.TAB).perform()
    actions.send_keys("2024").perform()
    #CLick & Enter the Foreign party name
    safe_click(driver,"(//input[@type='text'])[4]")
    safe_send_keys(driver,(By.XPATH,"(//input[@type='text'])[4]"),"HUSCO INTERNATIONAL | OHMQ"+ Keys.ENTER)
    #Select the Report date
    safe_click(driver,"(//input[@type='date'])[4]")
    safe_send_keys(driver, (By.XPATH, "(//input[@type='date'])[4]"), "1201")
    actions = ActionChains(driver)
    actions.send_keys(Keys.TAB).perform()
    actions.send_keys("2025").perform()
    #Click and enter the reposrt ratings
    safe_click(driver,"(//input[@type='text'])[5]")
    safe_send_keys(driver,(By.XPATH,"(//input[@type='text'])[5]"),"Accepted")
    #Click the submit button
    safe_click(driver,"(//button[@id='ExportOpomopnReport'])[1]")
    # to print the message
    toast_message = get_toast_alert_text(driver)
    print("message:" + toast_message)

def test_pass(driver):
    output_path = r"D:\New Python\Recorded Videos\OpinionReports.mp4"
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
        opinionreportupload(driver, file_path=r"D:\New Python\samplePDFFile.pdf")
        opinionreportdata(driver)
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
    opinionreportupload(driver,file_path=r"D:\Downloads\2020_Taiwan_Tourism_Guide_Book_(E).pdf")
    longfilewarningmessage(driver)
