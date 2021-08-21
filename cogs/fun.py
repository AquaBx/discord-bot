import discord
from discord.ext import commands
import os
import random
from pack import function

class Fun(commands.Cog):

	def __init__(self, client):
		self.client = client

	@commands.command()
	async def blague(self,ctx):	
		blague = os.listdir("blague")
		tire = random.choice(blague)
		file=discord.File(fp="blague/"+tire, filename=tire)
		embed=discord.Embed(title=tire, url="", description="", color=0xff0000)
		embed.set_author(name=ctx.author.name,icon_url=ctx.author.avatar_url)
		await ctx.channel.send(embed=embed,file=file)

def setup(client):
	client.add_cog(Fun(client))