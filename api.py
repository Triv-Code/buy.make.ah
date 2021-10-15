import requests
import json
import math
#           !!!! What are the benefits / differences of loading this way? 
# data = requests.get("https://us.api.blizzard.com/data/wow/connected-realm/11/auctions?namespace=dynamic-us&locale=en_US&access_token=US7ojuxwdmAtxfikgsR4Zu4b68IM8rd1li").json()
# url = 'https://us.api.blizzard.com/data/wow/connected-realm/11/auctions?namespace=dynamic-us&locale=en_US&access_token=US7ojuxwdmAtxfikgsR4Zu4b68IM8rd1li'
# r = requests.get(url)
# data = json.loads(r.text)

herbs = [
    {
        "name": "Marrowroot", 
        "id": 168589,
        "img": "https://render-us.worldofwarcraft.com/icons/56/inv_misc_herb_marrowroot.jpg",
    },{
        "name": "Rising Glory", 
        "id": 168586,
        "img": "https://render-us.worldofwarcraft.com/icons/56/inv_misc_herb_risingglory.jpg",
    },{
        "name": "Vigil's Torch", 
        "id": 170554,
        "img": "https://render-us.worldofwarcraft.com/icons/56/inv_misc_herb_ardenweald.jpg",
    },{
        "name": "Widowbloom", 
        "id": 168583,
        "img": "https://render-us.worldofwarcraft.com/icons/56/inv_misc_herb_bloodcup.jpg",
    },{
        "name": "Death Blossom", 
        "id": 169701,
        "img": "https://render-us.worldofwarcraft.com/icons/56/inv_misc_herb_deathblossom.jpg",
    },{
        "name": "Nightshade", 
        "id": 171315,
        "img": "https://render-us.worldofwarcraft.com/icons/56/inv_misc_herb_nightshade.jpg",
    },]

potions = [
    {
        "name": "Flask of Power",
        "id": 171276,
        "img": "https://render-us.worldofwarcraft.com/icons/56/inv_alchemy_90_flask_green.jpg",
        #  craftCost: nightCost * 3 + risingCost * 4 + marrowCost * 4 + widowCost * 4 + vigilCost * 4,
    },{
        "name": "Phantom Fire",
        "id": 171349,
        "img": "https://render-us.worldofwarcraft.com/icons/56/inv_alchemy_90_combat1_green.jpg",
        # craftCost: marrowCost * 3 + risingCost * 3,
    },{
        "name": "Empowered Exorcisms",
        "id": 171352,
        "img": "https://render-us.worldofwarcraft.com/icons/56/inv_alchemy_90_combat1_pink.jpg",
        # craftCost: marrowCost * 3 + widowCost * 3,
    },{
        "name": "Deathly Fixation",
        "id": 171351,
        "img": "https://render-us.worldofwarcraft.com/icons/56/inv_alchemy_90_combat1_yellow.jpg",
        # craftCost:  widowCost * 3 + vigilCost * 3,
    },{
        "name": "Spectral Agility",
        "id": 171270,
        "img": "https://render-us.worldofwarcraft.com/icons/56/inv_alchemy_90_combat2_green.jpg",
        # craftCost:  widowCost * 5,
    },{
        "name": "Spectral Strength",
        "id": 171275,
        "img": "https://render-us.worldofwarcraft.com/icons/56/inv_alchemy_90_combat2_yellow.jpg",
        # craftCost: risingCost * 5,
    },{
        "name": "Spectral Intellect",
        "id": 171273,
        "img": "https://render-us.worldofwarcraft.com/icons/56/inv_alchemy_90_combat2_purple.jpg",
        # craftCost: marrowCost * 5,
    },{
        "name": "Hidden Spirit",
        "id": 171266,
        "img": "https://render-us.worldofwarcraft.com/icons/56/inv_alchemy_90_utility_red.jpg",
        # craftCost: deathCost * 2 + risingCost * 3,
    },]

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
    x = f"{into_gold(num)} Gold, {into_silver(num)} Silver, {into_copper(num)} Copper"
    return x

print(coin(1234567))