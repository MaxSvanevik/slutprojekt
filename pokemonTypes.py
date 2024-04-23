import pandas as pd


def types(type1 = input("ange en pokemon type"), type2 = input("ange en till (lämna blank för ingen secondary type)")):
    poke = pd.read_csv("Pokemon2.csv")
    poke = poke[poke["Type1"] == type1]
    poke = poke[poke["Type2"] == type2]
    print(poke)

types()
    