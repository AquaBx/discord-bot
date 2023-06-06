import discord
from discord.ext import commands
import json
import random
import requests
from pack import function
import math

pokemonserv = {}

def percent(num,base,red,force=False):
	percent = int(round(num*red/base,0))
	percenti = int(round(num*100/base,0))
	rest = red-percent
	if force:
		return percent*"▮" + rest*"▯" +  " " + str(percenti) + "%"
	else:
		return percent*"▮" + rest*"▯" +  " " + str(num) + "/" + str(base)


def calstat(stat,iv,niv):
	return (2*stat + 3*iv)*niv/100

def bddpost(type,id,varname,var,post):
	requests.post("https://aquabx.ovh/api/bot_post.php?q=bdd&t="+post, data={'type': type,'id': id,'varname':varname,'var': json.dumps(var)})

class pokémon(commands.Cog):

	def __init__(self, client):
		self.client = client

	
	
	@commands.Cog.listener()
	async def on_message(self,member):
		guild = str(member.guild.id)
		try:
			ctx = requests.get("https://aquabx.ovh/api/bot_post.php?q=bdd").json()["guilds"][guild]["pokemon"]
			channel = self.client.get_channel(int(ctx))

			try:
				pokemonserv[guild][0][0] += 1
			except:
				pokemonserv[guild] = [0,0]
				pokemonserv[guild][0] = [0,random.randint(5,10)]

			if pokemonserv[guild][0][0] == pokemonserv[guild][0][1]:
				pokemon = random.choice(requests.get("https://aquabx.ovh/api/pokemon.php?q=pokemon").json())

				liste=[]
				for sexe,percent in pokemon["sexe"][0].items():
					print(round(percent,0))
					for i in range(round(percent,0)):
						liste.append(sexe)

				random.shuffle(liste)

				pokemon["sexe"] = random.choice(liste)

				shiny1 = random.choice([x for x in range(0,128)])
				shiny2 = random.choice([x for x in range(0,128)])		

				try:				
					xp = random.choice([x for x in range(pokemon["evolution"][1] -15,pokemon["evolution"][1])])**3
				except :
					xp = random.choice([x for x in range(32,50)])**3

				if shiny1 == shiny2:
					pokemon["color"] = "shiny"
				else:
					pokemon["color"] = "normal"

				heal = random.randint(1,31)
				atta = random.randint(1,31)
				defe = random.randint(1,31)
				spat = random.randint(1,31)
				spde = random.randint(1,31)
				spee = random.randint(1,31)
				stot = heal + atta + defe + spat + spde + spee	

				pokemonserv[guild][1] = {"name" : pokemon["name"],"sexe":pokemon["sexe"],"color":pokemon["color"],"type":pokemon["type"],"number":pokemon["number"],"heal":heal,"atta":atta,"defe":defe,"spat":spat,"spde":spde,"spee":spee,"stot":stot,"xp":xp,"base" : pokemon["base"]}

				if pokemonserv[guild][1]["color"] == "shiny":
					img = "https://www.poketools.fr/bundles/ptpoketools/images/pokemon/animated/shiny/"+pokemonserv[guild][1]["number"]+".gif"
				else:
					img = "https://www.poketools.fr/bundles/ptpoketools/images/pokemon/animated/"+pokemonserv[guild][1]["number"]+".gif"

				embed=discord.Embed(title="‌‌A wild pokémon has аppeаred! ", description="Guess the pokémon аnd type +catch <pokémon> to cаtch it!", color=0x0059ff)
				embed.set_thumbnail(url=img)
				embed.add_field(name="Information", value="Sexe : " + pokemon["sexe"] + " Color : " +  pokemon["color"], inline=False)
				await channel.send(embed=embed)
		except:pass

	@commands.command()
	async def catch(self,ctx,pokemon):
		guild = str(ctx.author.guild.id)
		author = str(ctx.author.id)
		if pokemon in pokemonserv[guild][1]["name"]:
			bddpost("users",author,"pokemon",pokemonserv[guild][1],"add")
			await ctx.channel.send("Congratulation, you've catched a" + str(pokemonserv[guild][1]["name"]))
			pokemonserv[guild] = [0,0]
		else:
			await ctx.channel.send("Wrong Pokémon or wrong language")
	
	@commands.command()
	async def types(self,ctx):
		await ctx.channel.send()

	@commands.command()
	async def report(self,ctx):
		guild = str(ctx.author.guild.id)
		author = str(ctx.author.id)
		channel = self.client.get_user(163696573686087680)		
		await channel.send("<@" + author + "> in https://ptb.discordapp.com/channels/" + guild + " reports : " + str(pokemonserv[guild]))
		pokemonserv[guild] = [0,0]

	@commands.command()
	async def pokemon(self,ctx,id=None):
		guild = ctx.author.guild.id
		author = str(ctx.author.id)
		pokemons = requests.get("https://aquabx.ovh/api/bot_post.php?q=bdd").json()["users"][author]["pokemon"]
		
		if id == "last":
			id = -1

		

		if id == None:
			embed=discord.Embed(title="‌‌Your Pokémon list", description="list", color=0x0059ff)
			for pokemon in pokemons:
				embed.add_field(name=pokemon["name"], value="id: "+ str(pokemons.index(pokemon)) +" iv: "+str(pokemon["stot"]/186*100)+"%", inline=False)
			await ctx.channel.send(embed=embed)
		else :
			
			pokemon = pokemons[int(id)]
				
			if pokemon["color"] == "shiny":
				img = "https://www.poketools.fr/bundles/ptpoketools/images/pokemon/animated/shiny/"+pokemon["number"]+".gif"
			else:
				img = "https://www.poketools.fr/bundles/ptpoketools/images/pokemon/animated/"+pokemon["number"]+".gif"

			embed=discord.Embed(title="‌‌Your Pokémon "+ str(pokemon["name"]), description="Stats", color=0x0059ff)
			embed.set_thumbnail(url=img)

			niv = math.floor(round(pokemon["xp"]**(1/3),5))

			embed.add_field(name="Information", value="Sexe : " + pokemon["sexe"] + " Color : " +  pokemon["color"] + " Level : " +  str(niv), inline=False)
			
			req = requests.get("http://aquabx.ovh/api/pokemon.php?q=types").json()

			types = " ".join([req[i] for i in pokemon["type"]])

			embed.add_field(name="Information", value="Types : " + types + " Number : " +  str(pokemon["number"]), inline=False)

			hp = calstat(pokemon["base"]["hp"],pokemon["heal"],niv) + niv
			atta = calstat(pokemon["base"]["atk"],pokemon["atta"],niv)
			defe = calstat(pokemon["base"]["def"],pokemon["defe"],niv)
			spat = calstat(pokemon["base"]["spa"],pokemon["spat"],niv)
			spde = calstat(pokemon["base"]["spd"],pokemon["spde"],niv)
			spee = calstat(pokemon["base"]["spe"],pokemon["spee"],niv)

			embed.add_field(name="HP : " + str(hp), value=percent(pokemon["heal"],31,24), inline=False)
			embed.add_field(name="Attack : " + str(atta), value=percent(pokemon["atta"],31,24), inline=False)
			embed.add_field(name="Defense : " + str(defe), value=percent(pokemon["defe"],31,24), inline=False)
	
			embed.add_field(name="Special Attack : " + str(spat), value=percent(pokemon["spat"],31,24), inline=False)
			embed.add_field(name="Special Defense : " + str(spde), value=percent(pokemon["spde"],31,24), inline=False)
			embed.add_field(name="Speed : " + str(spee), value=percent(pokemon["spee"],31,24), inline=False)
	
			embed.add_field(name="Total", value=percent(pokemon["stot"],186,24,True), inline=False)
	
			await ctx.channel.send(embed=embed)
			

def setup(client):
	client.add_cog(pokémon(client))