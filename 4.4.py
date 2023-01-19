# Kirjoita peli, jossa tietokone arpoo kokonaisluvun väliltä 1..10. Kone arvuuttelee lukua pelaajalta siihen asti, kunnes tämä arvaa oikein. Kunkin arvauksen jälkeen ohjelma tulostaa tekstin Liian suuri arvaus, Liian pieni arvaus tai Oikein. Huomaa, että tietokone ei saa vaihtaa lukuaan arvauskertojen välissä.

import random

guessesTaken = 0

print("Arvoo numero 1-10")

myName = input()

number = random.randint(1, 10)


while guessesTaken < 1:
     print("Arvoo numero")
     guess = input()
     guess = int(guess)
     guessesTaken = guessesTaken + 0


     if guess < number:
         print("Liian pieni arvaus.")


     if guess > number:
         print("Liian suuri arvaus.")


     if guess == number:
         break

if guess == number:
     print("Oikein")