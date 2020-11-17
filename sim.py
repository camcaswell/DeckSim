from math import inf as INF

from deck import *


a = [Card(v) for v in 
                  1 * (-INF,)   #miss
                + 3 * (-1,)
                + 5 * (0,)
                + 3 * (1,)
                + 1 * (2,)
            ]

b = [Card(v,s) for v,s in 
                  1 * ((-2, True),)
                + 3 * ((-1, False),)
                + 5 * ((0, False),)
                + 3 * ((1, False),)
                + 1 * ((2, True),)
            ]

ATK = 4
d1 = Deck(a)
d2 = Deck(b)

n = 100000
results = []

for d in (d1, d2):
    total = 0
    for _ in range(n):
        md = d.draw().val
        dmg = max(0, ATK+md)
        total += dmg
    results.append(total/n)

print(results[0])
for r in results[1:]:
    print(r-results[0])