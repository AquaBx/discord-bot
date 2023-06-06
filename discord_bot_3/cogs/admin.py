import discord
from discord.ext import commands
import json
from pack import function
import requests

def bddpost(type,id,varname,var,post):
	requests.post("https://aquabx.ovh/api/bot_post.php?q=bdd&t="+post, data={'type': type,'id': id,'varname':varname,'var': json.dumps(var)})

class Administration(commands.Cog):

	def __init__(self, client):
		self.client = client

	@commands.command()
	async def init(self, ctx):
		guild = str(ctx.guild.id)
		await ctx.guild.create_voice_channel("Membres:")
		await ctx.guild.create_voice_channel("Bot:")
		welc = [str(discord.utils.get(ctx.guild.voice_channels, name="Membres:").id),str(discord.utils.get(ctx.guild.voice_channels, name="Bot:").id)]		
	
		bot= [member.bot for member in ctx.guild.members]
				
		channel = self.client.get_channel(int(welc[0]))
		await channel.edit(name="Membres: " + str(bot.count(False)))
		await channel.set_permissions(ctx.guild.default_role, connect=False)
	
		channel = self.client.get_channel(int(welc[1]))
		await channel.edit(name="Bots: " + str(bot.count(True)))
		await channel.set_permissions(ctx.guild.default_role, connect=False)
	
		bddpost("guilds",guild,"chann",welc,"rep")

	@commands.command()
	async def welcome(self,ctx,id,*,message):
		if(function.check_admin(ctx)):
			guild = str(ctx.channel.guild.id)
			welc = [id,message]
			bddpost("guilds",guild,"welc",welc,"rep")

			channel = self.client.get_channel(int(welc[0]))
			await channel.send(welc[1])
		else:
			await ctx.channel.send("T'es pas admin :p")

	@commands.command()
	async def pokespawn(self,ctx,id):
		if(function.check_admin(ctx)):
			guild = str(ctx.channel.guild.id)
			bddpost("guilds",guild,"pokemon",id,"rep")

			channel = self.client.get_channel(int(id))
			await channel.send("Hautes Herbes")
		else:
			await ctx.channel.send("T'es pas admin :p")

	@commands.command()
	async def clear(self,ctx,num):
		if(function.check_admin(ctx)):
			await ctx.channel.send('Supression de {} messages'.format(num))
			deleted = await ctx.channel.purge(limit=int(num)+2)
			await ctx.channel.send('{} message(s) supprimé(s)'.format(len(deleted)-2))
		else:
			await ctx.channel.send("T'es pas admin :p")


def setup(client):
	client.add_cog(Administration(client))

'''


	if message.content.startswith(prefix + 'devoir'):
		try:
			matiere = message.content.split("$m")[1:][0].split("$d")[0]
			date = message.content.split("$d")[1:][0].split("$f")[0]
			cat = message.content.split("$f")[1:]

			embed=discord.Embed(title=matiere, url="", description=date, color=0xff0000)
			embed.set_author(name=message.author, url="", icon_url="")
			embed.set_thumbnail(url=dicomat[matiere.replace(" ","")])
		
			for i in range(len(cat)):
				embed.add_field(name="Travail " + str(i+1), value=cat[i], inline=False)
			await message.channel.send(embed=embed)
		except:
			await message.channel.send(str(dicomat.keys()) + "\n$m pour la matière $d pour la date $f devant chauqe travail")
	
	if message.content.startswith(prefix + 'mp clause'):
		i=0
		for item in message.guild.members:
			i+=1
			try:
				await item.send("Acceptez les nouvelles clauses ici si vous ne l'avez pas fait: https://discord.gg/9DTfWc9, <@163696573686087680> pour me répondre.")
			except :
				await message.channel.send("fail à partir de" + item + " " + str(i))
		await message.channel.send("fini")

	if message.content.startswith(prefix + 'mp troll'):
		i=0
		for item in message.guild.members:
			i+=1
			print(item)
			try:
				await item.send(":warning: des faux élèves rejoignent si vous ne connaissez pas une personne dans votre classe contacter moi <@163696573686087680>.")
			except :
				await message.channel.send(item)
		await message.channel.send("fini")

'''