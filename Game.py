# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 16:47:25 2020

@author: о
"""
from Desk import Desk
from time import sleep

class Game():
    
    def __init__(self):
        self.desk = Desk()
        self.result = ''
        self.playing = True
        
        
    def game_input(self):
        while True:
            move = input("You could HIT or STAY. What is your move? ").lower()
            if move in ['hit', 'stay']:
                return move
            else:
                print("Invalid command! Try again")
                
                
    def take_bet(self):
        while True:
            try:
                self.desk.bet = int(input("What is your bet? "))
            except:
                print("Invalid input, try again")
            else:
                if self.desk.bet <= 0:
                    print("Your bet must be bigger than $0")
                elif self.desk.bet > self.desk.account.balance:
                    print("Your bet is bigger, than your account!")
                else:
                    self.desk.account.balance -= self.desk.bet
                    break
                
                
    def players_turn(self):
        move = ''
        self.result = ''
        while move != 'stay' :
            self.desk.visualize_concealed()
            move = self.game_input()
            
            if move == 'hit':
                current_card = self.desk.deck.cards[self.desk.deck.index_card]
                print("\nYour card is : ", current_card)
                self.desk.player_hand.add_card(current_card)
                self.desk.deck.index_card += 1
                
                sleep(2)
                                    
                if self.desk.player_hand.score > 21:
                    self.desk.visualize_concealed()
                    print("You exceeded 21 scores!")
                    self.result = 'lose'
                    sleep(3)
                    break
                elif self.desk.player_hand.score == 21:
                    print("Your score is 21!")
                    sleep(3)
                    break
                
        
    def dealers_turn(self):
        if self.result != 'lose':
            while self.desk.dealer_hand.score < 17:
                self.desk.visualize()
                
                current_card = self.desk.deck.cards[self.desk.deck.index_card]
                print("\nDealer's card is : ", current_card)                
                self.desk.dealer_hand.add_card(current_card)
                self.desk.deck.index_card += 1
                sleep(2)
                #else:
                 #   break           
        
        
    def check_result(self):
        if self.result != 'lose':
            if self.desk.dealer_hand.score > 21:
                self.result = 'win'
            elif self.desk.dealer_hand.score > self.desk.player_hand.score:
                self.result = 'lose'
            elif self.desk.dealer_hand.score == self.desk.player_hand.score:
                self.result = 'tie'
            elif self.desk.dealer_hand.score < self.desk.player_hand.score:
                self.result = 'win'
            else:
                print("Something in checking went wrong")
            
        print()
        if self.result == 'lose':
            print("You've lost :(")
        elif self.result == 'win':
            print("You've won!")
            self.desk.account.balance += self.desk.bet*2
        else:
            print("It's a tie. Your bet is back")
            self.desk.account.balance += self.desk.bet
    
    
    def main_game(self):
              
        while self.playing:
            
            self.take_bet()
            
            #Shuffling Main Deck
            self.desk.deck.shuffle()
            
            #Reseting Hands 
            self.desk.player_hand.reset()    
            self.desk.dealer_hand.reset()
                      
            
            #Dealing
            for i in range(2):
                self.desk.deal_card('player')
                self.desk.deal_card('dealer')
                
            self.players_turn()
            self.dealers_turn()
            
            self.desk.visualize()                        
            self.check_result()
                            
            print(f"Your balance is ${self.desk.account.balance}")
            
            sleep(2)    
            
            if self.desk.account.balance == 0:
                print("You have no money! :( :(")
                self.playing = False
            else:            
                if input("Enter EXIT for exit: ").lower() == 'exit':
                    self.playing = False