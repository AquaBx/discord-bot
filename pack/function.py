import requests
import json
import random
import os
from pack import function

def call_api(game, platform,player):
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

def check_sadmin(id):
	role = [163696573686087680]
	if id in role:
		return True
	else :
		return False

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
	requests.post("https://aquabx.ovh/api/bot_bdd.php?q=bdd&t="+post, data={'type': type,'id': id,'varname':varname,'var': json.dumps(var)})