import argparse
import sys

import selenium
from GPSPhoto import gpsphoto
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def get_map_screenshot(image):
    """
    Returns screenshot of whole google map page
    """
    data = gpsphoto.getGPSData(image)
    Lat, Long = data["Latitude"], data["Longitude"]
    url = "https://www.google.co.in/maps?q=" + str(Lat) + ",+" + str(Long)
    driver = webdriver.Firefox()
    driver.get("http://www.python.org")
    driver.save_screenshot("map_." + image.split('/')[-1])


if __name__ == "__main__":
    get_map_screenshot("~/Git/SCT19/static/bus1.jpg")
