# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 13:55:40 2020

@author: Alex
"""


class Card():
    
    def __init__(self,suit,rank,value):
        self.suit = suit
        self.rank = rank
        self.value = value
        
    def __str__(self):
        return f"{self.rank} of {self.suit}"


suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

from random import shuffle

class Deck():
    
    def __init__(self,cards=[],index_card=0):
        self.cards = cards
        self.index_card = index_card
        
        self.create()

    def create(self,deck_len=52):
        '''
        Creating a new deck
        '''
        self.cards = []
        if deck_len == 52:
            for suit in suits:
                for rank in ranks:
                    self.cards.append(Card(suit,rank,values[rank]))        
    
    def shuffle(self):
        '''
        Shuffling current deck and dropping index to zero
        '''
        shuffle(self.cards)
        self.index_card=0
        
    def __str__(self):
        result = 'INDEX: ' + str(self.index_card)
        for card in self.cards:
            result += '\n' + str(card)
        return result
        
        