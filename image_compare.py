from PIL import Image
from PIL import ImageChops

from configuration import log


def compare_images(path_one, path_two):
    """
    compare images
    :param path_one: first image
    :param path_two: second image
    :return: same is True, otherwise is False
    """
    image_one = Image.open(path_one)
    image_two = Image.open(path_two)
    try:
        log.logger.info("Looks similar ..... Thinking......")
        diff = ImageChops.difference(image_one, image_two)

        if diff.getbbox() is None:
            # same
            log.logger.info("Match confirmed")
            log.logger.info("Images are similar")
            return True
        else:
            log.logger.info("Not Matched")
            log.logger.info("Images are different")
            return False

    except ValueError as e:
        log.logger.error("Unexpected Error !!")
        log.logger.info("Not my fault")
        return False
