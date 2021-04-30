import discord
import datetime
import time
import bs4
import requests
import asyncio
from discord.ext import commands
from time import sleep
from bs4 import BeautifulSoup

TOKEN = ''

client = commands.Bot(command_prefix = 'c;')

@client.event
async def on_ready():
    print('Bot is Online')

@client.command(pass_context=True)
async def clear(ctx, amount=100):
	channel = discord.Object(id='687396047831826451') 
	messages = []
	async for message in client.logs_from(channel, limit=int(amount)):
		messages.append(message)
		await client.delete_messages(messages)

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

#case counter

#GLOBAL COUNTER
newGlobalCases=str(globalCases)
newGlobalDeaths=str(globalDeaths)
newGlobalRecovered=str(globalRecovered)
TGlobalCases=str(globalCases)
TGlobalDeaths=str(globalDeaths)
TGlobalRecovered=str(globalRecovered)


noCommaNewGlobalCases = newGlobalCases.replace(',','')
noCommaNewGlobalDeaths = newGlobalDeaths.replace(',','')
noCommaNewGlobalRecovered = newGlobalRecovered.replace(',','')
noCommaGlobalCases = TGlobalCases.replace(',','')
noCommaGlobalDeaths = TGlobalDeaths.replace(',','')
noCommaGlobalRecovered = TGlobalRecovered.replace(',','')


changeGlobalCases=int(noCommaNewGlobalCases)-int(noCommaGlobalCases)
changeGlobalDeaths=int(noCommaNewGlobalDeaths)-int(noCommaGlobalDeaths)
changeGlobalRecovered=int(noCommaNewGlobalRecovered)-int(noCommaGlobalRecovered)
############

#UK COUNTER
newUKCases=str(ukCases)
newUKDeaths=str(ukDeaths)
newUKRecovered=str(ukRecovered)
TUKCases=str(ukCases)
TUKDeaths=str(ukDeaths)
TUKRecovered=str(ukRecovered)


noCommaNewUKCases = newUKCases.replace(',','')
noCommaNewUKDeaths = newUKDeaths.replace(',','')
noCommaNewUKRecovered = newUKRecovered.replace(',','')
noCommaUKCases = TUKCases.replace(',','')
noCommaUKDeaths = TUKDeaths.replace(',','')
noCommaUKRecovered = TUKRecovered.replace(',','')


#changeUKCases=int(noCommaNewUKCases)-int(noCommaUKCases)
#changeUKDeaths=int(noCommaNewUKDeaths)-int(noCommaUKDeaths)
#changeUKRecovered=int(noCommaNewUKRecovered)-int(noCommaUKRecovered)
############



def timeOfParse():
    parseTime = time.localtime()
    parse_time = time.strftime("%H:%M:%S", parseTime)
    latestUpdate = str(parse_time) + ', GMT'
    print('Parse Time Noted')
    return latestUpdate

#Web Scraping Function   
def parseCases():

    globalCases=soupGLOBAL.find_all('div',{'class':'maincounter-number'})[0].find('span').text
    globalDeaths=soupGLOBAL.find_all('div',{'class':'maincounter-number'})[1].find('span').text
    globalRecovered=soupGLOBAL.find_all('div',{'class':'maincounter-number'})[2].find('span').text

    ukCases=soupUK.find_all('div',{'class':'maincounter-number'})[0].find('span').text
    ukDeaths=soupUK.find_all('div',{'class':'maincounter-number'})[1].find('span').text
    ukRecovered=soupUK.find_all('div',{'class':'maincounter-number'})[2].find('span').text
    timeOfParse()
    print('Parsed Cases')

embed = discord.Embed(
		title  = 'Coronavirus Update!',
		description = 'Below you can find the latest information on the COVID-19 Pandemic. This bot automatically checks for new updates every hour.',
		colour = discord.Colour.red()
		)

embed.set_footer(text='Last Update: ' + str(timeOfParse()))
embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/689810841998065811/689811121406083075/Outbreak_Map.png'),
	#embed.set_author(name='Coronavirus Tracker!', icon_url='https://cdn.discordapp.com/attachments/689810841998065811/689817317189615652/sars-cov-19.jpg')
embed.add_field(name='🌍  **Coronavirus Global Statistics:**', value='­‎', inline=True)
embed.add_field(name='Cases:', value=str(globalCases), inline=False)
embed.add_field(name='Deaths:', value=str(globalDeaths), inline=False)
embed.add_field(name='Recoveries:', value=str(globalRecovered), inline=False)

embed.add_field(name='🇬🇧  **Coronavirus UK Statistics:**', value='‎', inline=False)
embed.add_field(name='Cases:', value=str(ukCases), inline=False)
embed.add_field(name='Deaths:', value=str(ukDeaths), inline=False)
embed.add_field(name='Recoveries:', value=str(ukRecovered), inline=False)

@client.command()
async def latest(ctx, amount=100):
	globalCases=TGlobalCases
	globalDeaths=TGlobalDeaths
	globalRecovered=TGlobalRecovered
	ukCases=TUKCases
	ukDeaths=TUKDeaths
	ukRecovered=TUKRecovered
	parseCases()
	timeOfParse()

	await ctx.send(embed=embed)

@client.command()
async def hourly(ctx):
    globalCases=TGlobalCases
    globalDeaths=TGlobalDeaths
    globalRecovered=TGlobalRecovered
    ukCases=TUKCases
    ukDeaths=TUKDeaths
    ukRecovered=TUKRecovered
    parseCases()
    timeOfParse()
    hourlyTracker = 1
    print('Tracked Stats')
    await ctx.send(embed=embed)
    await asyncio.sleep(5)

async def timer():
    print('Time')

def stop():
    task.cancel()

async def timeSched():
    loop = asyncio.get_event_loop()
    loop.call_later(1740, stop)
    task = loop.create_task(timer())

    try:
        loop.run_until_complete(task)
    except asyncio.CancelledError:
        pass

client.run(TOKEN)
