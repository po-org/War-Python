import random

# Rules
# The goal is to be the first player to win all 52 cards

# The Deal
# The deck is divided evenly, with each player receiving 26 cards, 
# dealt one at a time, face down. Anyone may deal first. Each player 
# places their stack of cards face down, in front of them.

# The Play
# Each player turns up a card at the same time and the player with the 
# higher card takes both cards and puts them, face down, on the bottom of his 
# stack.If the cards are the same rank, it is War. Each player turns up one 
# card face down and one card face up. The player with the higher cards 
# takes both piles (six cards). If the turned-up cards are again the same 
# rank, each player places another card face down and turns another card face 
# up. The player with the higher card takes all 10 cards, and so on.

# How to Keep Score
# The game ends when one player has won all the cards.

# Players will include human vs computer

# Card Types
suits = ['♥','♦','♣','♠']
ranks = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']

# Declare Array For Deck
wardeck = []

for suit in suits:
    for rank in ranks:
        card = (rank, suit)
        wardeck.append(card)

# Shuffle Array
random.shuffle(wardeck)

# Deal Cards
handplayer = wardeck[0:26]
handcomputer = wardeck[26:52]
# print(handcomputer)

# print(handplayer)
print(handplayer[0])
print(handcomputer[0])
if (handplayer[0] > handcomputer[0]):
    print('The winner is', handplayer[0])
else : print('The winner is', handcomputer[0])
print(wardeck)