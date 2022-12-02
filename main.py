import time

from selenium import webdriver

from time import sleep
from selenium.webdriver.chrome.webdriver import WebDriver
#First test case

def logged_in_successfully():

    driver: WebDriver = webdriver.Chrome()
    driver.get("https://opensource-demo.orangehrmlive.com")
    driver.maximize_window()
    time.sleep(3)
            # To enter user name and password
    driver.find_element(By.NAME,'username').send_keys('Admin')
    driver.find_element(By.NAME,'password').send_keys("admin123")
            # To click on login button
    driver.find_element(By.XPATH,"//button[text()=' Login ']").click()
            #  Expected result A user is successfully login
    print("The user is logged in successfully")

#Second test case

def invalid_crendentials():
    driver= webdriver.Chrome()
    driver.get("https://opensource-demo.orangehrmlive.com")
    time.sleep(5)
    driver.maximize_window()
 # To enter user name and password
    driver.find_element(By.NAME,'username').send_keys('Admin')
    driver.find_element(By.NAME,'password').send_keys("invalid password")
# To click on login button
    l= driver.find_element(By.XPATH,"//button[text()=' Login ']")
    l.click()
    time.sleep(5)
# A valid error message for invalid credentials
    print("A valid error message for invalid credentials is displayed")

#Test Cases dealing the with PIM
#Test cases 1
def Add_empolee_in_PIM():

    driver= webdriver.Chrome()
    driver.get("https://opensource-demo.orangehrmlive.com")
    time.sleep(5)
    driver.maximize_window()
 # For user login
    driver.find_element(By.NAME,'username').send_keys('Admin')
    driver.find_element(By.NAME,'password').send_keys("admin123")
    l= driver.find_element(By.XPATH,"//button[@type='submit']")
    l.click()
    time.sleep(5)
 # To click on PIM
    m= driver.find_element(By.LINK_TEXT,'PIM')
    m.click()
    time.sleep(5)
 # To click on AddEmployee and flill the employee details

    a=driver.find_element(By.LINK_TEXT, 'Add Employee')
    a.click()
    time.sleep(2)
    driver.find_element(By.NAME,'firstName').send_keys('Sandy')
    time.sleep(2)
    driver.find_element(By.NAME,'lastName').send_keys('S')
 # To click on save
    o= driver.find_element(By.XPATH,"//button[@type='submit']")
    o.click()
# PIM and should see a message for successful employee addition
    print("The user should be able to add a new employee in the PIM and should see a message for successful employee addition")

#Test case2
def edit_existing_empoyee():

    driver= webdriver.Chrome()
    driver.get("https://opensource-demo.orangehrmlive.com")
    time.sleep(5)
    driver.maximize_window()
#for user login
    driver.find_element(By.NAME,'username').send_keys('Admin')
    driver.find_element(By.NAME,'password').send_keys("admin123")
    l= driver.find_element(By.XPATH,"//button[@type='submit']")
    l.click()
    time.sleep(3)
# TO enter in PIM
    b= driver.find_element(By.LINK_TEXT,'PIM')
    b.click()
    time.sleep(2)
# Click Employee list
    a= driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[2]')
    a.click()
    time.sleep(2)
    driver.find_element(By.NAME,'firstName').send_keys('Jenny')
    driver.find_element(By.NAME,'lastName').send_keys('S')
 # click to save
    m = driver.find_element(By.XPATH, "//button[@type='submit']")
    m.click()
# Expected result
    print('The user should be able to edit an existing employee information in the PIM and should see a message for successful employee details addition')

#Test case3
def delete_an_existing_employee():

    driver= webdriver.Chrome()
    driver.get("https://opensource-demo.orangehrmlive.com")
    time.sleep(5)
    driver.maximize_window()
# login page
    driver.find_element(By.NAME,'username').send_keys('Admin')
    driver.find_element(By.NAME,'password').send_keys("admin123")
    a= driver.find_element(By.XPATH,"//button[@type='submit']")
    a.click()
    time.sleep(3)
#into pim pane
    m= driver.find_element(By.LINK_TEXT,'PIM')
    m.click()
    time.sleep(2)
# To delete an existing employee
    p= driver.find_element(By.XPATH,"//[@class='oxd-icon-button oxd-table-cell-action-space']")
    p.click()
# confirmation to delete an existing employee
    q=driver.find_element(By.XPATH,"//*[@id='app']/div[3]/div/div/div/div[3]/button[2]")
    q.click()

    print('The user should be able to delete an existing employee information in the PIM and should see a message for successful deletion')
