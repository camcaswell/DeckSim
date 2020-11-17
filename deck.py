import random
from math import inf as INF

class Card:
    def __init__(self, val, shuffle=None):
        self.val = val
        if shuffle is None:
            if val in (2, -INF):
                shuffle = True
            else:
                shuffle = False
        self.shuffle = shuffle

    def __repr__(self):
        return str(self.val)

class Deck:
    default = [Card(v) for v in 
                      1 * (-INF,)   #miss
                    + 3 * (-1,)
                    + 5 * (0,)
                    + 3 * (1,)
                    + 1 * (2,)
                ]

    def __init__(self, cards=None):
        if cards is None:
            cards = Deck.default
        cards = list(cards)
        self.full = cards[:]
        self.current = cards[:]

    def __str__(self):
        return f"Full:    {self.full}\nCurrent: {self.current}"

    def draw(self):
        if not self.current:
            self.reshuffle()
        top = self.current.pop()
        if top.shuffle:
            self.reshuffle()
        return top

    def reshuffle(self):
        self.current = self.full[:]
        random.shuffle(self.current)

