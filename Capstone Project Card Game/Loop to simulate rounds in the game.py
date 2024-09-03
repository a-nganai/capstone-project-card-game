# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 00:33:25 2024

@author: hp
"""

name1 = input("What's your name? Player 1: ")
player1 = Player(name1)
name2 = input("What's your name? Player 2: ")
player2 = Player(name2)
deck = CardDeck()

while True:
    player1_card = deck.get_card()
    player2_card = deck.get_card()
    player1.add_card_to_hand(player1_card)
    player2.add_card_to_hand(player2_card)
    
    if player1_card == None or player2_card == None:
        print("Game Over. No more cards in deck.")
        print(name1, " has ", player1.hand_size())
        print(name2, " has ", player2.hand_size())
        print("Who won?")
        if player1.hand_size() > player2.hand_size():
            print(name2, "wins!")
        elif player1.hand_size() < player2.hand_size():
            print(name1, "wins!")
        else:
            print("A Tie!")
        break
    else:
        print(name1, ":", player1_card)
        print(name2, ":", player2_card)
        if deck.compare_cards(player1_card,player2_card)==player1_card:
            player2.add_card_to_hand(player1_card)
            player1.remove_card_from_hand(player1_card)
        else:
            player1.add_card_to_hand(player2_card)
            player2.remove_card_from_hand(player2_card)