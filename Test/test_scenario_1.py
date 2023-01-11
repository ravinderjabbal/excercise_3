# 1.	This scenario is based on automation Ravinder wrote for Motorola.
# Automated Validation of AI in Camera Feature which Auto focus on the Human Face in  shot.

import time

import Base
from configuration import log, driver


def test_camera():
    time.sleep(2)

    # to capture the photo
    log.logger.info("Capturing Photo")
    Base.tap_func(544, 1984)

    time.sleep(2)

    # to capture second image
    log.logger.info("Capturing 2nd Photo")
    Base.tap_func(544, 1984)

    time.sleep(1)

    # to fetch the folder from DUT where file in saved
    log.logger.info("Looking for captured pic")
    test_images = Base.fetch_saved_image()

    # to compare the images
    log.logger.info("Comparing the images '" + str(test_images[0]) + "' & '" + str(test_images[1] + "'"))
    result = Base.compare_images(test_images[0], test_images[1])
    log.logger.info("Result : " + str(result))

    driver.close_app()
