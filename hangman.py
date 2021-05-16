# -*- coding: utf-8 -*-
"""
Created on Sun May 09 20:33:46 2021

@author: toti.cavalcanti
"""
#!/bin/python3

import random
import time

# Initial Steps to invite in the game:
print("\nBem-vindo ao jogo Forca\n")
name = input("Digite seu nome por favor: ")
print("Olá " + name + " :)")
time.sleep(2)
print("O jogo está prestes a começar!\nBoa sorte!")
time.sleep(3)

def find(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]

# The parameters we require to execute the game:
def main():
    global count
    global display
    global word
    global word_l
    global already_guessed
    global length
    #global play_game
    words_to_guess = [  "ardiloso","basquete","hospital",
                        "filme","promessa","horrorizado","material",
                        "praia","caminho","perigo", "asterisco",
                        "planta", "amor", "ave", "amendoim", 
                        "banheiro", "campeonato", "forca", "trilogia",
                        "paçoca", "menta", "caatinga", "afobado",
                        "quimera", "otorrinolaringologista", "ovo",
                        "parque", "rato", "noite", "girafa"]

    word = random.choice(words_to_guess)
    word_l = list(word)
    #print(word)
    length = len(word_l)
    count = 0
    display = []
    [display.append("_") for i in range(length)]
    #print(display)
    already_guessed = []
    #play_game = ""

    hangman()

# A loop to re-execute the game when the first round ends:
def play_loop():
    global play_game
    play_game = input("Você quer jogar de novo? s = sim, n = não \n")
    # only get out the loop when the user enter s or S, n or N
    while play_game not in ["s", "n","S","N"]:
        play_game = input("Você quer jogar de novo? s = sim, n = não \n")
    if play_game == "s":
        main()
    elif play_game == "n" or play_game == "N":
        print("Obrigado por jogar! Esperamos você de volta pra mais um desafio!")
        exit()

# Initializing all the conditions required for the game:
def hangman():
    global count
    global display
    global word
    global word_l
    global already_guessed
    global play_game
    limit = 9

    if count == 0:
      print("   _____ \n"
                    "  |      \n"
                    "  |      \n"
                    "  |      \n"
                    "  |      \n"
                    "  |      \n"
                    "  |      \n"
                    "__|__\n")

    guess = input("Tente advinhar a palavra: " + " ".join(display) + " \ndigite seu palpite: \n")
    guess = guess.strip()
    guess = guess.lower()
    
    # Checks if is not a letter
    if not guess.isalpha() or len(guess) > 1:
        print("Opa, você digitou algo errado, por favor, tente apenas letras\n")
        hangman()
    elif guess in word_l:
        # list with already guessed letters
        already_guessed.extend([guess])
        # find all index of the guess letter in word_l
        indexs = find(word_l, guess)
        print("Boa, palpite correto!")

        for indx in indexs:
          display[indx] = guess
          word_l[indx] = "_"
    elif guess in already_guessed:
        print("Essa letra você já tentou, escolha outra por favor!\n")
    else:
        already_guessed.extend([guess])
        count += 1

        if count == 1:
            time.sleep(1)
            print("   _____ \n"
                  "  |     |\n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Palpite errado! A letra " + guess + " não está na palavra! \n" + "Você ainda tem " + str(limit - count) + " palpites restantes.\n")

        elif count == 2:
            time.sleep(1)
            print("   _____ \n"
                 "  |     |\n"
                 "  |     |\n"
                 "  |      \n"
                 "  |      \n"
                 "  |      \n"
                 "  |      \n"
                 "__|__\n")
            print("Palpite errado! A letra " + guess + " não está na palavra! \n" + "Você ainda tem " + str(limit - count) + " palpites restantes.\n")

        elif count == 3:
            time.sleep(1)
            print("   _____ \n"
                 "  |     |\n"
                 "  |     |\n"
                 "  |     |\n"
                 "  |      \n"
                 "  |      \n"
                 "  |      \n"
                 "__|__\n")
            print("Palpite errado! A letra " + guess + " não está na palavra! \n" + "Você ainda tem " + str(limit - count) + " palpites restantes.\n")

        elif count == 4:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Palpite errado! A letra " + guess + " não está na palavra! \n" + "Você ainda tem " + str(limit - count) + " palpites restantes.\n")

        elif count == 5:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |     | \n"
                  "  |      \n"
                  "__|__\n")
            print("Palpite errado! A letra " + guess + " não está na palavra! \n" + "Você ainda tem " + str(limit - count) + " palpites restantes.\n")

        elif count == 6:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |    /| \n"
                  "  |      \n"
                  "__|__\n")
            print("Palpite errado! A letra " + guess + " não está na palavra! \n" + "Você ainda tem " + str(limit - count) + " palpites restantes.\n")
        elif count == 7:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |    /|\ \n"
                  "  |       \n"
                  "__|__\n")
            print("Palpite errado! A letra " + guess + " não está na palavra! \n" + "Você ainda tem " + str(limit - count) + " palpites restantes.\n")

        elif count == 8 :
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |    /|\ \n"
                  "  |    /  \n"
                  "__|__\n")
            print("Palpite errado! A letra " + guess + " não está na palavra! \n" + "Você ainda tem " + str(limit - count) + " palpite restante.\n")

        elif count == 9:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |    /|\ \n"
                  "  |    / \ \n"
                  "__|__\n")
            print("Palpite errado. Voce foi enforcado!!!")
            print("A palavra era: ", word)
            print()
            play_loop()

    if word_l == ['_'] * length:
        print("Parabéns! \nVocê adivinhou a palavra! ;)")
        play_loop()

    elif count != limit:
        hangman()
        
main()