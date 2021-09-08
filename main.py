import discord
import requests
import json
from datetime import date
import random

client = discord.Client()

bad_words = ["eric", "eric lin"]

def countdown():
    today_months = int(date.today().strftime("%m"))
    today_days = int(date.today().strftime("%d"))
    today_year = int(date.today().strftime("%y"))
    end = "062821"
    end_months = int(end[0]+end[1])
    end_days = int(end[2]+end[3])
    end_year = int(end[4]+end[5])

    remain_mo = end_months - today_months
    remain_da = end_days - today_days
    remain_yr = end_year - today_year

    if remain_yr >0:
        if remain_mo >0:
            if remain_da >0:
                time = str(remain_yr)+ " years left, " + str(remain_mo)+ " months left, and " + str(remain_da) + " days left"
            else:
                time = str(remain_yr)+ " years left, and " + str(remain_mo)+ " months left"
        else:
            if remain_da >0:
                time = str(remain_yr)+ " years left, and " + str(remain_da) + " days left"
            else:
                time = str(remain_yr)+ " years left" 
    else:
        if remain_mo >0:
            if remain_da >0:
                time = str(remain_mo)+ " months left, and " + str(remain_da) + " days left"
            else:
                time = str(remain_mo)+ " months left"
        else:
            if remain_da >0:
                time = str(remain_da) + " days left"
            else:
                time = "ITS TODAY"
    if time != "ITS TODAY":
        return("There are "+ time + " until the end of school on June 28, 2021")
    else:
        return("ITS TODAY!!!!"+ " :tada:"+ " :partying_face:")

def roll(rollInput): 
    rollInput = rollInput.replace("!roll","")
    rollInput = rollInput.lstrip()
    if rollInput.isnumeric():
        rollOutput = random.randint(0,int(rollInput))
        return(rollOutput)
    else:
        return ("!roll [integer] only.")

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!countdown'):
        time = countdown()
        await message.channel.send(time)
        
    if message.content.startswith("!roll"):
        rollOutput = roll(message.content)
        await message.channel.send(rollOutput)

    if message.content.startswith("!info"):
        await message.channel.send("Poorly created by justin chow")

    if message.content.startswith("!help"):
        await message.channel.send("!countdown - how many days till the end of school\n!roll [integer] - gives you a random number\n!info - bruh")

    if message.content.startswith("!bowser"):
        await message.channel.send("fuck off")
    
    if any(word in message.content for word in bad_words):
        await message.channel.send(message.author.mention+" hey! you can't say that here") 
        await message.delete()













client.run("ODM0OTA3MzEzODQ4MzIwMDcx.YIHuBw.q3Xq_-OUFvJOjpsmNM_s0ct9XX4")
