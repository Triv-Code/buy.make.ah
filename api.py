import requests
import json
import math
#           !!!! What are the benefits / differences of loading this way? 
# data = requests.get("https://us.api.blizzard.com/data/wow/connected-realm/11/auctions?namespace=dynamic-us&locale=en_US&access_token=US7ojuxwdmAtxfikgsR4Zu4b68IM8rd1li").json()
# url = 'https://us.api.blizzard.com/data/wow/connected-realm/11/auctions?namespace=dynamic-us&locale=en_US&access_token=US7ojuxwdmAtxfikgsR4Zu4b68IM8rd1li'
# r = requests.get(url)
# data = json.loads(r.text)

potions = [
    {
        "name": "Flask of Power",
        "id": 171276,
        "img": "https://render-us.worldofwarcraft.com/icons/56/inv_alchemy_90_flask_green.jpg",
    },{
        "name": "Phantom Fire",
        "id": 171349,
        "img": "https://render-us.worldofwarcraft.com/icons/56/inv_alchemy_90_combat1_green.jpg",
    }]


def ah_filter(potid):
    for i in range(0, len(potions)):
        if (potid == potions[1]["id"]):
            print("It works!")
        else:
            print("Whut?")

# ah_filter(data["auctions"])
# print(data["auctions"])
# print(len(data["auctions"]))

def into_gold(num):
    gold = num / 10000
    gold = math.floor(gold)
    return gold

def into_silver(num):
    num = str(num)
    num = num[-4:-2] 
    return num

def into_copper(num):
    num = str(num)
    num = num[-2:]
    return num

def coin(num): # Return into a Dict?
    x = f"{into_gold(num)} Gold, {into_silver(num)} Silver, {into_copper(num)} Copper, "
    return x

print(coin(1234567))
