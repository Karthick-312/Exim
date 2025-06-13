import time

from Exim.EximExport.Config import *

def Completedsummary(driver):
    #CLick the menu
    safe_click(driver,"(//a[normalize-space()='SB IRM Match Off'])[1]")
    #Click the veiw icon
    safe_click(driver,"(//p[@title='View'])[1]")
    #CLick the SI Details checkbox
    safe_click(driver,"(//span[@class='mat-checkbox-inner-container mat-checkbox-inner-container-no-side-margin'])[1]")
    #CLick the view crm details button
    safe_click(driver,"(//button[normalize-space()='View IRM Details'])[1]")
    #CLick the ok button in popup
    safe_click(driver,"(//span[normalize-space()='Ok'])[1]")

def Summarypendingoff(driver):
    #Click the summary pending off option
    safe_click(driver,"(//span[normalize-space()='Summary Pending Match Off'])[1]")
    time.sleep(1)
    #CLick & select the Match off option's in table
    safe_click(driver,"(//input[@class='ng-tns-c428-81 ng-valid ng-dirty ng-touched'])[1]")
    #Click & Select the CI details checkbox
    safe_click(driver,"(//span[@class='mat-checkbox-inner-container mat-checkbox-inner-container-no-side-margin'])[1]")
    #CLick the view CRM details button
    safe_click(driver,"(//button[normalize-space()='View IRM Details'])[1]")
    # CLick the ok button in popup
    safe_click(driver, "(//span[normalize-space()='Ok'])[1]")

def test_SB_IRM_match(driver):
    Completedsummary(driver)
    Summarypendingoff(driver)