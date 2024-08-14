import random
from enum import Enum, auto
# Define card ranks using Enum
class Rank(Enum):
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 10
    QUEEN = 10
    KING = 10
    ACE = 11
    def __repr__(self):
        return self.name.capitalize()
# Define suits using Enum
class Suit(Enum):
    Hearts = auto()
    Diamonds = auto()
    Clubs = auto()
    Spades = auto()
# Define card class
class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
    def __repr__(self):
        return f'{self.rank} of {self.suit.name.capitalize()}'
# Define deck class
class Deck:
    def __init__(self):
        self.cards = [Card(rank, suit) for rank in Rank for suit in Suit]
        random.shuffle(self.cards)
    def draw(self):
        return self.cards.pop()
# Define hand class
class Hand:
    def __init__(self):
        self.cards = []
    def add_card(self, card):
        self.cards.append(card)
    def calculate_value(self):
        value = sum(card.rank.value for card in self.cards)
        num_aces = sum(1 for card in self.cards if card.rank == Rank.ACE)
        while value > 21 and num_aces:
            value -= 10
            num_aces -= 1
        return value
    def __repr__(self):
        return ', '.join(map(str, self.cards))
# Define game class
class BlackjackGame:
    def __init__(self):
        self.deck = Deck()
        self.player_hand = Hand()
        self.dealer_hand = Hand()
    def initial_deal(self):
        for _ in range(2):
            self.player_hand.add_card(self.deck.draw())
            self.dealer_hand.add_card(self.deck.draw())
    def display_hands(self, reveal_dealer=False):
        print(f"your hand: {self.player_hand} - Value: {self.player_hand.calculate_value()}")
        if reveal_dealer:
            print(f"Dealer's hand: {self.dealer_hand} - Value: {self.dealer_hand.calculate_value()}")
        else:
            print(f"Dealer's hand: {self.dealer_hand.cards[0]} and [Hidden]")
    def player_turn(self):
        while True:
            action = input("Do you want to 'hit' or 'stand'? ").lower()
            if action == 'hit':
                self.player_hand.add_card(self.deck.draw())
                print(f"You drew: {self.player_hand.cards[-1]}")
                if self.player_hand.calculate_value() > 21:
                    print("You bust!")
                    return False
            elif action == 'stand':
                return True
            else:
                print("Please enter 'hit' or 'stand'.")
            if self.player_hand.calculate_value() == 21:
                return "player wins"
            elif self.dealer_hand.calculate_value() == 21:
                    pass
    def dealer_turn(self):
        while self.dealer_hand.calculate_value() < 17:
            self.dealer_hand.add_card(self.deck.draw())
        if self.dealer_hand.calculate_value() > 21:
            print("Dealer busts!")
        if self.dealer_hand.calculate_value() == 21:
            print("Dealer wins!")
        elif self.player_hand.calculate_value() == 21:
            pass       
# defines how the player or cpu wins
    def determine_winner(self):
        player_value = self.player_hand.calculate_value()
        dealer_value = self.dealer_hand.calculate_value()
        if player_value > 21:
            return "you busts. Dealer wins!"
        elif dealer_value > 21:
            return "you won! Dealer busts."
        elif player_value > dealer_value:
            return "you won"
        elif player_value < dealer_value:
            return "Dealer wins!"
        else:
            return "Its a tie!"
    def play(self):
        self.initial_deal()
        self.display_hands()
        if self.player_turn():
            self.dealer_turn()
        self.display_hands(reveal_dealer=True)
        print(self.determine_winner())
# Main function to start the game
if __name__ == "__main__":
    while True:
        print("\nWelcome to Blackjack!")
        game = BlackjackGame()
        game.play()
        again = input("Do you want to play again? (yes/no) ").lower()
        if again != 'yes':
            print("Thanks for playing!")
            break
        game.play()
        again = input("Do you want to play again? (yes/no) ").lower()
        if again != 'yes':
            print("Thanks for playing!")
            break
