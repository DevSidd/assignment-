import selenium
from selenium import webdriver as wb
webD=wb.Chrome('chromedriver')
webD.get('https://store.hp.com/us/en/pdp/hp-laptop-15t-dy200-2j130av-1')

re=webD.find_element_by_xpath('//*[@id="BVRRContainer"]/div/div/div/div/ol/li[1]/div/div[1]/div/div[1]/div/div[3]/h3')

print(re.text)
