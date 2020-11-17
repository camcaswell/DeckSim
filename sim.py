from math import inf as INF

from deck import *

def sim(deck, n=100000, atk=4, adv=False, disadv=False):
    total = 0
    for _ in range(n):
        dmg = max(0, atk + deck.draw(adv=adv, disadv=disadv))
        total += dmg
    return total/n


a = [Card(v,s) for v,s in 
                  1 * ((-INF, True),)
                + 3 * ((-1, False),)
                + 5 * ((0, False),)
                + 3 * ((1, False),)
                + 1 * ((2, True),)
            ]

b = a + 2 * [Card(1, roll=True)]


d1 = Deck(a)
d2 = Deck(a)
d3 = Deck(a)

results = [sim(d1), sim(d2, adv=True), sim(d1, disadv=True)]

print(results[0])
for r in results[1:]:
    print(r-results[0])