import logging
import os
import time

from appium import webdriver

import Base
from looger.logger_util import Logger

log = Logger(__name__, logging.INFO)

desired_caps = dict(
    deviceName='NDOR4X0011',
    platformName='Android',
    appPackage='com.motorola.camera2',
    appActivity='com.motorola.camera.Camera',
    platformVersion='10',
    noReset='True'
)

log.logger.info("Configuring " + str(desired_caps))
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
log.logger.info("Configuration done " + str(driver))
