#This the very first program I created, trimmed to be edited for any usecase. 
#The main function is to repeatedly fill out 2 webforms on a timer.
#A bit messy, but you'd be surprised how much cleaner it is from the original version.
#chevrons<> and text within must be customized your info

webFormField1 = "<text to be entered into first field>"
webFormField2 = "<text to be entered into second field>"
webFormField3 = "<text to be entered into third field>"

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from random import randint
from time import sleep

x = True
opt = Options()
opt.add_experimental_option("debuggerAddress", "localhost:<address number set for debugger port>")
driver = webdriver.Chrome(chrome_options=opt)
wait = WebDriverWait(driver, <time in integer seconds until wait times out>)

def accessForm(site):
    driver.get(site)
    time.sleep(3)
    webFormField1 = "<text to be entered into first field>"
    main_window = driver.current_window_handle
    click1 = driver.find_element_by_xpath('<xpath of first item to click>')
    click1.click()
    time.sleep(1)
    click2 = driver.find_element_by_xpath('<xpath of second item to click>')
    click2.click()
    time.sleep(5)
    driver.switch_to.window(main_window)

def completeForm1(formVariable1):
    main_window = driver.current_window_handle
    form1Field1 = driver.find_element_by_xpath('<xpath of first field in first form>')
    form1Field1.click()
    form1Field1.clear()
    form1Field1.send_keys(webFormField1)
    form1Field2 = driver.find_element_by_xpath('<xpath of second field in first form>')
    form1Field2.click()
    form1Field2.clear()
    form1Field2.send_keys(formVariable1)
    form1Field3 = driver.find_element_by_xpath('<xpath of third field in first form>')
    form1Field3.click()
    form1Field3.clear()
    form1Field3.send_keys(webFormField3)
    submit = driver.find_element_by_xpath('<xpath of submit button>')
    submit.click()
    time.sleep(3)
    #switches to popup
    for window_handle in driver.window_handles:
        if window_handle != main_window:
            driver.switch_to.window(window_handle)
            break
    click3 = wait.until(EC.element_to_be_clickable((By.XPATH, '<xpath of item to click in popup>')))
    click3 = driver.find_element_by_xpath('<xpath of item to click in popup>')
    click3.click()
    time.sleep(1)
    driver.switch_to.window(main_window)
    time.sleep(1)

def completeForm2(formVariable1):
    main_window = driver.current_window_handle
    form2Field1 = driver.find_element_by_xpath('<xpath of first field in second form>')
    form2Field1.click()
    form2Field1.clear()
    form2Field1.send_keys(webFormField1)
    form2Field2 = driver.find_element_by_xpath('<xpath of second field in second form>')
    form2Field2.click()
    form2Field2.clear()
    form2Field2.send_keys(formVariable1)
    submit = driver.find_element_by_xpath('<xpath of submit button>')
    submit.click()
    time.sleep(3)
    for window_handle in driver.window_handles:
        if window_handle != main_window:
            driver.switch_to.window(window_handle)
            break
    wait = WebDriverWait(driver, <time in integer seconds until wait times out>)
    click4 = wait.until(EC.element_to_be_clickable((By.XPATH, '<xpath of item to click in second popup>')))
    click4 = driver.find_element_by_xpath('<xpath of item to click in second popup>')
    click4.click()
    time.sleep(1)
    driver.switch_to.window(main_window)
    time.sleep(1)

while x:
    try:
        accessForm('<website URL containing first form>')
        completeForm1(webFormField2)
        print('First form complete')
    except Exception:
        driver.close()
        driver.get('<website URL containing first form>')
        print('e1')
        time.sleep(<time in integer seconds to wait to attempt loop again>)
        continue
    time.sleep(<time in integer seconds to wait to complete second form>)
    try:
        accessForm('<website URL containing second form>')
        completeForm2(webFormField2)
        print('Second form complete')
    except Exception:
        driver.close()
        driver.get('<website URL containing second form>')
        print('e2')
        time.sleep(<time in integer seconds to wait to attempt loop again>)
        continue
    time.sleep(<time in integer seconds to wait to complete first form>)