from Exim.EximExport.Config import *

def Declarationselect(driver):
    #Click the declartion menu
    safe_click(driver,"(//h6[normalize-space()='Declaration/Annexure'])[1]")
    #CLick the add new button
    safe_click(driver,"(//button[normalize-space()='ADD NEW'])[1]")
    #Click the declaration/annexue2
    safe_click(driver,"(//button[normalize-space()='Declaration/Annex2'])[1]")
    #CLick the select buyer name
    safe_click(driver,"(//button[normalize-space()='Select Buyer'])[1]")
    #Click the Select buyer name dropdown
    safe_click(driver,"(//span[@class='ng-arrow-wrapper'])[1]")
    #Select the buyername
    safe_click(driver,"(//span[normalize-space()='HUSCO INERNATIONAL | OHRU'])[1]")
    #Click the Select ci
    safe_click(driver,"(//button[normalize-space()='SELECT CI'])[1]")
    #Select the Ci Summary
    safe_click(driver,"(//input[@type='checkbox'])[2622]")
    #Click the Select
    safe_click(driver,"(//button[normalize-space()='Select'])[1]")
    '''#Click the save button
    safe_click(driver,"(//button[normalize-space()='Save'])[1]")
    #to print the message
    toast_message = get_toast_alert_text(driver)
    print("message:" + toast_message)'''

def declarationsummarypageoptions(driver):
    #Click the add enw button
    safe_click(driver,"(//button[normalize-space()='ADD NEW'])[1]")
    #Click the Without Indent option
    safe_click(driver,"(//span[@class='mat-checkbox-inner-container'])[2]")
    #Click the Generate invoice button
    safe_click(driver,"(//button[normalize-space()='Generate Invoice'])[1]")
    #Click the Generate packing list button
    safe_click(driver,"(//button[normalize-space()='Generate Packing List'])[1]")


def test_pass(driver):
    output_path = r"D:\New Python\Recorded Videos\Declaration(or)Annexure.mp4"
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
        Declarationselect(driver)
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
