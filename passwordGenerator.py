import random
import re


def ranz(N, M):
    return random.randint(N, M)


ePattern = r'[A-Z]+'
Randomtext = 'Python  snake,  also  known  as  Ajgar,  is  one  of  the  most  massively  built  snakes  of  the  Indian  subcontinent.  It belongs to the Boidae family and is dependent on water to quite an extent. One of the unique features of the rock pythons of India is that they can raise their body temperature above the ambient level through muscular contractions.'
Randomtext = Randomtext.split()
runApp = 'Y'
while runApp == 'Y' or runApp == 'y':
    PassType = input("Generate Easy or Hard password:")
    if PassType == "Easy":
        while True:
            ePassword = "".join(
                [Randomtext[ranz(1, len(Randomtext)) - 1], Randomtext[ranz(1, len(Randomtext)) - 1]])
            if len(ePassword) >= 10:
                break
    elif PassType == "Hard":
        ePassword = ''
        while True:
            k = chr(ranz(33, 126))
            ePassword = ePassword + str(k)
            if len(ePassword) >= 10:
                break

    else:
        print("Wrong Type. Enter 'Hard' or 'Easy'")
    print(ePassword)
    runApp = input("Generate new Password: Y/N?")
