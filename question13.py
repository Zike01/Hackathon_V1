"""
13 - Write a function that simulates a rubbish version of the game of snap! (https://
en.wikipedia.org/wiki/Snap_(card_game). There are two players each of whom receives half a
deck of cards each (at random) and then plays one card at a time. If the two players play a card
with the same value (e.g. two Kings or two 4’s) then the phrase “Snap!” should be printed to
screen and the game ends.
"""

import random
from time import sleep


def snap():
    cards = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K',
             'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K',
             'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K',
             'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

    random.shuffle(cards)

    # Each player receives half a deck of cards
    player_1_cards = cards[0: int(len(cards)/2)]
    player_2_cards = cards[int(len(cards)/2):]

    print(len(player_1_cards))
    print(len(player_2_cards))

    for i in range(len(player_1_cards)):
        print(f"Player 1 card = {player_1_cards[i]}")
        print(f"Player 2 card = {player_2_cards[i]}")
        print("----------------------------")
        if player_1_cards[i] == player_2_cards[i]:
            print("SNAP!")
            break
        sleep(2)


snap()
