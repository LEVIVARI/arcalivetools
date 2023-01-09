from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import urllib.request
import os

driver = webdriver.Firefox()
url = "https://arca.live/b/singbung"
driver.get(url)
driver.implicitly_wait(5)

adImgElem = driver.find_element(By.CSS_SELECTOR, "#svQazR5NHC3xCQr3 > a:nth-child(2) > img:nth-child(1)")
adImg_url = adImgElem.get_attribute('src')
adLinkElem = driver.find_element(By.CSS_SELECTOR, "#svQazR5NHC3xCQr3 > a:nth-child(2)")
adLink_url = adLinkElem.get_attribute('href')
