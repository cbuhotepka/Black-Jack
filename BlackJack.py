#!/usr/bin/env python
# coding: utf-8

# In[1]:


class PlayerAccount():
    
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance
        
    def deposit(self,amount):
        self.balance += amount
        
    def withdraw(self,amount):
        self.balance -= amount
        
    def take_bet(self):
        while True:
            try:
                bet = int(input("What is your bet? "))
            except:
                print("Invalid input, try again")
            else:
                if bet <= self.balance:
                    return bet
                else:
                    print("Your bet is bigger, than your account!")

    def __str__(self):
        return f"{self.name}: ${self.balance}"
        


# In[2]:


class Card():
    
    def __init__(self,suit,rank,value):
        self.suit = suit
        self.rank = rank
        self.value = value
        
    def __str__(self):
        return f"{self.rank} of {self.suit}"


# In[3]:


suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}


# In[4]:


from random import shuffle

def deck_create():
    deck = []
    for suit in suits:
        for rank in ranks:
            deck.append(Card(suit,rank,values[rank]))
    return deck


# In[5]:


class Hand():
    
    def __init__(self,cards,score):
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
        
    def visualize(self):
        for card in self.cards:
            print(card)
        print(f"Score: {self.score}")


# In[6]:


class Desk():
    
    def __init__(self, dealer_hand, player_hand, account, bet):
        self.dealer_hand = dealer_hand
        self.player_hand = player_hand
        self.account = account
        self.bet = bet
        
    def visualize_concealed(self):
        clear_output()
        print(f"BET: ${self.bet}\n")
        print("DEALER:")
        print(self.dealer_hand.cards[0])
        print("- CONCEALED -")
        print("\n", self.account, ": ")
        self.player_hand.visualize()
        
    def visualize(self):
        clear_output()
        print("DEALER:")
        self.dealer_hand.visualize()
        print("\n", self.account, ": ")
        self.player_hand.visualize()
        
    
            


# In[7]:


from IPython.display import clear_output
from time import sleep


# In[8]:


def game_input():
    while True:
        move = input("You could HIT or STAY. What is your move?").lower()
        if move in ['hit', 'stay']:
            return move
        else:
            print("Invalid command! Try again")


# In[ ]:





# In[10]:


game = True
player = PlayerAccount(input("Hello! What is your name? "), 500)
print(f"Great to see you, {player.name}! Your balance is ${player.balance}")
print("Let's play!")
main_deck = deck_create()

while game:
    
    bet = player.take_bet()
    player.balance -= bet
    
    #Shuffling Main Deck
    shuffle(main_deck)
    #Reseting Hands and count
    player_hand = Hand([],0)    
    dealer_hand = Hand([],0)
    stay = False
    result = 'tie'
    
    #Dealing
    for i in [0, 2]:
        player_hand.add_card(main_deck[i])
        dealer_hand.add_card(main_deck[i+1])
    card_count = 4
    
    #Player's turn
    while not stay :
        desk = Desk(dealer_hand, player_hand, player, bet)
        desk.visualize_concealed()
        
        move = game_input()
        if move == 'stay':
            stay = True
        elif move == 'hit':
            print("\nYour card is : ", main_deck[card_count])
            player_hand.add_card(main_deck[card_count])
            card_count += 1
            sleep(2)
            desk = Desk(dealer_hand, player_hand, player, bet)
            
            if player_hand.score > 21:
                desk.visualize_concealed()
                print("You exceeded 21 scores!")
                result = 'lose'
                sleep(3)
                break
                
    #Dealer's turn
    if result != 'lose':
        while (dealer_hand.score < player_hand.score) or (dealer_hand.score == player_hand.score and dealer_hand.score < 17):
            #if dealer_hand.score < 17:
            desk.visualize()
            print("\nDealer's card is : ", main_deck[card_count])                
            dealer_hand.add_card(main_deck[card_count])
            card_count += 1
            desk = Desk(dealer_hand, player_hand, player, bet)            
            sleep(2)
            #else:
             #   break           
    
        if dealer_hand.score > 21:
            result = 'win'
        elif dealer_hand.score > player_hand.score:
            result = 'lose'
        elif dealer_hand.score == player_hand.score:
            result = 'tie'
        elif dealer_hand.score < player_hand.score:
            result = 'win'
        else:
            print("Something in checking went wrong")
    
    desk.visualize()
    
    print()
    if result == 'lose':
        print("You've lost :(")
    elif result == 'win':
        print("You've won!")
        player.balance += bet*2
    else:
        print("It's a tie. Your bet is back")
        player.balance += bet
        
    print(f"Your balance is ${player.balance}")
    
    sleep(2)    
    if player.balance == 0:
        print("You have no money! :( :(")
        game = False
    else:            
        if input("Enter EXIT for exit").lower() == 'exit':
            game = False
            
            
    
    #LOOP:
    #Visualize a desk
    #Ask a move
    
    #LOOP:
    #Visualize a desk
    #Make a move
    
    #Assess
    
    #Visualize a desk
    #Ask for more
    


# In[ ]:





# In[ ]:




