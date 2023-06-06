import discord
from discord.ext import commands
import json
import requests

class Exemple(commands.Cog):

	def __init__(self, client):
		self.client = client
	

	"""@commands.command()
	async def status(self,ctx):
		
		
	import discord
from discord.ext import commands
import json
from pack import function

react = []

class Event(commands.Cog):

	def __init__(self, client):
		self.client = client

	@commands.command()
	async def react(self, ctx, id):

		channel = self.client.get_channel(int(id))

		await channel.send("Music")
		await msg.add_reaction('⏸')
		await msg.add_reaction('⏹')
		await msg.add_reaction('▶')
		await msg.add_reaction('⏩')


	@commands.Cog.listener()
	async def on_reaction_add(self, reaction, member):
		if [reaction.message.guild.id,reaction.message.channel.id,reaction.message.id] in react and member.id != 689151880370454610:
			ctx = reaction.message



	@commands.Cog.listener()
	async def on_reaction_add(self, reaction, member):
		if [reaction.message.guild.id,reaction.message.channel.id,reaction.message.id] in react and member.id != 689151880370454610:
			ctx = reaction.message
			await ctx.channel.send(str([reaction.message.guild.id,reaction.message.channel.id,reaction.message.id]))
			await ctx.channel.send("```" + str(reaction) + str(member.id) + "```")
			await ctx.remove_reaction(reaction,member)


def setup(client):
	client.add_cog(Event(client))	
		
		
		
		
		"""
	
	@commands.Cog.listener()
	async def on_guild_join(self, _):
		guild = str(len(self.client.guilds))
		await self.client.change_presence(status=discord.Status.online, activity=discord.Game("+help " + guild + " servers"))

	@commands.Cog.listener()
	async def on_guild_remove(self, _):
		guild = str(len(self.client.guilds))
		await self.client.change_presence(status=discord.Status.online, activity=discord.Game("+help " + guild + " servers"))

	@commands.Cog.listener()
	async def on_ready(self):
		print('Bot is up')

	@commands.Cog.listener()
	async def on_member_join(self,member):
		welc = requests.get("https://aquabx.ovh/api/bot_post.php?q=bdd")
		guild = str(member.guild.id)
		try:
			channel = self.client.get_channel(int(welc["guilds"][guild]["welc"][0]))
			await channel.send(welc["guilds"][guild]["welc"][1].replace("<@>", "<@"+str(member.id)+">"))
		except: pass
		try:
			bot= [member.bot for member in member.guild.members]

			channel = self.client.get_channel(int(welc["guilds"][guild]["chann"][0]))
			await channel.edit(name="Membres: " + str(bot.count(False)))

			channel = self.client.get_channel(int(welc["guilds"][guild]["chann"][1]))
			await channel.edit(name="Bots: " + str(bot.count(True)))
		except: pass

	@commands.Cog.listener()
	async def on_member_remove(self,member):
		welc = requests.get("https://aquabx.ovh/api/bot_post.php?q=bdd")
		guild = str(member.guild.id)
		try:
			bot= [member.bot for member in member.guild.members]

			channel = self.client.get_channel(int(welc["guilds"][guild]["chann"][0]))
			await channel.edit(name="Membres: " + str(bot.count(False)))

			channel = self.client.get_channel(int(welc["guilds"][guild]["chann"][1]))
			await channel.edit(name="Bots: " + str(bot.count(True)))
		except: pass

def setup(client):
	client.add_cog(Exemple(client))















































'''
def call_api(game, player, platform):
	api_token = '56ce7a91-574a-4c4b-a363-750b2d121912'
	url = {"r6":"https://r6.tracker.network/api/v1/standard/profile/4/","fn":"https://api.fortnitetracker.com/v1/profile/"+platform+"/","cs":"https://public-api.tracker.gg/v2/csgo/standard/profile/steam/","lol":""}
	api_url_base = url[game]+player
	headers = {'Content-Type': 'application/json','TRN-Api-Key': api_token}
	return requests.get(api_url_base,headers = headers).json()

def check_admin(ctx):
	role = [role.permissions.administrator for role in ctx.author.roles]
	if True in role:
		return True
	else :
		return False


@client.event
async def on_message(message):
	

#############################################################################
	
	if message.content.startswith(prefix + 'help'):
		embed=discord.Embed(title="Help", description="Command Help")
		embed.add_field(name="Statistiques : ``stats jeu platform pseudo``", value="jeu : ``fn`` ``cs`` ``r6``  platform : ``pc`` ``xbl`` ``psn`` ", inline=False)
		embed.add_field(name="Blague : ``blague``", value="Envoie une blague au hasard", inline=False)
		embed.add_field(name="Welcome : ``welcome channel-id message``", value=" Vous pouvez mettre ``<@>`` pour que le pseudo soit mis", inline=False)
		await message.channel.send(embed=embed)	

	if message.content.startswith(prefix + 'stats'):


#############################################################################

	if message.content.startswith(prefix + 'blague'):

		

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
