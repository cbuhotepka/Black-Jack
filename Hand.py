# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 14:36:19 2020

@author: Alex
"""



class Hand():
    
    def __init__(self,cards=[],score=0):
        self.cards = cards
        self.score = score
        
    def evaluate(self):
        self.score = 0
        for card in self.cards:
            self.score += card.value
            
        #Check Aces
        if self.score > 21:
            for card in self.cards:
                if card.rank == 'Ace':
                    self.score -= 10
                    if self.score <= 21:
                        break
        
    def add_card(self,card):
        self.cards.append(card)
        self.evaluate()
        
    def reset(self):
        self.cards = []
        self.score = 0
        
    def visualize(self):
        for card in self.cards:
            print(card)
        print(f"Score: {self.score}")