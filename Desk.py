# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 16:06:50 2020

@author: Alex
"""
from PlayerAccount import PlayerAccount
from Hand import Hand
from Deck import Deck


def clear_scrn():
    print('\n'*30)
    

class Desk():
    
    def __init__(self, dealer_hand=Hand(), player_hand=Hand(), account=PlayerAccount(), deck=Deck(), bet=0):
        self.dealer_hand = dealer_hand
        self.player_hand = player_hand
        self.account = account
        self.bet = bet
        self.deck = deck
        
    def visualize_concealed(self):
        clear_scrn()
        print(f"BET: ${self.bet}\n")
        print("DEALER:")
        print(self.dealer_hand.cards[0])
        print("- CONCEALED -")
        print("\n", self.account, ": ")
        self.player_hand.visualize()
        
    def visualize(self):
        clear_scrn()
        print("DEALER:")
        self.dealer_hand.visualize()
        print("\n", self.account, ": ")
        self.player_hand.visualize()
        

                
    def deal_card(self, whom):
        if whom == 'player':
            self.player_hand.add_card(self.deck.cards[self.deck.index_card])
            self.deck.index_card += 1
        elif whom == 'dealer':            
            self.dealer_hand.add_card(self.deck.cards[self.deck.index_card])
            self.deck.index_card += 1
            