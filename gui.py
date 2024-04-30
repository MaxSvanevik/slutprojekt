import PySimpleGUI as sg
import numpy as np

allTypes = [
    "Normal", "Fire", "Water", "Electric", "Grass", "Ice", 
    "Fighting", "Poison", "Ground", "Flying", "Bug", "Dark",
    "Rock", "Ghost", "Dragon", "Psychic", "Steel", "Fairy"
]
types = set()
sg.theme("DarkTanBlue")
layout = [

    [sg.Text("klicka på typerna du vill ha med")],
    [sg.Button(typ, key=typ) for typ in allTypes[:9]],
    [sg.Button(typ, key=typ) for typ in allTypes[9:]],
    [sg.Text("Hur vill du sortera dom?")],
    [sg.Button("Single types"), sg.Button("Dual types"), sg.Button("Båda")]
]

window = sg.Window("Pokémon Types", layout)

while True:
    event, values = window.read()
    print(event)
    print(values)
    if event == sg.WINDOW_CLOSED:
        break
    if event in types:
        types.remove(event)
        window[event].update(button_color=(sg.theme_button_color_text(), sg.theme_button_color_background()))
    else:
        types.add(event)
        window[event].update(button_color=('white', 'red'))



window.close()