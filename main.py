import card
from card import Card
import random,math,time ; 


# used for getting desired input for example: we want the amount of players to be a number and not some random letter
def take_input( Text : str , Type : any ):
    userinput = None ; 
    # keep trying until they reach the desired type
    while userinput == None:
        try:
            userinput = Type(input(Text)) ; 
        except: pass
        if userinput == None:
            print( f'Invalid Input, Expected Type: {str(Type)}' )
    return userinput ;       

class Player():
    def __init__( self , Name : str , Id : int ):
        self.name = Name ; 
        self.id = Id ; 
        self.deck = [] ;


class Computer():
    def __init__( self , Id : int ):
        self.id = Id ; 

class Game():
    def __init__(self,amount_of_players):
        # generate a random deck of cards
        self.CardsPile = Card.new_deck() ;  
        self.CurrentPile = [] ; 
        
        self.Player_Instances = [] ; 
        self.Computer_Instances = [] ; 

        self._innit_game(amount_of_players) ; 
    # public methods 
    def get_number_of_players(self):
        return len(self.Player_Instances) ; 

    def is_move_legal( self , Move ):
        pass

    def _innit_game( self , amount_of_players : int ):
        for x in range(amount_of_players):
            # give each player an id so they can use it 
            player_id = x + 1 ; 
            playername = take_input( f'Player {player_id} Name: ' , str )

            self.Player_Instances.append(Player( playername , player_id ))
            # make a computer for every player that was made
            self.Computer_Instances.append(Computer(player_id)) ; 
            print( f'Computer {player_id} was registered' ) ;   

        # add a random card to the pile to start the game off


    def get_player_from_id( self , Id : int ):
        return self.Player_Instances[Id] ; 


amount_of_players_input = take_input( 'Choose The Amount Of Players: ' , int )
game_instance = Game(amount_of_players_input) ; 

if __name__ == '__main__':
    # Main game loop
    while True:
        for x in range(len(game_instance.Player_Instances)):
            current_player_instance = game_instance.get_player_from_id(x) ; 
            player_input = take_input( f'Make a move, player {current_player_instance.id} ({current_player_instance.name}): ' , str ) ; 
            
            print(f'| {[str(x) + " |" for x in current_player_instance.deck]}')

