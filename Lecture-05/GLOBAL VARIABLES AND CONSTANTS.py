import random

HEADS = 1
TAILS = 2
TOSSES = 10

def tosses_cion():
    for i in range(TOSSES):
        if random.randint(HEADS,TAILS) == HEADS:
            print("Heads")
        else:
            print("Tails")

tosses_cion()