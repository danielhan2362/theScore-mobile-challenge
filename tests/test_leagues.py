import os
import time

from appium import webdriver
from appium.options.android import UiAutomator2Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from resources import *
from device_info import get_android_device_model, get_android_os_version


options = UiAutomator2Options()
options.platform_name = 'Android'
options.device_name = get_android_device_model()
options.automation_name = 'UiAutomator2'
options.platformVersion = get_android_os_version()
options.auto_grant_permissions = True
options.app = os.getcwd() + '/test_app/theScore_ Sports News & Scores_24.8.0_Apkpure.apk'

driver = webdriver.Remote('http://127.0.0.1:4723', options=options)


def find_element(locator, wait_time):
    element = WebDriverWait(driver, wait_time).until(EC.presence_of_element_located(locator))
    return element


def assert_data(data):
    print("Assert data", data)
    for key in data:
        assert key == data[key], f"Expected '{data}' to match - Assertion Failed"


# Click on Get Started button
get_started_button = find_element(Onboarding.GET_STARTED_BUTTON, 5)
get_started_button.click()
print("Clicked Get Started button")

# Check if CCPA screen appears
time.sleep(7)
try:
    ccpa_continue_button = find_element(Onboarding.CCPA_CONTINUE_BUTTON, 5)
    if ccpa_continue_button.is_displayed():
        ccpa_continue_button.click()
        print("Dismissing CCPA screen")
        time.sleep(3)
        get_started_button = find_element(Onboarding.GET_STARTED_BUTTON, 5)
        get_started_button.click()
    else:
        print("Not on CCPA screen")

except NoSuchElementException:
    print(f"'{ccpa_continue_button}' not found")

# Click on NFL Football
nfl_football_row = find_element(Onboarding.NFL_FOOTBALL_ROW, 5)
nfl_football_row.click()
print("Clicked NFL Football")

# Click on Continue button (Choose your favorite leagues screen)
continue_button = find_element(Onboarding.CONTINUE_BUTTON, 5)
continue_button.click()
print("Clicked Continue button")

# Click on San Francisco 49ers
sf_niners = find_element(Onboarding.SF_NINERS, 5)
sf_niners.click()
print("Clicked San Francisco 49ers")

# Click Continue button (Choose your favorite teams screen)
continue_button = find_element(Onboarding.CONTINUE_BUTTON, 5)
continue_button.click()
print("Clicked Continue button")

# Click on Continue button (Never miss a game)
continue_button = find_element(Onboarding.CONTINUE_BUTTON, 5)
continue_button.click()
print("Clicked Continue button")

# Click on Maybe Later
maybe_later = find_element(Onboarding.MAYBE_LATER, 5)
maybe_later.click()
print("Clicked Maybe Later")

# Check if Profile popup appears
time.sleep(5)
try:
    ok_got_it = find_element(HomeScreen.OK_GOT_IT, 5)
    if ok_got_it.is_displayed():
        ok_got_it.click()
        print("Dismissing Profile popup")
    else:
        print("Profile popup did not appear")

except NoSuchElementException:
    print(f"'{ok_got_it}' not found")

# Click Leagues tab
leagues_tab = find_element(HomeScreen.LEAGUES_TAB, 5)
leagues_tab.click()
print("Clicked Leagues tab")

# Click Edit
edit = find_element(LeaguesScreen.EDIT, 5)
edit.click()
print("Clicked Edit")
time.sleep(3)

# Click Done
done = find_element(LeaguesScreen.DONE, 5)
done.click()
print("Clicked Done")
time.sleep(3)

# Click NFL row
nfl_row = find_element(LeaguesScreen.NFL_ROW, 5)
nfl_row.click()
print("Clicked NFL")

# Click Standings tab
standings_tab = find_element(NFLScreen.STANDINGS_TAB, 5)
standings_tab.click()
print("Clicked Standings tab")

# Verify AFC tab
try:
    afc_tab = find_element(NFLScreen.AFC_TAB, 5)
    if afc_tab.is_displayed():
        print("Verifying AFC tab label")
        afc_tab = afc_tab.text
        data = {afc_tab: "AFC"}
        assert_data(data)
    else:
        print("AFC tab not displayed")

except NoSuchElementException:
    print(f"'{afc_tab}' not found")

# Go back to Leagues screen
driver.back()
print("Going back to Leagues screen")

# Verify on Leagues screen
try:
    leagues_screen_title = find_element(LeaguesScreen.LEAGUE_SCREEN_TITLE, 5)
    if leagues_screen_title.is_displayed():
        print("Verifying Leagues screen title")
        leagues_screen_title = leagues_screen_title.text
        data = {leagues_screen_title: "Leagues"}
        assert_data(data)
    else:
        print("League screen title not displayed")

except NoSuchElementException:
    print(f"'{leagues_screen_title}' not found")

# Exit app
driver.quit()
