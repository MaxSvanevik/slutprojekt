import pandas as pd

poke = pd.read_csv("Pokemon.csv")
poke = poke.sort_values("Form", ascending=False)
pd.set_option("display.max_rows", None)
poke = poke.replace(" ", "None")
print(poke.head(222))