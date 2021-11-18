import requests
import json
import math

# ? What are the benefits / differences of loading this way? 
# data = requests.get("https://us.api.blizzard.com/data/wow/connected-realm/11/auctions?namespace=dynamic-us&locale=en_US&access_token=USO3eQDmxPgccomj8nS74ZsmlivAe735Mk").json()
url = 'https://us.api.blizzard.com/data/wow/connected-realm/11/auctions?namespace=dynamic-us&locale=en_US&access_token=USHQmRdZs5C34wd3xXcb20K5qQqObBJ2qI'
r = requests.get(url)
data = json.loads(r.text)

herbs = [
    {
        "name": "Marrowroot", 
        "id": 168589,
        "img": "https://render-us.worldofwarcraft.com/icons/56/inv_misc_herb_marrowroot.jpg",
        # "cost": 234567,
    },{
        "name": "Rising Glory", 
        "id": 168586,
        "img": "https://render-us.worldofwarcraft.com/icons/56/inv_misc_herb_risingglory.jpg",
        # "cost": 314567,
    },{
        "name": "Vigil's Torch", 
        "id": 170554,
        "img": "https://render-us.worldofwarcraft.com/icons/56/inv_misc_herb_ardenweald.jpg",
        # "cost": 354567,
    },{
        "name": "Widowbloom", 
        "id": 168583,
        "img": "https://render-us.worldofwarcraft.com/icons/56/inv_misc_herb_bloodcup.jpg",
        # "cost": 349567,
    },{
        "name": "Death Blossom", 
        "id": 169701,
        "img": "https://render-us.worldofwarcraft.com/icons/56/inv_misc_herb_deathblossom.jpg",
        # "cost": 304567,
    },{
        "name": "Nightshade", 
        "id": 171315,
        "img": "https://render-us.worldofwarcraft.com/icons/56/inv_misc_herb_nightshade.jpg",
        # "cost": 780431,
    },]

# Function Filers AH & Updates herbs w/ cost
def ah_herb_filter(num):
    prices = []
    for auction in data["auctions"]:
        if (auction["item"]["id"] == herbs[num]["id"]):
            prices.append(auction["unit_price"])
    herbs[num]["cost"] = min(prices)

# # Loops herbs Dictionary to call ah_herb_filter for each potion. 
for i in range(0, len(herbs)):
    ah_herb_filter(i)    


potions = [
    {
        "name": "Flask of Power",
        "id": 171276,
        "img": "https://render-us.worldofwarcraft.com/icons/56/inv_alchemy_90_flask_green.jpg",
        "craft_cost": herbs[5]["cost"] * 3 + herbs[1]["cost"] * 4 + herbs[0]["cost"] * 4 +herbs[3]["cost"] * 4 + herbs[2]["cost"] * 4,
    },{
        "name": "Phantom Fire",
        "id": 171349,
        "img": "https://render-us.worldofwarcraft.com/icons/56/inv_alchemy_90_combat1_green.jpg",
        "craft_cost": herbs[0]["cost"] * 3 + herbs[1]["cost"] * 3,
    },{
        "name": "Empowered Exorcisms",
        "id": 171352,
        "img": "https://render-us.worldofwarcraft.com/icons/56/inv_alchemy_90_combat1_pink.jpg",
        "craft_cost": herbs[0]["cost"] * 3 + herbs[3]["cost"] * 3,
    },{
        "name": "Deathly Fixation",
        "id": 171351,
        "img": "https://render-us.worldofwarcraft.com/icons/56/inv_alchemy_90_combat1_yellow.jpg",
        "craft_cost": herbs[3]["cost"] * 3 + herbs[2]["cost"] * 3,
    },{
        "name": "Spectral Agility",
        "id": 171270,
        "img": "https://render-us.worldofwarcraft.com/icons/56/inv_alchemy_90_combat2_green.jpg",
        "craft_cost": herbs[3]["cost"] * 5,
    },{
        "name": "Spectral Strength",
        "id": 171275,
        "img": "https://render-us.worldofwarcraft.com/icons/56/inv_alchemy_90_combat2_yellow.jpg",
        "craft_cost": herbs[1]["cost"] * 5,
    },{
        "name": "Spectral Intellect",
        "id": 171273,
        "img": "https://render-us.worldofwarcraft.com/icons/56/inv_alchemy_90_combat2_purple.jpg",
        "craft_cost": herbs[0]["cost"] * 5,
    },{
        "name": "Hidden Spirit",
        "id": 171266,
        "img": "https://render-us.worldofwarcraft.com/icons/56/inv_alchemy_90_utility_red.jpg",
        "craft_cost": herbs[4]["cost"] * 2 + herbs[1]["cost"] * 3,
    },]

# Function Filers AH & Updates potions w/ buy_cost
def ah_pot_filter(num):
    prices = []
    for auction in data["auctions"]:
        if (auction["item"]["id"] == potions[num]["id"]):
            prices.append(auction["unit_price"])
    potions[num]["buy_cost"] = min(prices)

# Loops Potions Dictionary to call ah_pot_filter for each potion. 
for i in range(0, len(potions)):
    ah_pot_filter(i)

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

def coin(num):
    x = f"{into_gold(num)} Gold, {into_silver(num)} Silver, {into_copper(num)} Copper"
    return x

def comp():
    for i in range(len(potions)):
        name = potions[i]["name"]
        if (potions[i]["craft_cost"] > potions[i]["buy_cost"]):
            x = potions[i]["craft_cost"] - potions[i]["buy_cost"]
            print(f"{name}: Buy it! You'll save {coin(x)} per potion.")
        elif (potions[i]["craft_cost"] < potions[i]["buy_cost"]):
            x = potions[i]["buy_cost"] - potions[i]["craft_cost"]
            print(f"{name}: Craft it! You'll save {coin(x)} per potion.")
        elif (potions[i]["craft_cost"] == potions[i]["cost"]):
            print("It doesn't matter...")

print(comp())