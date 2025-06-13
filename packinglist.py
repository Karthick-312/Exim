from Config import *

def test_pass(driver):
    login(driver)
    time.sleep(4)
    wait_for_loader_to_disappear(driver,timeout=45)
    documents(driver)
    #Click the Packing list menu
    safe_click(driver,"(//h6[normalize-space()='Packing List'])[1]")
    #Click the add new button
    safe_click(driver,"(//button[normalize-space()='ADD NEW'])[1]")
    wait_for_loader_to_disappear(driver,timeout=45)
    #Select the data in grid
    safe_click(driver,"(//input[@type='checkbox'])[2]")
    #click the upload button
    force_click_with_actions(driver, "(//div[@class='dz-wrapper dropzone dz-multiple dz-clickable'])[1]","D:\Testing Plan for Web Application.pdf")
    time.sleep(3)
    #click the bill entry dropdown
    safe_click(driver,"(//span[@class='ng-arrow-wrapper'])[1]")
    #Select the bill entry
    safe_click(driver,"(//span[@class='ng-option-label ng-star-inserted'])[1]")
    #Click the Packing list number
    safe_click(driver,"(//input[@type='text'])[4]")
    #enter the packing list number
    safe_send_keys(driver, (By.XPATH, "(//input[@type='text'])[4]"), "12343")
    #click the submit
    #safe_click(driver,"(//button[@id='Importpackinglist'])[1]")

def test_fail(driver):
    login(driver)
    time.sleep(4)
    wait_for_loader_to_disappear(driver, timeout=45)
    documents(driver)
    # Click the Packing list menu
    safe_click(driver, "(//h6[normalize-space()='Packing List'])[1]")
    # Click the add new button
    safe_click(driver, "(//button[normalize-space()='ADD NEW'])[1]")
    wait_for_loader_to_disappear(driver, timeout=45)
    # Select the data in grid
    safe_click(driver, "(//input[@type='checkbox'])[2]")
    # click the upload button
    force_click_with_actions(driver, "(//div[@class='dz-wrapper dropzone dz-multiple dz-clickable'])[1]",r"D:\Downloads\pkpadmin,+432-2321-1-CE.pdf")
    time.sleep(2)
    error_message = driver.find_element(By.XPATH,
                                        "(//div[@aria-label='File is too big (25.13MiB). Max filesize: 5MiB.'])[1]")
    print("Validation Message:", error_message)


