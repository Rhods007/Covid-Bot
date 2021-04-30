import datetime
import time
from time import sleep
import bs4
import requests
from bs4 import BeautifulSoup




    

#Web Scraping
rGLO=requests.get('https://www.worldometers.info/coronavirus/')
rUK=requests.get('https://www.worldometers.info/coronavirus/country/uk/')

soupGLOBAL=bs4.BeautifulSoup(rGLO.text, "lxml")
soupUK=bs4.BeautifulSoup(rUK.text, "lxml")

globalCases=soupGLOBAL.find_all('div',{'class':'maincounter-number'})[0].find('span').text
globalDeaths=soupGLOBAL.find_all('div',{'class':'maincounter-number'})[1].find('span').text
globalRecovered=soupGLOBAL.find_all('div',{'class':'maincounter-number'})[2].find('span').text

ukCases=soupUK.find_all('div',{'class':'maincounter-number'})[0].find('span').text
ukDeaths=soupUK.find_all('div',{'class':'maincounter-number'})[1].find('span').text
ukRecovered=soupUK.find_all('div',{'class':'maincounter-number'})[2].find('span').text


#Web Scraping Function   
def parseCases():

    globalCases=soupGLOBAL.find_all('div',{'class':'maincounter-number'})[0].find('span').text
    globalDeaths=soupGLOBAL.find_all('div',{'class':'maincounter-number'})[1].find('span').text
    globalRecovered=soupGLOBAL.find_all('div',{'class':'maincounter-number'})[2].find('span').text

    ukCases=soupUK.find_all('div',{'class':'maincounter-number'})[0].find('span').text
    ukDeaths=soupUK.find_all('div',{'class':'maincounter-number'})[1].find('span').text
    ukRecovered=soupUK.find_all('div',{'class':'maincounter-number'})[2].find('span').text

    parseTime = time.localtime()
    parse_time = time.strftime("%H:%M:%S", parseTime)
    latestUpdate = str(parse_time) + ' GMT'


#Print to Console
print('------')
print('Global Cases:' + str(globalCases))
print('Global Deaths:' + str(globalDeaths))
print('Global Recovered:' + str(globalRecovered))
print('------')
print('UK Cases:' + str(ukCases))
print('UK Deaths:' + str(ukDeaths))
print('UK Recovered:' + str(ukRecovered))
print('------')
print(' ')
wait = input("Press enter to terminate")
