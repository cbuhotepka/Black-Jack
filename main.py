from Game import Game


# In[8]:


def greeting(player):
    print(f"Great to see you, {player.name}! Your balance is ${player.balance}")
    print("Let's play!")            



# In[10]:

game = Game()
greeting(game.desk.account)

game.main_game()


            



