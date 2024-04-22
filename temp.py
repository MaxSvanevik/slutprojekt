import pandas as pd

# poke = pd.read_csv("Pokemon.csv")
# poke = poke.sort_values("Form", ascending=False)
pd.set_option("display.max_rows", None)
# poke = poke.replace(" ", "None")
# poke = poke.drop_duplicates(subset="ID", keep="last")
# poke = poke.sort_values("ID", ascending=True)
# print(poke.head(1010))
# poke.to_csv('Pokemon2.csv', index=False)
poke = pd.read_csv("Pokemon2.csv")
print(poke)