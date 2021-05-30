import os
import sys
import random
import discord
from discord.ext import commands

#discord API token
TOKEN = "ODQ4MzkyMDMwNDA5MDY0NDY5.YLL8pg.nLuVkQ77_d8lin76nW4Q6jcMk7g"

#prefix 
prefix = None

#create the bot
bot = commands.Bot(command_prefix = prefix)

'''
EVENTS
 ==> create auto assign system to factions in the discord; react to a comment and become a pogger, pougar, or based.
 ==> listen to certains and respond

'''

'''
COMMANDS
 ==> raise-project : enter a raise project and store it
 ==> bucket-list : enter a "thing to do once at pomona" and put it in a priority list
 ==> possibly implement a paranoia game
 ==> text based minigames?
 ==> clear chat

'''

#events
@bot.event
async def on_raw_reaction_add(payload):
    RAW_MESSAGE_ID = 848393714601820182
    messageID = payload.message_id
    if messageID == RAW_MESSAGE_ID:
        guildID = payload.guild_id
        guild = discord.utils.find(lambda g : g.id == guildID, bot.guilds)

        if(payload.emoji.name=="prime"):
            role = discord.utils.get(guild.roles, name = "Poggers")
        elif(payload.emoji.name=="exotic"):
            role = discord.utils.get(guild.roles, name = "Pougars")
        else:
            role = None

        if(role is not None):
            member = payload.member
            if(member is not None):
                await member.add_roles(role)
                print("done")
            else:
                print("member not found")

@bot.event
async def on_raw_reaction_remove(payload):
    RAW_MESSAGE_ID = 848393714601820182
    messageID = payload.message_id
    if messageID == RAW_MESSAGE_ID:
        guildID = payload.guild_id
        guild = discord.utils.find(lambda g : g.id == guildID, bot.guilds)

        if(payload.emoji.name=="prime"):
            role = discord.utils.get(guild.roles, name = "Poggers")
        elif(payload.emoji.name=="exotic"):
            role = discord.utils.get(guild.roles, name = "Pougars")
        else:
            role = None

        if(role is not None):
            member = payload.member
            if(member is not None):
                await member.remove_roles(role)
                print("done")
            else:
                print("member not found")

#commands

bot.run(TOKEN)