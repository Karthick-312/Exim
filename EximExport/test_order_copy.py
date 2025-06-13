from selenium.webdriver import Keys
from Exim.EximExport.Config import *

def Ordercopyupload(driver,file_path=r"D:\Testing Plan for Web Application.pdf"):
    #CLick the Order Copy menu
    safe_click(driver,"(//h6[normalize-space()='PI / PO / Order Copy'])[1]")
    time.sleep(1)
    #Click the add new button
    safe_click(driver,"(//button[normalize-space()='ADD NEW'])[1]")
    time.sleep(1)
    force_click_with_actions(driver,"(//div[@class='dz-wrapper dropzone dz-multiple dz-clickable'])[1]",file_path)
    time.sleep(2)

def submitinvoice(driver):
    #select the option as proforma invoice
    safe_click(driver,"(//div[@class='checkbox-border'])[1]")
    '''# select the option as purchase order
    safe_click(driver,"(//div[@class='checkbox-border'])[2]")'''
    #Click the buyer name dropdown
    safe_click(driver,"(//span[@class='ng-arrow-wrapper'])[1]")
    #selct the buyername
    safe_click(driver,"(//span[normalize-space()='HUSCO INTERNATIONAL | OHMQ'])[1]")
    #Click the part no dropdown
    safe_click(driver,"(//span[@class='ng-arrow-wrapper'])[2]")
    #Select the part no
    safe_click(driver,"(//span[normalize-space()='HC6603-B10'])[1]")
    #CLick the HSN code & Enter the HSN Code
    safe_click(driver,"(//textarea[@class='form-control ng-untouched ng-pristine ng-valid'])[1]")
    safe_send_keys(driver,(By.XPATH,"(//textarea[@class='form-control ng-untouched ng-pristine ng-valid'])[1]"),"HSNCode")
    #Click the Pi/Po Number and enter the pi/po number
    safe_click(driver,"(//input[@type='text'])[4]")
    safe_send_keys(driver,(By.XPATH,"(//input[@type='text'])[4]"),"983220012")
    #Click the pi/po date
    safe_click(driver,"(//input[@type='date'])[1]")
    safe_send_keys(driver, (By.XPATH, "(//input[@type='date'])[1]"), "1004")
    actions = ActionChains(driver)
    actions.send_keys(Keys.TAB).perform()
    actions.send_keys("2025").perform()
    #Click the curreny dropdown
    safe_click(driver,"(//span[@class='ng-arrow-wrapper'])[3]")
    #Select the currency
    safe_click(driver,"(//span[normalize-space()='AFN'])[1]")
    #Enter the pi/po amount
    safe_click(driver,"(//input[@type='textbox'])[1]")
    safe_send_keys(driver,(By.XPATH,"(//input[@type='textbox'])[1]"),"1000")
    #select the goods
    safe_click(driver,"(//label[normalize-space()='Services'])[1]")
    '''#Click the consignee name dropdown
    safe_click(driver,"(//span[@class='ng-arrow-wrapper'])[4]")
    #select the consignee
    safe_click(driver,"(//span[@class='ng-option-label ng-star-inserted'])[1]")'''
    #Click the Remitter name dropdown
    safe_click(driver,"(//span[@class='ng-arrow-wrapper'])[5]")
    #Select the remitter name
    safe_click(driver,"(//span[@class='ng-option-label ng-star-inserted'])[1]")
    #Click the branch name dropdown
    safe_click(driver,"(//span[@class='ng-arrow-wrapper'])[7]")
    #Select the brach name
    safe_click(driver,"(//span[@class='ng-option-label ng-star-inserted'])[1]")
    #Click the QtyOrdered & Enter the QtyOrdered
    safe_click(driver,"(//input[@type='number'])[1]")
    safe_send_keys(driver,(By.XPATH,"(//input[@type='number'])[1]"),"1000")
    #Click the QtytoShip & enter the Qtytoship
    safe_click(driver,"(//input[@type='TextValiadtion'])[1]")
    safe_send_keys(driver,(By.XPATH,"(//input[@type='TextValiadtion'])[1]"),"500")
    #CLick the net price & enter the net price
    safe_click(driver,"(//input[@type='text'])[10]")
    safe_send_keys(driver,(By.XPATH,"(//input[@type='text'])[10]"),"1000")
    #Click the type dropdown
    safe_click(driver,"(//span[@class='ng-arrow-wrapper'])[8]")
    #Select the type
    safe_click(driver,"(//span[normalize-space()='Direct Dispatch'])[1]")
    #Selct the last date delivery
    safe_click(driver,"(//input[@type='date'])[2]")
    safe_send_keys(driver, (By.XPATH, "(//input[@type='date'])[2]"), "1004")
    actions = ActionChains(driver)
    actions.send_keys(Keys.TAB).perform()
    actions.send_keys("2025").perform()
    #Enter the amount
    safe_click(driver,"(//input[@type='textbox'])[2]")
    safe_send_keys(driver,(By.XPATH,"(//input[@type='textbox'])[2]"),"1000")
    #CLick the submit button
    safe_click(driver,"(//button[@id='PIPO_EXPORT'])[1]")
    time.sleep(5)
    #to print the message
    toast_message = get_toast_alert_text(driver)
    print("message:" + toast_message)

def test_pass(driver):
    output_path = r"D:\New Python\Recorded Videos\PIPOOrderCopy.mp4"
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
        Ordercopyupload(driver, file_path=r"D:\New Python\samplePDFFile.pdf")
        submitinvoice(driver)
    finally:
        stop_event.set()
        #Signals the recording thread to stop capturing by setting the event flag.The record_screen function’s loop checks this event and will exit cleanly.
        t.join(timeout=8)
        #Waits (blocks) for the recording thread t to finish.
        if t.is_alive():
            #Checks if the recording thread is still running (didn’t stop in time).
            print("⚠️ Recording thread did not stop in time.")
        else:
            print(f"✅ Screen recording saved to: {output_path}")
        try:
            driver.quit()
            #CLose the browser
            print("✅ Driver quit successfully.")
        except Exception as e:
            print(f"❌ Driver quit failed: {e}")


def test_fail(driver):
    Ordercopyupload(driver,file_path=r"D:\Downloads\pkpadmin,+432-2321-1-CE.pdf")
    longfilewarningmessage(driver)