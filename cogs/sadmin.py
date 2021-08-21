import discord
from discord.ext import commands
import os
from pack import function
import datetime
import requests
import urllib.request

statuslist = {}

def time() :
	x = datetime.datetime.now()
	return str(x.day) + "/" + str(x.month) + "/" + str(x.year) + " " + str(x.hour) + ":" + str(x.minute) + ":" + str(x.second)


class SuperAdministration(commands.Cog):

	def __init__(self, client):
		self.client = client

	@commands.command()
	async def reload(self,ctx):
		if(function.check_sadmin(ctx.author.id)):
			await ctx.channel.purge(limit=100)
			embed=discord.Embed(title="Status of the " + time())
			await ctx.channel.send(embed=embed)
			await ctx.channel.last_message.add_reaction("🔁")
			await ctx.channel.last_message.add_reaction("🐱")
			await ctx.channel.last_message.add_reaction("🔑")
		else:
			await ctx.channel.send("T'es pas sadmin :p")

	@commands.Cog.listener()
	async def on_reaction_add(self, reaction, member):
		reloadlist = [603636752569335839, 719945695892734002]
		

		if [reaction.message.guild.id, reaction.message.channel.id] == reloadlist and member.id != 827459006532157440:
			url = "https://raw.githubusercontent.com/AquaBx/discord-bot/db4679fb499fb13d365d03e341f3ba75a512e660/"
			if str(reaction.emoji) == "🔁":	 
				req = requests.get(url + "cogs.json").json()

				try:
					sadmin = coglist.index("sadmin.py")
					sadmin = coglist.pop(sadmin)
					pokemon = coglist.index("pokemon.py")
					pokemon = coglist.pop(pokemon)
				except: pass
				coglist = [x[:-3] for x in req]

			elif str(reaction.emoji) == "🐱":
				coglist = ["pokemon"]

			elif str(reaction.emoji) == "🔑":
				coglist = ["sadmin"]
			
			for cog in coglist:
				with open("./cogs/" + cog + ".py","w", encoding='utf8') as fich:
					nreq = urllib.request.urlopen(url + cog + ".py").read().decode('utf-8')
					fich.write(nreq)

				try:
					try:
						self.client.load_extension("cogs." + cog)
						print(cog)
					except:
						self.client.unload_extension("cogs." + cog)
						self.client.load_extension("cogs." + cog)
					statuslist[cog] = ":green_circle:"
				except:
					statuslist[cog] = ":red_circle:"

			embed=discord.Embed(title="Status of the " + time())

			for key,value in statuslist.items():
				embed.add_field(name=key, value="Status : " + value, inline=False)

			ctx = reaction.message
			await ctx.edit(embed=embed)
			await ctx.remove_reaction(reaction,member)
			

def setup(client):
	client.add_cog(SuperAdministration(client))
