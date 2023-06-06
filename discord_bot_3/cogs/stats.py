import discord
from discord.ext import commands
import json
from pack import function
import requests
import json

class Statistiques(commands.Cog):

	def __init__(self, client):
		self.client = client

	@commands.command()
	async def stats(self,ctx,game,platform,*,player):	
		reponseapi = function.call_api(game,platform,player)

		#messagee = [description,url_thumb,[[name1,value1],[name2,value2],[name3,value3]]]

		if game == "r6":
			mmr = reponseapi["data"]["stats"][0]["value"]
			season = reponseapi["data"]["stats"][0]["metadata"]["categoryName"]
			try:
				rank = reponseapi["data"]["stats"][0]["metadata"]["iconUrl"]
			except:
				rank =""
			kill = reponseapi["data"]["stats"][2]["value"]
			death = reponseapi["data"]["stats"][3]["value"]	
			win = reponseapi["data"]["stats"][7]["value"]
			lose = reponseapi["data"]["stats"][6]["value"]
			kd = round(kill/death,3)
			wl = round(win/lose,3)

			messagee = ["Rainbow Six Siege"+" "+season,rank,[["MMR",mmr],["Victoires/Défaites","Victoires: " + str(win) + "\nDéfaites: " + str(lose) + "\nRatio: " + str(wl)],["Kills/Deaths","Kills: " + str(kill) + "\nDeaths: " + str(death) + "\nRatio: " + str(kd)]]]

		elif game == "fn":
			top1 = reponseapi["stats"]["p2"]["top1"]["valueInt"]
			kill1 = reponseapi["stats"]["p2"]["kills"]["valueInt"]
			match1 = reponseapi["stats"]["p2"]["matches"]["valueInt"]
			kd1 = round(kill1/match1,3)
			wl1 = round(top1/match1,3)

			top2 = reponseapi["stats"]["p10"]["top1"]["valueInt"]
			kill2 = reponseapi["stats"]["p10"]["kills"]["valueInt"]
			match2 = reponseapi["stats"]["p10"]["matches"]["valueInt"]
			kd2 = round(kill2/match2,3)
			wl2 = round(top2/match2,3)

			top3 = reponseapi["stats"]["p9"]["top1"]["valueInt"]
			kill3 = reponseapi["stats"]["p9"]["kills"]["valueInt"]
			match3 = reponseapi["stats"]["p9"]["matches"]["valueInt"]
			kd3 = round(kill3/match3,3)
			wl3 = round(top3/match3,3)

			messagee = ["Fortnite","",[["Solo","Matches: " + str(match1) + "\nVitoires: " + str(top1) + "\nRatio: " + str(wl1) + "\nKills: " + str(kill1) + "\nRatio: " + str(kd1)],["Duo","Matches: " + str(match2) + "\nVitoires: " + str(top2) + "\nRatio: " + str(wl2)  + "\nKills: " + str(kill2) + "\nRatio: " + str(kd2)],["Squad","Matches: " + str(match3) + "\nVitoires: " + str(top3) + "\nRatio: " + str(wl3) + "\nKills: " + str(kill3) + "\nRatio: " + str(kd3)]]]
		elif game == "cs":
			api_token = '56ce7a91-574a-4c4b-a363-750b2d121912'
			api_url_base = 'https://public-api.tracker.gg/v2/csgo/standard/search/?platform=steam&query='+player
			headers = {'Content-Type': 'application/json','TRN-Api-Key': api_token}
			id = requests.get(api_url_base,headers = headers).json()["data"][0]["platformUserIdentifier"]
			reponseapi = function.call_api("cs","pc",id)
			try:
				print(reponseapi)
				rank = reponseapi["data"]["segments"][0]["stats"]["score"]["rank"]

				kill = reponseapi["data"]["segments"][0]["stats"]["kills"]["value"]
				death = reponseapi["data"]["segments"][0]["stats"]["deaths"]["value"]

				damage = reponseapi["data"]["segments"][0]["stats"]["damage"]["value"]

				headshot = reponseapi["data"]["segments"][0]["stats"]["headshots"]["value"]
				shotsfired = reponseapi["data"]["segments"][0]["stats"]["shotsFired"]["value"]
				shotshit = reponseapi["data"]["segments"][0]["stats"]["shotsHit"]["value"]

				mvp = reponseapi["data"]["segments"][0]["stats"]["mvp"]["value"]

				win = reponseapi["data"]["segments"][0]["stats"]["wins"]["value"]
				losses = reponseapi["data"]["segments"][0]["stats"]["losses"]["value"]

				kd = round(kill/death,3)
				wl = round(win/losses,3)

				accuracy = round(shotshit/shotsfired,3)
				accuracyh = round(headshot/shotshit,3)

				messagee = ["CS:GO","",[["Rank",rank],["Victoires/Défaites","Victoires: " + str(win) + "\nDéfaites: " + str(losses) + "\nRatio: " + str(wl)],["Kills/Deaths","Kills: " + str(kill) + "\nDeaths: " + str(death) + "\nRatio: " + str(kd)],["Précision","Dégats: " + str(damage) + "\nPrécision: " + str(accuracy) + "\nPrécision headshot: " + str(accuracyh)]]]
			except:
				reponseapi["errors"][0]["message"]



		embed=discord.Embed(title=player + " sur " + platform, url="", description=messagee[0], color=0xff0000)
		embed.set_thumbnail(url=messagee[1])
		for element in messagee[2]:
			embed.add_field(name=element[0], value=element[1], inline=True)
		await ctx.channel.send(embed=embed)

def setup(client):
	client.add_cog(Statistiques(client))