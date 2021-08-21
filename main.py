import discord
from discord.ext import commands
import os

client = commands.Bot(command_prefix = "+")
for file in os.listdir("./cogs"):
	if file.endswith(".py"):
		client.load_extension("cogs." + file[:-3])
		print("cogs." + file[:-3])

with open("token.txt") as token:
	client.run(token.read())