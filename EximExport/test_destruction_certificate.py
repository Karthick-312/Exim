from Exim.EximExport.Config import *

def destructioncertificateupload(driver,file_path=r"D:\Testing Plan for Web Application.pdf"):
    #CLick the Insurance Policy menu
    safe_click(driver,"(//h6[normalize-space()='Destruction Certificate'])[1]")
    # CLick the add new button
    safe_click(driver,"(//button[normalize-space()='ADD NEW'])[1]")
    time.sleep(2)
    # select the dta in grid
    safe_click(driver, "(//input[@type='checkbox'])[3]")
    # File Upload
    force_click_with_actions(driver, "(//div[@class='dz-wrapper dropzone dz-multiple dz-clickable'])[1]", file_path)
    time.sleep(2)

def destructiondata(driver):
    #Click and enter the Destruction certificate number
    safe_click(driver,"(//input[@type='text'])[3]")
    safe_send_keys(driver,(By.XPATH,"(//input[@type='text'])[3]"),"345345")
    #CLick the submit button
    safe_click(driver,"(//button[@id='ExportDestructionCertificate'])[1]")
    # to print the message
    toast_message = get_toast_alert_text(driver)
    print("message:" + toast_message)

def test_pass(driver):
    output_path = r"D:\New Python\Recorded Videos\DestructionCertificate.mp4"
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
        destructioncertificateupload(driver, file_path=r"D:\New Python\samplePDFFile.pdf")
        destructiondata(driver)
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
    destructioncertificateupload(driver,file_path=r"D:\Downloads\2020_Taiwan_Tourism_Guide_Book_(E).pdf")
    longfilewarningmessage(driver)