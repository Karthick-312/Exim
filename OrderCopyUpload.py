
import pyautogui
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from LoginPage import *

def documents(driver):
    # Click the documents expand
    documents=driver.find_element(By.XPATH, "(//a[normalize-space()='Documents'])[1]")
    documents.click()

def ordercopy(driver):
    #click the PI/PO order copy menu
    openordercopy=driver.find_element(By.XPATH,"(//h6[normalize-space()='PI / PO / Order Copy'])[1]")
    openordercopy.click()
    time.sleep(2)
    #Click add a new button
    addnew=driver.find_element(By.XPATH,"(//button[normalize-space()='ADD NEW'])[1]")
    addnew.click()
    time.sleep(2)
    upload= driver.find_element(By.XPATH, "(//div[@class='dz-wrapper dropzone dz-multiple dz-clickable'])[1]")
    upload.click()
    time.sleep(2)  # Wait for the file dialog to open
    pyautogui.write(r"D:\Testing Plan for Web Application.pdf")
    pyautogui.press('enter')
    time.sleep(3)

def submitinvoice():
    #Proforma invoice
    selecttype=driver.find_element(By.XPATH,"(//div[@class='checkbox-border'])[1]")
    selecttype.click()
    '''    #Purchase order
        selecttype=driver.find_element(By.XPATH,"(//div[@class='checkbox-border'])[2]")
        selecttype.click()'''
    #click the buyername dropdown
    buyernamedrodown = driver.find_element(By.XPATH, "(//span[@class='ng-arrow-wrapper'])[1]")
    buyernamedrodown.click()
    time.sleep(2)
    #select buyername --- IKEA,STPI,Tom & Jery,Iberica Export,EKOTERRA FOOD SRL
    selectbuyername=driver.find_element(By.XPATH,"(//span[normalize-space()='STPI | undefined'])[1]")
    selectbuyername.click()
    #click the part no dropdown
    partnodropdown=driver.find_element(By.XPATH,"(//span[@class='ng-arrow-wrapper'])[2]")
    partnodropdown.click()
    #select the part no
    selectpartno=driver.find_element(By.XPATH,"(//span[normalize-space()='2154456'])[1]")
    selectpartno.click()
    #Enter the HSN Code Desrciption
    HSNCodeDescription=driver.find_element(By.XPATH,"(//textarea[@class='form-control ng-untouched ng-pristine ng-valid'])[1]")
    HSNCodeDescription.send_keys("HSNCode")
    #Enter the PI/PO Number
    PIPoNumber=driver.find_element(By.XPATH,"(//input[@type='text'])[4]")
    PIPoNumber.send_keys("234343")
    #select the PI/Po date
    clickdatepicker=driver.find_element(By.XPATH,"(//input[@type='date'])[1]")
    clickdatepicker.click()
    time.sleep(1)
    actions=ActionChains(driver)
    actions.send_keys("1205")
    actions.send_keys(Keys.TAB).perform()
    actions.send_keys("2025").perform()
    time.sleep(1)
    #click the currency droddown
    currency=driver.find_element(By.XPATH,"(//span[@class='ng-arrow-wrapper'])[3]")
    currency.click()
    time.sleep(1)
    #to scroll
    scroll=driver.find_element(By.XPATH,"(//div[@class='ng-dropdown-panel-items scroll-host'])[1]")
    origin = ScrollOrigin.from_element(scroll)
    actions = ActionChains(driver)
    actions.scroll_from_origin(origin, 0, 300).perform()
    selectcurrency=driver.find_element(By.XPATH,"(//span[normalize-space()='ARS'])[1]")
    selectcurrency.click()
    time.sleep(1)
    #enter the PI/PO amount
    amount=driver.find_element(By.XPATH,"(//input[@type='textbox'])[1]")
    driver.execute_script("arguments[0].scrollIntoView();", amount)
    amount.send_keys("1000")
    time.sleep(1)
    #seelct the goods
    goods=driver.find_element(By.XPATH,"(//label[normalize-space()='Services'])[1]")
    driver.execute_script("arguments[0].scrollIntoView();", goods)
    goods.click()
    time.sleep(1)
    #consignee name
    consigneename=driver.find_element(By.XPATH,"(//span[@class='ng-arrow-wrapper'])[4]")
    driver.execute_script("arguments[0].scrollIntoView();", consigneename)
    consigneename.click()
    time.sleep(1)
    selectconsigneename=driver.find_element(By.XPATH,"(//span[@class='ng-option-label ng-star-inserted'])[1]")
    selectconsigneename.click()
    #Select the remitter name
    remitter=driver.find_element(By.XPATH,"(//span[@class='ng-arrow-wrapper'])[5]")
    remitter.click()
    time.sleep(1)
    selectremitter=driver.find_element(By.XPATH,"(//span[@class='ng-option-label ng-star-inserted'])[1]")
    selectremitter.click()
    time.sleep(1)
    '''#select the incoterm
    incoterm=driver.find_element(By.XPATH,"(//span[@class='ng-arrow-wrapper'])[6]")
    incoterm.click()
    time.sleep(1)
    selectincoterm=driver.find_element(By.XPATH,"(//span[normalize-space()='FOB | Free on Board'])[1]")
    selectincoterm.click()'''
    #Select the branch
    branch=driver.find_element(By.XPATH,"(//span[@class='ng-arrow-wrapper'])[7]")
    branch.click()
    time.sleep(1)
    selectbranch=driver.find_element(By.XPATH,"(//span[normalize-space()='CHENNAI'])[1]")
    selectbranch.click()
    time.sleep(1)
    #Qtyordered
    Qtyordered=driver.find_element(By.XPATH,"(//input[@type='number'])[1]")
    Qtyordered.send_keys("10")
    time.sleep(1)
    #Qty to ship
    Qtytoship=driver.find_element(By.XPATH,"(//input[@type='number'])[2]")
    Qtytoship.send_keys("10")
    time.sleep(1)
    #Net price
    Netprice=driver.find_element(By.XPATH,"(//input[@type='text'])[10]")
    driver.execute_script("arguments[0].scrollIntoView();", Netprice)
    Netprice.send_keys("1000")
    time.sleep(1)
    #Payment terms (type)
    Type=driver.find_element(By.XPATH,"(//span[@class='ng-arrow-wrapper'])[8]")
    Type.click()
    time.sleep(1)
    selecttype=driver.find_element(By.XPATH,"(//span[normalize-space()='Direct Dispatch'])[1]")
    selecttype.click()
    time.sleep(1)
    #select the last day of shipment
    Lastdayofshipment=driver.find_element(By.XPATH,"(//input[@type='date'])[2]")
    Lastdayofshipment.click()
    time.sleep(1)
    actions = ActionChains(driver)
    actions.send_keys("1205")
    actions.send_keys(Keys.TAB).perform()
    actions.send_keys("2025").perform()
    time.sleep(1)
    #Amount
    Amount=driver.find_element(By.XPATH,"(//input[@type='textbox'])[2]")
    Amount.send_keys("1000")
    time.sleep(1)
    #submit the order
    submit=driver.find_element(By.XPATH,"(//button[@id='PIPO_EXPORT'])[1]")
    submit.click()
    time.sleep(2)

if __name__ == "__main__":
    driver = start_driver()
    # Execute the steps
    login(driver)
    username(driver)
    password(driver)
    perform_login(driver)
    perform_otp(driver)
    perform_login(driver)
    time.sleep(50)
    documents(driver)
    time.sleep(2)
    ordercopy(driver)
    submitinvoice()

