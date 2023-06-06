import discord
from discord.ext import commands
import requests
from pack import function

class Fun(commands.Cog):

	def __init__(self, client):
		self.client = client

	@commands.command()
	async def chess(self,ctx):
		user = ctx.author
		msg = await ctx.guild.get_channel(827601690940276786).fetch_message(827606075917729994)
		msg = msg.content.split("```")[1].replace("\n", "").replace(" ", "").split("*")[1:]
		msg = [ms.split(":")[1].split("#") for ms in msg]
		
		ls = [rs for rs in msg if int(rs[1]) == user.id]

		if len(ls) == 0:
			response = "Veuillez mettre votre pseudo dans ce channel https://discord.com/channels/827063633091624991/827601690940276786/"
		else:
			player = ls[0][0]
			url = "https://api.chess.com/pub/player/"+player+"/stats"
			req = requests.get(url).json()
			list1 = ["chess_rapid","chess_blitz","chess_bullet"]
			list2 = []
			for item in list1 : 
				try:
					var = req[item]["last"]["rating"]
				except:
					var = 0
				list2.append(var)
			ranks = ["Non évalué","Débutant - 800","Amateur - 1000","Avancé - 1200"]
			score = list2[0]
			
			for rank in ranks:
				await user.remove_roles(discord.utils.get(user.guild.roles, name=rank))
	
			if score > 1200:
				await user.add_roles(discord.utils.get(user.guild.roles, name=ranks[3]))
			elif score > 1000:
				await user.add_roles(discord.utils.get(user.guild.roles, name=ranks[2]))
			elif score > 800:
				await user.add_roles(discord.utils.get(user.guild.roles, name=ranks[1]))
			else:
				await user.add_roles(discord.utils.get(user.guild.roles, name=ranks[0]))
			response = list2
		
		await ctx.channel.send(response)
		

def setup(client):
	client.add_cog(Fun(client))