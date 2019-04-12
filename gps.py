import argparse
import sys

import selenium
from GPSPhoto import gpsphoto
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def get_map_screenshot():
    """
    Returns screenshot of whole google map page
    """
    image = sys.argv[1]
    data = gpsphoto.getGPSData(image)
    Lat, Long = data["Latitude"], data["Longitude"]
    url = "https://www.google.co.in/maps?q=" + str(Lat) + ",+" + str(Long)
    driver = webdriver.Firefox()
    driver.get("http://www.python.org")
    driver.save_screenshot("map_." + image_name + ".png")


if __name__ == "__main__":
    get_map_screenshot()
