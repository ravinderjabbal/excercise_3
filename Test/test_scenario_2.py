# a. Make a call from Test Device to Support Device. --Done
# b. While call is ongoing switch to YouTube application --Done
# c. Play video while call is still ON --Done
# d. Switch to call, Note time spent on call --Done
# e. Hand up call and send SMS to support device with time spent on call. --Done
# f. Switch back to YouTube app and enjoy video for 5 minute. --Done
# g. End test case
import time

from appium.webdriver.extensions.android.nativekey import AndroidKey
from num2words import num2words
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

import Base
from configuration import driver, log
from selenium.webdriver.support import expected_conditions

numberToCall = "8884780752"  # The number which we want to call
callAppPackageName = "com.google.android.dialer"
callAppActivityName = "com.android.dialer.DialtactsActivity"
youTubeAppPackageName = "com.google.android.youtube"
youTubeAppActivityName = 'com.google.android.apps.youtube.app.watchwhile.WatchWhileActivity'
msgAppPackageName = "com.google.android.apps.messaging"
msgAppActivityName = "com.google.android.apps.messaging.home.HomeActivity"


def change_number_text(number):
    log.logger.info("Converting the number to text : " + str(number))
    txtNumber = num2words(number)
    log.logger.info("Returning converted Number :" + str(txtNumber))
    return txtNumber


def make_a_call():
    log.logger.info("Number to call :" + str(numberToCall))

    log.logger.info("Opening the Phone App")
    driver.start_activity(callAppPackageName, callAppActivityName)

    time.sleep(2)

    log.logger.info("Opening Dialer")
    Base.tap_func(929, 1855)

    time.sleep(2)

    log.logger.info("Making a call")
    for number in numberToCall:
        txtNumber = change_number_text(number)
        Base.click("id", "com.google.android.dialer:id/" + str(txtNumber))  # 1 for one , 2 for two

    log.logger.info("Clicking on Call button")
    Base.tap_func(540, 2079)

    try:
        wait = WebDriverWait(driver, 5)
        wait.until(
            expected_conditions.visibility_of_element_located(
                (By.ID, "com.google.android.dialer:id/contactgrid_bottom_timer")))
    except:
        log.logger.error("Call could not be connected ")

    time.sleep(2)
    Base.tap_func(999, 714)
    run_youTube_app()


def run_youTube_app():
    log.logger.info("Opening the YouTube App")
    driver.start_activity(youTubeAppPackageName, youTubeAppActivityName)

    time.sleep(7)

    Base.click("xpath", "//android.widget.ImageView[@content-desc='Search']")
    time.sleep(2)
    Base.send_keys("id", "com.google.android.youtube:id/search_edit_text", "35 Sine Tones *For Audio Engineers*")
    time.sleep(1)
    driver.press_keycode(AndroidKey.ENTER)
    time.sleep(5)
    Base.click("xpath",
               '//android.view.ViewGroup[@content-desc="35 Sine Tones *For Audio Engineers* - 35 minutes - Go to channel - Outlier Audio - 81K views - 2 years ago - play video"]')
    time.sleep(2)
    try:
        wait = WebDriverWait(driver, 10)
        wait.until(
            expected_conditions.element_to_be_clickable((By.ID, "com.google.android.youtube:id/skip_ad_button_text")))
        Base.click("id", "com.google.android.youtube:id/skip_ad_button_text")
        log.logger.info("Adv Skipped")

    except:
        log.logger.info("Adv did not appear")

    in_call_activity()


def in_call_activity():
    log.logger.info("Opening Notification Panel")
    driver.open_notifications()
    time.sleep(2)

    log.logger.info("Opening the ongoing call screen")
    Base.click("xpath", "//android.widget.TextView[@text='Ongoing call']")

    log.logger.info("Fetching the time spent on call")
    Time_spent_on_call = Base.getText("id", "com.google.android.dialer:id/contactgrid_bottom_timer")
    log.logger.info("Time spent on call :" + Time_spent_on_call)

    log.logger.info("Ending the call")
    Base.click("id", "com.google.android.dialer:id/incall_end_call")

    log.logger.info("Closing TrueCaller Popup")
    try:
        wait = WebDriverWait(driver, 9)
        wait.until(
            expected_conditions.visibility_of_element_located((By.ID, "com.truecaller:id/closeIcon")))
        log.logger.info("TrueCaller Popup located")
    except:
        log.logger.info("Truecaller popup not seen")

    log.logger.info("Closed Truecaller popup")
    Base.click("id", "com.truecaller:id/closeIcon")

    send_sms(Time_spent_on_call)


def send_sms(Time_spent_on_call):
    log.logger.info("Preparing to send the SMS")
    time.sleep(2)

    log.logger.info("Opening the Message app")
    driver.start_activity(msgAppPackageName, msgAppActivityName)

    log.logger.info("Clicking on New Message")
    Base.tap_func(867, 2083)

    log.logger.info("Entering the recipient : " + numberToCall)
    Base.send_keys("id", "com.google.android.apps.messaging:id/recipient_text_view", numberToCall)
    driver.press_keycode(AndroidKey.ENTER)

    log.logger.info("Writing the message")
    time.sleep(5)

    log.logger.info("Entering the Call duration : " + Time_spent_on_call)
    Base.click("id", "com.google.android.apps.messaging:id/compose_message_text")
    time.sleep(1)
    Base.send_keys("id", "com.google.android.apps.messaging:id/compose_message_text", Time_spent_on_call)

    time.sleep(1)

    log.logger.info("Sending the SMS")
    Base.click("id", "com.google.android.apps.messaging:id/send_message_button_icon")

    try:
        wait = WebDriverWait(driver, 10)
        wait.until(expected_conditions.visibility_of_element_located((By.ID, "android:id/button2")))
        Base.click("id", "android:id/button2")
    except:
        log.logger.info("No Flash SMS ")

    time.sleep(2)

    switching_back_to_youTube()


def switching_back_to_youTube():
    log.logger.info("Going to  Recent Screen")
    driver.press_keycode(AndroidKey.APP_SWITCH)
    Base.swipe_leftToright()
    log.logger.info("Locating YouTube")
    try:
        wait = WebDriverWait(driver, 9)
        wait.until(
            expected_conditions.visibility_of_element_located(
                (By.XPATH, "//android.widget.FrameLayout[@content-desc='YouTube']")))
        log.logger.info("YouTube Located")
    except:
        log.logger.error("YouTube Not found")

    log.logger.info("YouTube Located,Opening...")
    Base.tap_func(500, 500)

    log.logger.info("Playing the video")
    Base.click("xpath", "//android.widget.ImageView[@content-desc=\"Play video\"]")

    log.logger.info("Now program will wait for sometime and abort")
    time.sleep(10)


def test_second_scenario():
    make_a_call()
