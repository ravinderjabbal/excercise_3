import os

from configuration import log

source_folder = "/sdcard/DCIM/camera"
dest_folder = "./"


# This function is used to pull folder from DUT and saved in working library
def to_pull_folder(src_folder, dst_folder):
    log.logger.info("Pulling the folder from DUT: " + str(src_folder))
    os.system("adb pull " + src_folder + " " + dst_folder)
    log.logger.info("Folder copied to: " + str(dst_folder))


# it will return the files under the requested folder
def file_handle(location):
    log.logger.info("Fetching the files under: " + str(location))
    file_list = os.listdir(dest_folder + location)
    new_list = []
    for i in file_list:
        new_list.append(os.path.abspath('camera/' + str(i)))
    log.logger.info("Returning the files from '" + str(location) + "' " + "with absolute path: " + str(new_list))
    return new_list
