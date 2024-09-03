# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 16:00:17 2024

@author: hp
"""

import random

class CardDeck(object):
    """ A deck of cards 2-9 of spades, hearts, diamonds, clubs """
    def __init__(self):
        """ a deckmof cards(strings e.g. "2C" for the 2 of clubs)
            contains all cards possible"""
        hearts = "2H,3H,4H,5H,6H,7H,8H,9H"
        diamonds = "2D,3D,4D,5D,6D,7D,8D,9D"
        spades = "2S,3S,4S,5S,6S,7S,8S,9S"
        clubs = "2C,3C,4C,5C,6C,7C,8C,9C"
        self.deck = hearts.split(',')+diamonds.split(',') + \
                    spades.split(',')+clubs.split(',')
    def get_card(self):
        """ Returns one random card (string) and
            returns None if there are no more cards """
        if len(self.deck) < 1:
            return None
        card = random.choice(self.deck)
        self.deck.remove(card)
        return card
    def compare_cards(self, card1, card2):
        """ returns the larger card according to
        (1) the larger of the numbers or, if equal,
        (2) Spades > Hearts > Diamonds > Clubs """
        if card1[0] > card2[0]:
            return card1 
        elif card1[0] < card2[0]:
            return card2
        elif card1[1] > card2[1]:
            return card1
        else:
            return card2