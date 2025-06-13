from selenium.webdriver import Keys
from Exim.EximExport.Config import *

def BOEUpload(driver,file_path=r"D:\New Python\samplePDFFile.pdf"):
    # Click the Shipping Bill menu
    safe_click(driver, "(//h6[normalize-space()='BOE'])[1]")
    # CLick the add new button
    safe_click(driver, "(//button[normalize-space()='ADD NEW'])[1]")
    # Select the pi/po number
    safe_click(driver, "(//input[@type='checkbox'])[2]")
    # File Upload
    force_click_with_actions(driver, "(//div[@class='dz-wrapper dropzone dz-multiple dz-clickable'])[1]", file_path)
    time.sleep(3)

def BOEdata(driver):
    #Click the date picker
    safe_click(driver,"(//input[@type='date'])[3]")
    time.sleep(1)
    #Enter the date
    safe_send_keys(driver, (By.XPATH, "(//input[@type='date'])[3]"), "1004")
    actions = ActionChains(driver)
    actions.send_keys(Keys.TAB).perform()
    actions.send_keys("2025").perform()
    time.sleep(1)
    #click & enter the BOE no
    safe_click(driver,"(//input[@type='text'])[3]")
    safe_send_keys(driver,(By.XPATH,"((//input[@type='text'])[3]"),"BOE100")
    #Enter the BOE Amount
    safe_click(driver,"(//input[@type='textbox'])[1]")
    safe_send_keys(driver,(By.XPATH,"(//input[@type='textbox'])[1]"),"5000")
    #CLick and enter the port code
    safe_click(driver,"(//input[@type='text'])[4]")
    safe_send_keys(driver,(By.XPATH,"(//input[@type='text'])[4]"),"port")
    #CLick and enter the AWB no
    safe_click(driver,"(//input[@type='text'])[5]")
    safe_send_keys(driver,(By.XPATH,"(//input[@type='text'])[5]"),"SWA8474")
    #Click and enter the origin
    safe_click(driver,"(//input[@type='text'])[6]")
    safe_send_keys(driver,(By.XPATH,"(//input[@type='text'])[6]"),"Chennai")
    #Click and enter ethe portof loading
    safe_click(driver,"(//input[@type='text'])[7]")
    safe_send_keys(driver,(By.XPATH,"(//input[@type='text'])[7]"),"Delhi")
    #click and enter Adcode
    safe_click(driver,"(//input[@type='text'])[8]")
    safe_send_keys(driver,(By.XPATH,"(//input[@type='text'])[8]"),"AD8544")
    #Click and enter the freight value
    safe_click(driver,"(//input[@type='textbox'])[2]")
    safe_send_keys(driver,(By.XPATH,"(//input[@type='textbox'])[2]"),"500")
    #click and enter the miscellenous amount
    safe_click(driver,"(//input[@type='text'])[9]")
    safe_send_keys(driver,(By.XPATH,"(//input[@type='text'])[9]"),"2000")
    #CLick the TYpe dropdown
    safe_click(driver,"(//span[@class='ng-arrow-wrapper'])[1]")
    #Select the Type
    safe_click(driver,"(//span[normalize-space()='Direct Imports(Payment Against Bill of entry)'])[1]")


def test_pass(driver):
    BOEUpload(driver,r"D:\New Python\samplePDFFile.pdf")
    BOEdata(driver)

def test_fail(driver):
    BOEUpload(driver,r"D:\Downloads\2020_Taiwan_Tourism_Guide_Book_(E).pdf")
    longfilewarningmessage(driver)