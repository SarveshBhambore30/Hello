from selenium.webdriver.support import expected_conditions as EC
from behave import *
from telnetlib import EC

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from utils.browser_setup import launch_browser, launch_hrmURL


@given('I launch chrome browser')
def launchBrowser_steps(context):
    context.driver = launch_browser()


@when('I open orange hrm homepage')
def OpenHomepage(context):
     try:
        url = launch_hrmURL()
        context.driver.get(url)
        print(f"Opened URL: {url}")
        context.driver.implicitly_wait(10)
     except Exception as e:
        print(f"Error opening URL: {e}")


@when('Enter username "{user}" and password "{pwd}"')
def enterUsername(context,user,pwd):
    context.driver.find_element(By.NAME, "username").send_keys(user)
    context.driver.find_element(By.NAME, "password").send_keys(pwd)


@when('Click on Login button')
def LoginButton(context):
    context.driver.find_element(By.XPATH, "//button[@type='submit']").click()


@then('User must successfully login to the HRM Dashboard page')
def VerifyPage(context):
    try:
        print("Waiting for Dashboard element to be visible...")
        WebDriverWait(context.driver, 30).until(EC.visibility_of_element_located((By.XPATH, "//h6[contains(text(), 'Dashboard')]")))
        print("Dashboard element found. Retrieving text...")
        text = context.driver.find_element(By.XPATH, "//h6[contains(text(), 'Dashboard')]").text
        print(f"Retrieved text: {text}")
    except Exception as e:
        context.driver.close()
        assert False, f"Test got failed: {e}"
    if text == "Dashboard":
        context.driver.close()
        assert True, "Test got passed"
    else:
        context.driver.close()
        assert False, "Text did not match 'Dashboard'"



