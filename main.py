import discord
from discord.ext import commands

bot = commands.Bot(command_prefix = "!", description = "Thomas Bot la Pluie de Plumes")
bot.event
async def on_ready():
    print("Ready !")
bot.run("MTA0MzYyODgwNzc5NTUxNTQzMw.GGhWzz.7G_U-zWeIIghou61N_pIILRhtHZBRMAefbaRGQ")