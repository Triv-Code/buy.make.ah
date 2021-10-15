import requests
import json
import math
import pprint
# ? What are the benefits / differences of loading this way? 
# data = requests.get("https://us.api.blizzard.com/data/wow/connected-realm/11/auctions?namespace=dynamic-us&locale=en_US&access_token=US7ojuxwdmAtxfikgsR4Zu4b68IM8rd1li").json()
# url = 'https://us.api.blizzard.com/data/wow/connected-realm/11/auctions?namespace=dynamic-us&locale=en_US&access_token=US7ojuxwdmAtxfikgsR4Zu4b68IM8rd1li'
# r = requests.get(url)
# data = json.loads(r.text)

herbs = [
    {
        "name": "Marrowroot", 
        "id": 168589,
        "img": "https://render-us.worldofwarcraft.com/icons/56/inv_misc_herb_marrowroot.jpg",
        "cost": 234567,
    },{
        "name": "Rising Glory", 
        "id": 168586,
        "img": "https://render-us.worldofwarcraft.com/icons/56/inv_misc_herb_risingglory.jpg",
        "cost": 314567,
    },{
        "name": "Vigil's Torch", 
        "id": 170554,
        "img": "https://render-us.worldofwarcraft.com/icons/56/inv_misc_herb_ardenweald.jpg",
        "cost": 354567,
    },{
        "name": "Widowbloom", 
        "id": 168583,
        "img": "https://render-us.worldofwarcraft.com/icons/56/inv_misc_herb_bloodcup.jpg",
        "cost": 349567,
    },{
        "name": "Death Blossom", 
        "id": 169701,
        "img": "https://render-us.worldofwarcraft.com/icons/56/inv_misc_herb_deathblossom.jpg",
        "cost": 304567,
    },{
        "name": "Nightshade", 
        "id": 171315,
        "img": "https://render-us.worldofwarcraft.com/icons/56/inv_misc_herb_nightshade.jpg",
        "cost": 780431,
    },]

potions = [
    {
        "name": "Flask of Power",
        "id": 171276,
        "img": "https://render-us.worldofwarcraft.com/icons/56/inv_alchemy_90_flask_green.jpg",
        "cost": 8450891,
        "craft_cost": herbs[5]["cost"] * 3 + herbs[1]["cost"] * 4 + herbs[0]["cost"] * 4 +herbs[3]["cost"] * 4 + herbs[2]["cost"] * 4,
    },{
        "name": "Phantom Fire",
        "id": 171349,
        "img": "https://render-us.worldofwarcraft.com/icons/56/inv_alchemy_90_combat1_green.jpg",
        "cost": 1780431,
        "craft_cost": herbs[0]["cost"] * 3 + herbs[1]["cost"] * 3,
    },{
        "name": "Empowered Exorcisms",
        "id": 171352,
        "img": "https://render-us.worldofwarcraft.com/icons/56/inv_alchemy_90_combat1_pink.jpg",
        "cost": 780431,
        "craft_cost": herbs[0]["cost"] * 3 + herbs[3]["cost"] * 3,
    },{
        "name": "Deathly Fixation",
        "id": 171351,
        "img": "https://render-us.worldofwarcraft.com/icons/56/inv_alchemy_90_combat1_yellow.jpg",
        "cost": 650431,
        "craft_cost": herbs[3]["cost"] * 3 + herbs[2]["cost"] * 3,
    },{
        "name": "Spectral Agility",
        "id": 171270,
        "img": "https://render-us.worldofwarcraft.com/icons/56/inv_alchemy_90_combat2_green.jpg",
        "cost": 240431,
        "craft_cost": herbs[3]["cost"] * 5,
    },{
        "name": "Spectral Strength",
        "id": 171275,
        "img": "https://render-us.worldofwarcraft.com/icons/56/inv_alchemy_90_combat2_yellow.jpg",
        "cost": 330431,
        "craft_cost": herbs[1]["cost"] * 5,
    },{
        "name": "Spectral Intellect",
        "id": 171273,
        "img": "https://render-us.worldofwarcraft.com/icons/56/inv_alchemy_90_combat2_purple.jpg",
        "cost": 980431,
        "craft_cost": herbs[0]["cost"] * 5,
    },{
        "name": "Hidden Spirit",
        "id": 171266,
        "img": "https://render-us.worldofwarcraft.com/icons/56/inv_alchemy_90_utility_red.jpg",
        "cost": 120431,
        "craft_cost": herbs[4]["cost"] * 2 + herbs[1]["cost"] * 3,
    },]

# def ah_filter(potid):
#     for i in range(0, len(potions)):
#         if (potid == potions[1]["id"]):
#             print("It works!")
#         else:
#             print("Whut?")

# ah_filter(data["auctions"])
# print(data["auctions"])
# print(len(data["auctions"]))
# ? Could this be a Class
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

def comp():
    for i in range(len(potions)):
        name = potions[i]["name"]
        if (potions[i]["craft_cost"] > potions[i]["cost"]):
            x = potions[i]["craft_cost"] - potions[i]["cost"]
            print(f"{name}: Buy it! You'll save {coin(x)} per potion.")
        elif (potions[i]["craft_cost"] < potions[i]["cost"]):
            x = potions[i]["cost"] - potions[i]["craft_cost"]
            print(f"{name}: Craft it! You'll save {coin(x)} per potion.")
        elif (potions[i]["craft_cost"] == potions[i]["cost"]):
            print("It doesn't matter...")

print(comp())