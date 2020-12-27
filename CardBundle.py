import random

commons = ("C0", "C1", "C2", "C3", "C4", "C5", "C6", "C7", "C8", "C9")
uncommons = ("U0", "U1", "U2", "U3", "U4", "U6")
rares = ("R0", "R1", "R2", "R3", "R4", "R5")
legendaries = ("L0", "L1", "L2", "L3", "L4")


#there needs to be at least X amount of "cards" of each rarity so there's no chance of running out of cards to select from
#chances: common - 64% | uncommon - 25% | rare - 10% | legendary - 1%
def rand_bundle(amount):
    commons1, uncommons1, rares1, legendaries1 = list(commons), list(uncommons), list(rares), list(legendaries)
    result = []
    for i in range(amount):
        percent = random.randint(0, 99)
        if percent < 64:    #64%
            card = random.choice(commons1)  #a random common card
            result.append(card)         #appending the card to the results
            commons1.remove(card)       #removing the card from the selection list so as to not have any duplicates
        elif percent < 89:  #+= 25%
            card = random.choice(uncommons1)
            result.append(card)
            uncommons1.remove(card)
        elif percent < 99:  #+= 10%
            card = random.choice(rares1)
            result.append(card)
            rares1.remove(card)
        else:   #+= 1%
            card = random.choice(legendaries1)
            result.append(card)
            legendaries1.remove(card)
    return result

bundle = rand_bundle(5)
print(bundle)
