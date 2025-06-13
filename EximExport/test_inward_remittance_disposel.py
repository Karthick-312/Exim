

from Exim.EximExport.Config import *

def SelectInwardremittance(driver):
    #CLick the menu
    safe_click(driver, "(//h6[normalize-space()='Inward Remittance Disposal'])[1]")
    #Select the inward remittance
    #checkbox_xpath = "//table//tr[4]//td[1]//input[@type='checkbox']"
    checkbox_xpath="//*[@id='content']/new-export-home-transaction/div/check-completed-all-process/custom-mat-stepper/div/custom-mat-step[1]/div/div/div/custom-expansion-panel/div/table/tbody/div/custom-table-expansion-panel/div[3]/tr/td[1]/label/input"
    # Wait for checkbox to be present
    checkbox = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, checkbox_xpath))
    )
    # Scroll into view
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", checkbox)
    time.sleep(1)  # Give time for animation to finish

    # Click using JavaScript to bypass overlays
    driver.execute_script("arguments[0].click();", checkbox)

def InwardRemittancedata(driver):
    # Click the next button
    safe_click(driver, "(//button[normalize-space()='Next'])[1]")
   #Click the group name dropdown
    safe_click(driver,"(//span[@class='ng-arrow-wrapper'])[1]")
   #Select the group name in dropdown
    safe_click(driver,"(//span[normalize-space()='Short Terms Loans'])[1]")
   #Click the Purpose code dropdown
    safe_click(driver,"(//span[@class='ng-arrow-wrapper'])[2]")
   #Select the purpose code
    safe_click(driver,"(//span[normalize-space()='P0103'])[1]")
   #Selct the description
    safe_click(driver,"(//input[@name='groupnamepurposecode'])[1]")
    #Select the group name in popup
    safe_click(driver,"(//input[@type='checkbox'])[2]")
    #Click the select button in popup
    safe_click(driver,"(//span[normalize-space()='Select'])[1]")
    #Click the next button
    safe_click(driver,"(//button[normalize-space()='Next'])[1]")
    #Click the select bank dropdown
    safe_click(driver,"(//input[@id='myDropdown'])[1]")
    #Select the bank in dropdown
    safe_click(driver,"(//li[@class='li-dropdown ng-star-inserted'])[1]")
    #Click th To debit charges Acc.no & Acc type
    safe_click(driver,"(//span[@class='mat-checkbox-inner-container'])[1]")
    #Click th To credit charges Acc.no & Acc type
    safe_click(driver,"(//span[@class='mat-checkbox-inner-container'])[2]")
    #CLick the next button
    safe_click(driver,"(//button[normalize-space()='Next'])[1]")

def SelectForwardContract(driver):
    # Select the forward contract
    checkbox_xpath = "//table//tr[1]//td[1]//input[@type='checkbox']"
    # Wait for checkbox to be present
    checkbox = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, checkbox_xpath))
    )
    # Scroll into view
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", checkbox)
    time.sleep(1)  # Give time for animation to finish

    # Click using JavaScript to bypass overlays
    driver.execute_script("arguments[0].click();", checkbox)
     #Click the next button
    safe_click(driver,"(//button[normalize-space()='Next'])[1]")

def FillForwardContract(driver):
    #Clic the next button
    safe_click(driver,"(//button[normalize-space()='Next'])[1]")
    #CLick the PIPO number dropdown
    safe_click(driver,"(//span[@class='ng-arrow-wrapper'])[1]")
    #Select the PIPO Number
    safe_click(driver,"(//span[@class='ng-option-label ng-star-inserted'])[1]")
    #Click the cehck box in PIPO number grid
    safe_click(driver,"(//input[@class='checkBox-purpose-code'])[1]")
    #Click the next button
    safe_click(driver,"(//button[normalize-space()='Next'])[1]")





def test_pass(driver):
    SelectInwardremittance(driver)
    InwardRemittancedata(driver)
    SelectForwardContract(driver)
    FillForwardContract(driver)