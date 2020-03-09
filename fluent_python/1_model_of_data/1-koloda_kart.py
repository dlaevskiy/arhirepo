import collections
from random import choice

Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                       for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


objDeck = FrenchDeck()

print(len(objDeck))
print(objDeck[5].suit)
print(choice(objDeck))
print(objDeck[:3])

for card in objDeck:
    print(card)

print(Card('Q', 'hearts') in objDeck)