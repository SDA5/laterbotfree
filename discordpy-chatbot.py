#!/usr/bin/env python3

import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import requests
import json

Bot = discord.Client()

Bot = commands.Bot(command_prefix= "/")
@Bot.event 
async def on_ready():
    print('Logged in as')
    print(Bot.user.name)
    print(Bot.user.id)
    print('------')


@Bot.command(administrator=True)
async def send(ctx, sleepp, message):
    channelID = "" # enable dev mode on discord, right-click on the channel, copy ID
    botToken = ""    # get from the bot page. must be a bot, not a discord app

    baseURL = "https://discordapp.com/api/channels/{}/messages".format(channelID)
    headers = { "Authorization":"Bot {}".format(botToken),
            "User-Agent":"myBotThing (http://some.url, v0.1)",
            "Content-Type":"application/json", }

    await asyncio.sleep(int(sleepp))
    POSTedJSON =  json.dumps ( {"content":message} )
    r = requests.post(baseURL, headers = headers, data = POSTedJSON)

    

Bot.run("")
