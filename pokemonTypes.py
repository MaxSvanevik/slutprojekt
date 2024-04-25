import pandas as pd

pd.set_option("display.max_rows", None)
poke = pd.read_csv("Pokemon2.csv")
types = ["Water", "Flying", "Normal", "Dragon", "Fairy"]


# poke = poke[(poke["Type1"] == types[0]) | (poke["Type1"] == types[1])]
poke = poke[(poke["Type1"] == types[0]) | (poke["Type2"] == types[0])]
# poke = poke[(poke["Type1"] == types[1]) | (poke["Type2"] == types[1])]

poke = poke[(poke["Attack"] > 100)]
poke = poke[(poke["Generation"] <= 4) | (poke["Generation"] == 8)]


print(poke)
