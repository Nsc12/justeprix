start = str (input ("Le jeux du juste prix! "))
while start != "go":
    start = str(input("Le jeux du juste prix! (go POUR COMMENCER ! "))
print("Bonne chance")
import random
number = random.randint (0,1000)
number1 = int(input("Devinez un nombre:"))
while number != number1:
    if number < number1:
        print("Plus petit!")
        number1 = int(input("Devinez un nombre :"))
    elif number > number1:
        print("Plus grand !")
        number1 = int(input("Devinez un nombre : "))

    else:
        print ("Gagné !!")