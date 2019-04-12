import argparse
import sys
import cv2

import selenium
from GPSPhoto import gpsphoto
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def get_map_screenshot():
    """
    Returns screenshot of whole google map page
    """
    image = "./test.jpg"
    data = gpsphoto.getGPSData(image)
    Lat, Long = data["Latitude"], data["Longitude"]
    url = "https://www.google.co.in/maps?q=" + str(Lat) + ",+" + str(Long)
    driver = webdriver.Firefox()
    # driver.set_window_position(-2000,0)
    driver.get(url)
    driver.save_screenshot("map.png")
    img = cv2.imread("map.png",1)
    img = img[:,int(0.35*img.shape[1]):,:]
    cv2.imwrite("map.png",img)