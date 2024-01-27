import random
import time
import os


def clear_screen():
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')


def cree_une_sequence():
    seq = ""
    for i in range(4):
        seq += str(random.randint(0, 9))
    return seq


score = 0
sequence = cree_une_sequence()

while True:
    print("Retenez la séquence")
    time.sleep(1)
    print(f"{sequence}")
    time.sleep(3)
    clear_screen()
    reponse = input("Votre réponse: ")
    if reponse == sequence:
        score += 1
        print(f"Votre score: {score}")
        sequence += str(random.randint(0, 9))
        clear_screen()
        time.sleep(3)
    else:
        break

print(f"Mauvaise réponse, la séquence était: {sequence}")
print(f"Votre score final: {score}")
