import discord
from discord.ext import commands
import os
import random
from pack import function
import requests
import json
from discord.voice_client import VoiceClient
import asyncio
import youtube_dl


def downlmusc(req):
	with youtube_dl.YoutubeDL() as ydl:
		req = ydl.extract_info(req, download=False)
	return {"id":req["id"],"link":"https://youtube.com/watch?v=" + req["id"],"thumbnail":req["thumbnail"],"time":req["duration"],"title":req["title"],"author":req["creator"],"channel":"https://youtube.com/channel/" +req["channel_id"],"url":str(req["formats"][0]["url"])}

def bddpost(type,id,varname,var,post):
	requests.post("https://aquabx.ovh/api/bot_post.php?q=bdd&t="+post, data={'type': type,'id': id,'varname':varname,'var': json.dumps(var)})

queue = {"skip":0}


class Musique(commands.Cog):
	def __init__(self, client):
		self.client = client

	@commands.command()
	async def music(self, ctx, id):
		if(function.check_admin(ctx)):
			channel = self.client.get_channel(int(id))

			msg = await channel.send("Music")
			await msg.add_reaction('⏯️')
			await msg.add_reaction('▶')
			await msg.add_reaction('⏹')		
			await msg.add_reaction('⏭️')
			guild = str(ctx.channel.guild.id)
			bddpost("guilds",guild,"music",[str(id),str(msg.id)],"rep")

		else:
			await ctx.channel.send("T'es pas admin :p")

	@commands.Cog.listener()
	async def on_reaction_add(self, reaction, member):
		try:
			ctx = reaction.message
			guild = str(reaction.message.guild.id)
			music = requests.get("https://aquabx.ovh/api/bot_post.php?q=bdd").json()["guilds"][guild]["music"]
			if [str(reaction.message.channel.id), str(reaction.message.id)] == music and member.id != 689151880370454610:		
				await ctx.remove_reaction(reaction,member)
				###############################################################

				if str(reaction.emoji) == "⏯️":
					for serv in self.client.voice_clients:
						if member.voice.channel.id == serv.channel.id:					
							if serv.is_playing():
								serv.pause()
							else:
								serv.resume()

				###############################################################

				elif str(reaction.emoji) == "▶":
					msg = ctx.channel.last_message
					query = msg.content

					await msg.delete()

					for serv in self.client.voice_clients:
						if member.voice.channel.id == serv.channel.id:
							servi = serv
					try:
						print(servi)
					except:
						chan = member.voice.channel
						servi = await chan.connect()
						queue[guild] = []

					queue[guild].append(downlmusc(query))

					embed=discord.Embed()
					embed=discord.Embed(title="Playlist")
					embed.clear_fields()
					mus = queue[guild][0]
					for musics in queue[guild]:
						embed.add_field(name=queue[guild].index(musics), value=musics["author"] + " : " + musics["title"], inline=False)
					embed.set_image(url=mus["thumbnail"])
					await ctx.edit(embed=embed)

					if not(servi.is_playing()) and len(queue[guild]) == 1:
						while len(queue[guild]) != 0:
							queue["skip"]=0
							mus = queue[guild][0]

							durat = mus["time"]

							music = mus["url"]

							embed=discord.Embed()
							embed=discord.Embed(title="Playlist")

							embed.clear_fields()
							for musics in queue[guild]:
								embed.add_field(name=queue[guild].index(musics), value=musics["author"] + " : " + musics["title"], inline=False)
							embed.set_image(url=mus["thumbnail"])
							await ctx.edit(embed=embed)

							source = discord.FFmpegPCMAudio(music)
							await servi.play(source)

							queue[guild].pop(0)
						await servi.disconnect()

				###############################################################

				elif str(reaction.emoji) == "⏹":				
					for serv in self.client.voice_clients:
						if member.voice.channel.id == serv.channel.id:
							queue[guild] = []
							serv.stop()
							await serv.disconnect()

				elif str(reaction.emoji) == "⏭️":
					for serv in self.client.voice_clients:
						if member.voice.channel.id == serv.channel.id:
							queue[guild].pop(0)

							mus = queue[guild][0]		
							music = os.popen('youtube-dl -i -g '+mus["link"]).read().split("\n")[1]

							embed=discord.Embed()
							embed=discord.Embed(title="Playlist")

							embed.clear_fields()
							for musics in queue[guild]:
								embed.add_field(name=queue[guild].index(musics), value=musics["author"] + " : " + musics["title"], inline=False)
							embed.set_image(url=mus["thumbnail"])
							await ctx.edit(embed=embed)

							serv.source = discord.FFmpegPCMAudio(music)
		except:pass

	@commands.command(pass_content=True)
	async def live(self,ctx,url):
		if "youtu" in url:
			req = requests.get(url).text.replace("\\","").replace("},","#aquabx12").replace(",	{","#aquabx12").replace("],","#aquabx12").replace("[,","#aquabx12").split	("#aquabx12")
			vir = json.loads("{" + [x for x in req if "m3u8" in x][0] + "}")
			req = requests.get(vir["hlsManifestUrl"]).text.split("#")
			url = "https:"+[url for url in req if "x144" in url][0].split("https:")[-1]
		chan = ctx.author.voice.channel
		servi = await chan.connect()
		await ctx.channel.send(url)
		servi.play(discord.FFmpegPCMAudio(str(url)))

def setup(client):
	client.add_cog(Musique(client))
