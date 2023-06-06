import discord
from discord.ext import commands
import os

client = commands.Bot(command_prefix = "+")
for file in os.listdir("./cogs"):
	if file.endswith(".py"):
		client.load_extension("cogs." + file[:-3])
		print("cogs." + file[:-3])

client.run('ODI3NDU5MDA2NTMyMTU3NDQw.YGbVQA.27I-3uzrO59ncryzVF3YAO5-qmo')