#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 00:25:25 2020

@author: GurmanBhullar
"""

from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By 
import time 
  
# Replace below path with the absolute path 
# to chromedriver in your computer 
driver = webdriver.Chrome('/Users/GurmanBhullar/Downloads/chromedriver 3') 
  
driver.get("https://web.whatsapp.com/") 
wait = WebDriverWait(driver, 600) 
  
# Replace 'Friend's Name' with the name of your friend  
# or the name of a group  
target = '"Mummy"'
  
# Replace the below string with your own message 
string = "NEVER EVER CALL ME UNTIL YOU GET THE THING IN YOUR MIND"
  
x_arg = '//span[contains(@title,' + target + ')]'
group_title = wait.until(EC.presence_of_element_located(( 
    By.XPATH, x_arg))) 
group_title.click() 
inp_xpath = '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]'

input_box = wait.until(EC.presence_of_element_located(( 
    By.XPATH, inp_xpath))) 
for i in range(100): 
    input_box.send_keys(string + Keys.ENTER + Keys.ENTER) 
    time.sleep(0.1)