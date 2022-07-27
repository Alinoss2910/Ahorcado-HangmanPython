# hangman.py
#importing the time module
from ast import If
import time
import random
import urllib2
import json

response = urllib2.urlopen("https://palabras-aleatorias-public-api.herokuapp.com/random")
result = json.load(response)

turns = 10

print ("Hola, Vamos a jugar al Ahorcado. Tendrás  " + str(turns) + " turnos!")

print ("")

# delay
time.sleep(0.5)


# set of words to guess from
wordList = ["putamare", "cagoento", "python", "caranavo", "hola", "codificacion", "buajajaja", "porro", "fumar", "esternocleidomastoideo"]
word = random.choice(wordList)
opcion = ""
guiones = ""
nLetras = 0

for i in word:
        guiones += "_"

while turns > 0:
    print(guiones)
    print("Introduce una letra en minuscula")
    opcion = input()
    for t in word:
        if len(word) >= nLetras:
            if opcion is t:
                comp = list(guiones)
                comp[nLetras] = opcion
                guiones = "".join(comp)
                nLetras += 1
            else:
                nLetras += 1
    turns -= 1
    if guiones is word:
        cerrar = input("¿Quieres seguir jugando?")
    nLetras = 0