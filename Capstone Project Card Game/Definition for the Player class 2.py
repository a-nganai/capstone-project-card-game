# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 15:48:53 2024

@author: hp
"""
class Player(object):
    """ a player """
    # methods for listing 1
    def add_card_to_hand(self, card):
        """ card, a string
            Adds valid card to the player's hand """
        if card != None:
            self.hand.append(card)
    def remove_card_from_hand(self, card):
        """ card, a string
            Remove card from the player's hand """
        self.hand.remove(card)
    def hand_size(self):
        """ Returns the number of cards in player's hand """
        return len(self.hand)