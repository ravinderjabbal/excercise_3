import os
import time

from appium.webdriver.common.touch_action import TouchAction

import file_handling
from configuration import driver, log
from image_compare import compare_images





# This function will tap on the provided x,y coordinate
def tap_func(X, Y):
    time.sleep(2)
    user_action = TouchAction(driver)
    log.logger.info("tapping...." + str(X) + "," + str(Y))
    user_action.tap(x=X, y=Y).perform()


# This func will fetch the save image
def fetch_saved_image():
    # sent the location of source folder and destination folder
    log.logger.info("Searching for Folder")
    file_handling.to_pull_folder("/sdcard/DCIM/camera", " ./")
    log.logger.info("Fetching images ")
    img_list = file_handling.file_handle('camera')
    log.logger.info("Returning the fetched the images " + str(img_list))
    return img_list


# this function is used to compare two images
def compare(img1, img2):
    compare_images(img1, img2)


def swipe_down():
    log.logger.info("Swiping Down")
    driver.swipe(514, 500, 514, 800, 1000)


def swipe_leftToright():
    log.logger.info("swiping left to right")
    driver.swipe(240, 600, 730, 600, 500)


def click(locator, value):
    if str(locator) == "id":
        time.sleep(1)
        log.logger.info("Clicking on the locator by id")
        driver.find_element_by_id(value).click()
    elif str(locator).__contains__("xpath"):
        time.sleep(1)
        log.logger.info("Clicking on the locator by xpath")
        driver.find_element_by_xpath(value).click()
    elif str(locator).__contains__("accessibility_id"):
        time.sleep(1)
        log.logger.info("Clicking on the locator by accessibility_id")
        driver.find_element_by_accessibility_id(value)


def send_keys(locator, value, keys):
    if str(locator).__contains__("xpath"):
        time.sleep(1)
        log.logger.info("typing using the locator by xpath")
        driver.find_element_by_xpath(value).send_keys(keys)
    elif str(locator).__contains__("id"):
        time.sleep(1)
        log.logger.info("typing using the locator by id")
        driver.find_element_by_id(value).send_keys(keys)


def getText(locator, value):
    get_text = ""
    if str(locator).__contains__("xpath"):
        time.sleep(1)
        log.logger.info("getting text from the locator by xpath")
        get_text = driver.find_element_by_xpath(value).text
    elif str(locator).__contains__("id"):
        time.sleep(1)
        log.logger.info("getting text from the locator by id")
        get_text = driver.find_element_by_id(value).text
    return get_text
