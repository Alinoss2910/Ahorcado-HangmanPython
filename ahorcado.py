# hangman.py
#importing the time module
from ast import If
import time
import random
from unittest import case

turns = 10

print ("Hola, Vamos a jugar al Ahorcado. Tendrás  " + str(turns) + " turnos!")
print ("")

# delay
time.sleep(0.5)


# set of words to guess from
palabras_comunes=["hola","os","vengo","a","contar","la","historia","de","un","pirata","llamado","monkey","d","luffy","una","mañana","se","desperto","en un barril","que","habian","recogido","unos","piratas","salio","del",
"barril","derribando","de","un","puñetazo","a","los","tres","piratas","que","intentaban","abrir","el","barril","por","la","cerveza","luffy","tiene","mucha","hambre","y","se","dirige","corriendo","a","buscar","comida",
"encontro","unas","manzanas","cuando","un","tripulante","que","no","pintaba","nada","en","ese","barco","lo","descubre","se","hace","su colega","y","van","a","partirle","la","cara","a","la","capitana","del","barco",
"alvida","luffy","como","es","de","goma","estiro","su","brazo","para","mandar","por","los","aires","a","esa","vieja","y","gorda","capitana","cojen","un","bote","y","se","marchan","del","barco","hacia","la",
"isla","mas","cercana","que","es","donde","conocera","a","su","primer","tripulante","roronoa","zoro","un","espadachin","que","usa","el","estilo","tres","espadas","santoryuu","si","una","la","lleva","en","la","boca",
"a","partir","de","hay","luffy","vivira","muchas","aventuras","para","tener","una","tripulacion","de","unas","diez","personas","y","convertirse","en","el","rey","de","los","piratas","sus","nakamas","seran",
"zoro","nami","usopp","sanji","chopper","robin","franky","brook","jimbe","yamato"]
word = random.choice(palabras_comunes)
opcion = ""
guiones = ""
nLetras = 0

for i in word:
        guiones += "_"

while turns >= 0:
    print(guiones)
    print("")
    print("Tienes " + str(turns) + " turnos")
    print("")
    opcion = input("Introduce una letra en minuscula: ")
    print("")
    for t in word:
        if len(word) >= nLetras:
            if opcion == t:
                comp = list(guiones)
                comp[nLetras] = opcion
                guiones = "".join(comp)
                nLetras += 1
            else:
                nLetras += 1
    turns -= 1
    nLetras = 0
    if guiones == word:
        seguir = input("Has ganado. ¿Quieres seguir jugando? [s/n]: ")
        print("")
        if seguir == "s":
            guiones = ""
            word = random.choice(palabras_comunes)
            for i in word:
                guiones += "_"
                turns = 10
        else:
            exit
    if turns == 0:
        print("La palabra era: " + word)
        print("")
        seguir = input("Has perdido. ¿Quieres seguir jugando? [s/n]: ")
        print("")
        if seguir == "s":
            guiones = ""
            word = random.choice(palabras_comunes)
            for i in word:
                guiones += "_"
                turns = 10
        else:
            exit