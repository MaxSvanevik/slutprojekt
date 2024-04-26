import pandas as pd

pd.set_option("display.max_rows", None)
poke = pd.read_csv("Pokemon2.csv")
allTypes = [
    "Normal", "Fire", "Water", "Electric", "Grass", "Ice", 
    "Fighting", "Poison", "Ground", "Flying", "Bug", "Dark",
    "Rock", "Ghost", "Dragon", "Psychic", "Steel", "Fairy"
]
types = []

x = "."
while x != "":
    x = input("vilken typ vill du lägga till?\nskriv help för att få en lista av alla typer\n").lower().capitalize().strip()
    if x == "Help":
        print(allTypes)
    else:
        types.append(x)


poke = poke[poke["Type1"].isin(types)]
poke = poke[poke["Type2"].isin(types)]


x = input("vill du sortera efter något annat?\n")
y = int(input(""))
z = input("större eller mindre?")

if x in {"Total","HP","Attack","Defense","Sp. Atk","Sp. Def","Speed","Generation"}:

    if z == "större":
        poke = poke[poke[x] > y]

    elif z == "mindre":
        poke = poke[poke[x] < y]
    
    else:
        poke = poke[poke[x] == y]
    



print(poke)
