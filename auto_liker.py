from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from time import sleep
import random 
  
usr=input('Enter Email Id:')  
pwd=input('Enter Password:')
 
chrome_options = webdriver.ChromeOptions()

prefs = {"profile.default_content_setting_values.notifications" : 2}

chrome_options.add_experimental_option("prefs",prefs)
  
driver = webdriver.Chrome('/usr/bin/chromedriver',chrome_options=chrome_options) 
       
driver.get('https://www.facebook.com/') 
print ("Opened facebook") 
sleep(1) 
  
username_box = driver.find_element_by_id('email') 
username_box.send_keys(usr) 
print ("Email Id entered") 
sleep(1) 
  
password_box = driver.find_element_by_id('pass') 
password_box.send_keys(pwd) 
print ("Password entered") 
  
login_box = driver.find_element_by_id('loginbutton') 
login_box.click() 
print ("Done") 

j = 0
while(True):
	j = j + 1
	body_elem = driver.find_element_by_tag_name('body')     
	body_elem.send_keys(Keys.DOWN)
	body_elem.send_keys(Keys.DOWN)      
	sleeptime = random.randint(1,5)
	sleep(sleeptime)
	try:
		likes = driver.find_elements_by_xpath("//a[contains(@aria-pressed, 'false')]") 
		for i in likes:
			i.click()
			sleep(1)
	except:
		pass
	if(j > 100):
		driver.refresh()
		j = 0



		

