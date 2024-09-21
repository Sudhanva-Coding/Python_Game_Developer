#Write a python progame to shuffle a deck of cards and pick 5 cards at random

import random, itertools

card_deck = list(itertools.product(range(1, 14), ["Spade", "Heart", "Diamond", "Club"]))

# Shuffle the deck
random.shuffle(card_deck)

# draw five cards
print("your cards are :")
for i in range (5):
  print(card_deck[i][0], "of", card_deck[i][1])
  