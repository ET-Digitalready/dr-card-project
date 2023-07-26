import card
from card import Card
import modules.util as util ;
import random,math,time ; 

class Game():
    def __init__(self,**kwargs):
        # generate a random deck of cards
        self.CardsPile = Card.new_deck() ;  

        self.Player_Instances = [] ; 
        self.Computer_Instances = [] ; 

    # public methods 
    def get_number_of_players(self):
        return len(self.Player_Instances) ; 

    def is_move_legal( self , Move ):
        pass


def valid_input_callback(userinput : str):
    return int(userinput) and int(userinput) <= 5 and int(userinput) > 0 ; 
amount_of_players_input = util.take_input( 'Choose The Amount Of Players: ' , valid_input_callback )

print( '[Game Debug] | [Amount of Players]: ' + amount_of_players_input ) ; 
Game = Game(Players=amount_of_players_input) ; 
print(Game.CardsPile)

if __name__ == '__main__':
    # Main game loop
    while True:
        pass