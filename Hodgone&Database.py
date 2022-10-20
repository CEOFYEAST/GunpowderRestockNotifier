from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import win32api, win32con
import requests

import time

	#discord requests setup

# alt authorization
#NDQ1NzE0Njc2OTQ1Mzg3NTIw.YcE4Mg.TMfuQyq7Kk-C4CTE464-49RUp6E

# main authorization
#MzMzOTUxMDIzOTQ3MzE3MjQ4.YcEykA.SmTXlNrEK7e8yM9MAE8b9ZE7tE4"
header = {
	'authorization' : "NDQ1NzE0Njc2OTQ1Mzg3NTIw.YcE4Mg.TMfuQyq7Kk-C4CTE464-49RUp6E"
}


	#database setup

#key changes per program instance
brandkey = "Hodgdon"

#arraylist declarations
links = []
stockIDs = []

#reads and interprets gunpowder database
with open(r'C:\Users\bento\Desktop\The Project\Database.txt') as f:
    lines = f.readlines()
for x in lines:
	if brandkey not in x: 
		continue
	else:
		links.append(x[x.find('http') : x.find("\t", x.find('http'))])

		stockIDs.append(x[x.find("\t", x.find('http')) + 1 : x.find("\n")])


	#selenium setup

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get('https://shop.hodgdon.com/' + brandkey.lower())


	#main loop

time_counter = 0
while(True):
	elements = []
	for l in range(0, len(stockIDs)):
		for x in range(1, 47):
			article = WebDriverWait(driver, 100).until(
	    		EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/main/section/div/article/div/section/div/div[2]/div/div[2]/div/div[' + str(x) + ']/article'))
	    	)
			entity_id = article.get_attribute("data-entity-id")
			if entity_id == stockIDs[l]:
				elements.append(article)

	for x in range(0, len(elements)):		
		article_class = elements[x].get_attribute("class")
		if "out-of-stock" not in article_class:
			payload = {
				'content' : links[x]
			}
			r = requests.post("https://discord.com/api/v9/channels/922667219756920843/messages", data=payload, headers=header)
		else:
			continue

	for x in range(1, 6):
		time.sleep(1)
		time_counter += 1
		if(time_counter % 900 == 0):
			payload = {
				'content' : str(time_counter/60) + " minutes have elapsed"
			}
			r = requests.post("https://discord.com/api/v9/channels/922879447227572274/messages", data=payload, headers=header)

	#driver.refresh()

	# varget = WebDriverWait(driver, 100).until(
 #    	EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/main/section/div/article/div/section/div/div[2]/div/div[2]/div/div[34]/article'))
 #    )	
	# varget = driver.find_element_by_xpath('/html/body/div[2]/div/main/section/div/article/div/section/div/div[2]/div/div[2]/div/div[34]/article')
	# varget_stock = varget.get_attribute("class")

	

# varget store page element link
# /html/body/div[2]/div/main/section/div/article/div/section/div/div[2]/div/div[2]/div/div[34]/article

# varget out of stock buy link xpath
# /html/body/div[2]/div/main/section/div/article/div/section/div/div[2]/div/div[2]/div/div[39]/article/div/div/div/article/div[1]/div[2]/a[1]

# varget in stock buy link xpath
# /html/body/div[2]/div/main/section/div/article/div/section/div/div[2]/div/div[2]/div/div[39]/article/div/div/div/article/div[1]/div[2]/a[2]

