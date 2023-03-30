# Importing required libraries
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Setting up the webdriver
driver = webdriver.Chrome()

# Navigating to the Amazon.ca homepage
driver.get("https://www.amazon.ca/")

# Waiting for the home page to load
time.sleep(5)

# Finding the menu and clicking it
menu = driver.find_element("id","nav-hamburger-menu")
menu.click()

# Waiting for the menu page to load
time.sleep(5)

# Selecting bestsellers from menu and clicking it
best_sellers = driver.find_element("xpath","/html/body/div[3]/div[2]/div/ul[1]/li[2]/a")
best_sellers.click()

# Waiting for the bestsellers page to load
time.sleep(5)

# Selecting See More option
see_more_best_sellers = driver.find_element("xpath","/html/body/div[1]/div[2]/div[2]/div/div/div/div[2]/div/div[1]/div/div[1]/div/div/div/div/div[1]/div[1]/div/a")
see_more_best_sellers.click()

# Selecting men fashion section
men_fashion = driver.find_element("xpath","/html/body/div[1]/header/div/div[6]/div/a[4]")
men_fashion.click()

# Shopping from men fashion page
shop = driver.find_element("xpath","/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div/div/div/div[1]/div/div/div/a/img")
shop.click()

# Waiting for the shopping page to load
time.sleep(5)

# Closing the webdriver
driver.close()
