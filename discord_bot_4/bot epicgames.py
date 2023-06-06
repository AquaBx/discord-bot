import discord
import requests


guild_n = 829723470497185863
user_n = 829723526273564692
guilds = {}
users = {}
bdd = {"guilds":{},"users":{}}

async def get_bdd(self,liste_id):
	liste = await self.get_guild(603636752569335839).get_channel(liste_id).history(limit=200000).flatten()
	liste = {mess.content.split("\"")[1]:mess.id for mess in liste if mess.content!=""}
	return liste

class MyClient(discord.Client):
	async def on_ready(self):
		print(await get_bdd(self,guild_n))
	async def on_message(self,message):
		if message.content.startswith('!send'):
			req = requests.get("https://store-site-backend-static-ipv4.ak.epicgames.com/freeGamesPromotions").json()["data"]["Catalog"]["searchStore"]["elements"]
			for item in req :
				if item["promotions"] != None and item["promotions"]["promotionalOffers"] != []:
					embed = discord.Embed(title=item["title"], description="is free on EpicGames", url="https://www.epicgames.com/store/p" + item["productSlug"])
					embed.add_field(name="Start Date", value=item["promotions"]["promotionalOffers"][0]["promotionalOffers"][0]["startDate"])
					embed.add_field(name="End Date", value=item["promotions"]["promotionalOffers"][0]["promotionalOffers"][0]["endDate"])
					for img in item["keyImages"] :
						if img["type"] == "OfferImageWide":
							embed.set_image(url=img["url"])
							break
					await message.channel.send(embed=embed)

MyClient().run('ODI3NDU5MDA2NTMyMTU3NDQw.YGbVQA.27I-3uzrO59ncryzVF3YAO5-qmo')