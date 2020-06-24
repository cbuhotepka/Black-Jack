


# In[8]:


def greeting(player):
    print(f"Great to see you, {player.name}! Your balance is ${player.balance}")
    print("Let's play!")            



# In[10]:
print('\n'*30)
from Game import Game
game = Game()
greeting(game.desk.account)

game.main_game()


            



