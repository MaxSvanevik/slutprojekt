import pandas as pd
import numpy as np

pd.set_option("display.max_rows", None)
poke = pd.read_csv("Pokemon2.csv")
allTypes = [
    "Normal", "Fire", "Water", "Electric", "Grass", "Ice", 
    "Fighting", "Poison", "Ground", "Flying", "Bug", "Dark",
    "Rock", "Ghost", "Dragon", "Psychic", "Steel", "Fairy"
]
categories = ("Total","HP","Attack","Defense","Sp. Atk","Sp. Def","Speed","Generation")
types = [np.nan]

x = "."
while x != "":
    x = input("vilken typ vill du lägga till?\nskriv help för att få en lista av alla typer\n").lower().capitalize().strip()
    if x == "Help":
        print(allTypes)
    else:
        types.append(x)


poke = poke[poke["Type1"].isin(types)]
poke = poke[poke["Type2"].isin(types)]

while True:

    x = input(f"vill du sortera efter något annat?\n det går att sortera efter {categories}\n")

    if x == "":
        break

    try:
        x = int(x)
        x = categories[x-1]
    except:
        pass

    
    if x in categories:

        y = input("med hur mycket?")
        while type(y) != int:
            try:
                y = int(y)
            except:
                y = input("ange ett nummer!!!!!\n")


        z = input("större eller mindre?").strip

        if z == "större":
            poke = poke[poke[x] >= y]

        elif z == "mindre":
            poke = poke[poke[x] <= y]
        
        else:
            poke = poke[poke[x] == y]

if poke.empty == True:
    print("tyvärr fanns det inga som passade dom kriterierna")
else:
    print(f"detta var alla pokemons som passar in med dina krav\n{poke}")
