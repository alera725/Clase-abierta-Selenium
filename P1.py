#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 18:10:26 2020

@author: Aera
"""

from selenium import webdriver
import unittest 
import time 
import os
os.chdir('/Users/Aera/Documents/ALEJANDRO RAMOS GUTIERREZ/PROYECTOS/CURSO SELENIUM PABLO')


tc = unittest.TestCase('__init__')

driver = webdriver.Chrome('/Users/Aera/Documents/ALEJANDRO RAMOS GUTIERREZ/PROYECTOS/CURSO SELENIUM PABLO/chromedriver')
driver.get('http://automationpractice.com/index.php')


driver.find_element_by_id('search_query_top').send_keys('hola')
driver.find_element_by_name('submit_search').click()
#driver.find_element_by_xpath('//*[@id="center_column"]/p')

time.sleep(5)
tc.assertEqual('No results were found for your search "hola"',driver.find_element_by_xpath('//*[@id="center_column"]/p').text)
driver.close() #Cerrar el navegador
driver.quit() #Cerrar la cesion 


# ---------------------------- Otro ejemplo --------------------------------

import time
from selenium import webdriver

driver = webdriver.Chrome('/Users/Aera/Documents/ALEJANDRO RAMOS GUTIERREZ/PROYECTOS/CURSO SELENIUM PABLO/chromedriver')  # Optional argument, if not specified will search path.
driver.get('http://www.google.com/');
time.sleep(5) # Let the user actually see something!
search_box = driver.find_element_by_name('q')
search_box.send_keys('ChromeDriver')
search_box.submit()
time.sleep(5) # Let the user actually see something!
driver.quit()