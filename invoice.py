import pyautogui
from LoginPage import *
from ordercopy import documents

def invoice(driver):
    #click the invoice menu
    invoice=driver.find_element(By.XPATH,"(//h6[normalize-space()='Commercial Invoices'])[1]")
    invoice.click()
    #click the add new button
    Add_Button =driver.find_element(By.XPATH, "(//button[@class='upload-button btn btn-success ng-star-inserted'])")
    Add_Button.click()
    time.sleep(2)
    option=driver.find_element(By.XPATH,"(//input[@type='checkbox'])[2]")
    option.click()
    upload = driver.find_element(By.XPATH, "(//div[@class='dz-wrapper dropzone dz-multiple dz-clickable'])[1]")
    upload.click()
    time.sleep(2)  # Wait for the file dialog to open
    pyautogui.write(r"D:\Testing Plan for Web Application.pdf")
    pyautogui.press('enter')
    time.sleep(3)

if __name__=="__main__":
    driver=start_driver()
    login(driver)
    username(driver)
    password(driver)
    perform_login(driver)
    perform_otp(driver)
    perform_login(driver)
    time.sleep(35)
    documents(driver)
    invoice(driver)
