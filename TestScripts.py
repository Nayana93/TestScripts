from selenium import webdriver
import time

driver = webdriver.Chrome('..\driver\chromedriver.exe')
driver.get("http://127.0.0.1:9090/")

driver.find_element_by_xpath("//*[@id='navbar']/ul/li[2]/a").click()
time.sleep(5)
driver.find_element_by_xpath("//*[@id='navbar']/ul/li[3]/a").click()
time.sleep(5)
driver.find_element_by_xpath("//*[@id='navbar']/ul/li[3]/a").click()
time.sleep(5)
driver.find_element_by_xpath("//*[@id='navbar']/ul/li[4]/a").click()
time.sleep(5)

driver.get("http://127.0.0.1:9090/home/")
time.sleep(2)
driver.find_element_by_xpath("//*[@id='heroCarousel']/div[1]/div/a").click()
time.sleep(5)
