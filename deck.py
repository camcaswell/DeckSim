import random
from math import inf as INF

class Card:
    def __init__(self, val, shuffle=None, roll=False):
        self.val = val
        if shuffle is None:
            if val in (2, -INF):
                shuffle = True
            else:
                shuffle = False
        self.shuffle = shuffle
        self.roll = roll

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

    def draw(self, adv=False, disadv=False):
        if adv and disadv:
            adv = disadv = False
        top = self._draw()
        drawn = [top]
        while top.roll:
            top = self._draw()
            drawn.append(top)
        if any(c.shuffle for c in drawn):
            self.reshuffle()
        val1 = sum(c.val for c in drawn)

        if adv:
            return max(val1, self.draw())
        elif disadv:
            return min(val1, self.draw())
        else:
            return val1

    def _draw(self):
        if not self.current:
            self.reshuffle()
        return self.current.pop()

    def reshuffle(self):
        self.current = self.full[:]
        random.shuffle(self.current)

