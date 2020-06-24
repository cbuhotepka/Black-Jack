# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 13:39:36 2020

@author: Alex
"""


class PlayerAccount():
    
    def __init__(self,name='',balance=500):
        self.name = name
        self.balance = balance
        
        self.name = self.create_player()
        
        
    def deposit(self,amount):
        self.balance += amount
        
    def withdraw(self,amount):
        if self.balance < amount:
            return False
        else:
            self.balance -= amount
            return True
        
    def create_player(self):
        return input("Hello! What is your name? ")
    
    
    def __str__(self):
        return f"{self.name}: ${self.balance}"
        
