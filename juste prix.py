# prgm qui permet de connaitre le prix user et ordi
#https://www.freecodecamp.org/french/news/25-projets-python-pour-les-debutants-quelques-exemples-pour-commencer-a-coder-avec-python/#projet-python-g-n-rateur-de-mot-de-passe


import random

prix = random.randint(1, 100)

while True:
    print("guess a number :")
    x = int(input())
    if x < prix:
        print("dont be shy!")
    if x > prix:
        print("try less")
    if x == prix:
        print("number is " + str(x))
        break

print("okok")



    