from random import randint


class BlackjackGame:
    ''' Class representing a Blackjack game. '''
    def __init__(self):
        ''' Initialize the BlackjackGame Instance. '''
        self.CHIPS = 50
        self.SUM_PL_CARDS = 0
        self.SUM_DL_CARDS = 0
        self.HAS_BLACKJACK = False
        self.IS_IN_GAME = False
        self.MESSAGE_DL = ''
        self.MESSAGE = ''
        self.CARD_DECK_Pl = []
        self.CARD_DECK_Dl = []
        self.PLAYER = {'name': 'Player', 'chips': 1000}

    def shuffle_new_card(self):
        '''
        Shuffle and return a new card value.

        Returns:
        int: A random card value between 1 and 11.

        '''
        random_num = randint(1, 13)
        if random_num > 10:
            return 10
        elif random_num == 1:
            return 11
        else:
            return random_num

    def start_game(self):
        '''
        Starts the game by initializing player's and dealer's cards.

        Returns:
        dict: Dictionary with game state.

        '''
        self.IS_IN_GAME = True

        # Initialize player's cards.
        card_one_player = self.shuffle_new_card()
        card_two_player = self.shuffle_new_card()
        self.CARD_DECK_Pl = [card_one_player, card_two_player]
        self.SUM_PL_CARDS = sum(self.CARD_DECK_Pl)

        # Initialize dealer's card.
        card_one_dl = self.shuffle_new_card()
        card_two_dl = self.shuffle_new_card()
        self.CARD_DECK_Dl = [card_one_dl, card_two_dl]
        self.SUM_DL_CARDS = sum(self.CARD_DECK_Dl)
        

        # Return a dictionary with game state.
        return self.render_game()

    def render_game(self):
        '''
        Renders the game state, updates messages, and displays cards.

        Returns:
        dict: Dictionary with updated game state.
        '''

        # Update messages based on game logic.
        if self.SUM_DL_CARDS == 21:
           self.MESSAGE_DL = "Table Wins Black Jack!"
           self.MESSAGE = "Player lost!"
           self.PLAYER['chips'] -= self.CHIPS
           self.IS_IN_GAME = False
        elif self.SUM_PL_CARDS == 21:
            self.MESSAGE = "Player wins Black Jack!"
            self.PLAYER['chips'] += self.CHIPS
            self.HAS_BLACKJACK = True
        elif self.SUM_PL_CARDS == self.SUM_DL_CARDS:
            self.MESSAGE = "It's TIE!"
        elif self.SUM_PL_CARDS <= 20:
            self.IS_IN_GAME = True
            self.MESSAGE = "Would you like to hit?"
        elif self.SUM_PL_CARDS > 21:
            self.MESSAGE = "Player lost a Bet!"
            self.PLAYER['chips'] -= self.CHIPS
            self.IS_IN_GAME = False

        # Return a dictionary with updated game state.
        return {
            'CARD_DECK_Pl': self.CARD_DECK_Pl,
            'CARD_DECK_Dl': self.CARD_DECK_Dl,
            'SUM_DL_CARDS': self.SUM_DL_CARDS,
            'SUM_PL_CARDS': self.SUM_PL_CARDS,
            'MESSAGE_DL': self.MESSAGE_DL,
            'MESSAGE': self.MESSAGE,
            'PLAYER_NAME': self.PLAYER['name'],
            'PLAYER_CHIPS': self.PLAYER['chips'],
        }

    def new_card(self):
        '''
        Draws a new card for the player and updates the game state.

        Returns:
        dict: Dictionary with updated game state.
        '''

        # Default value of new card.
        player_card = None

        if self.IS_IN_GAME and not self.HAS_BLACKJACK:
            player_card = self.shuffle_new_card()
            self.SUM_PL_CARDS += player_card
            self.CARD_DECK_Pl.append(player_card)

        # Return a dictionary with updated game state.
        return {
            'SUM_DL_CARDS': self.SUM_DL_CARDS,
            'SUM_PL_CARDS': self.SUM_PL_CARDS,
            'MESSAGE_DL': self.MESSAGE_DL,
            'MESSAGE': self.MESSAGE,
            'PLAYER_NAME': self.PLAYER['name'],
            'PLAYER_CHIPS': self.PLAYER['chips'],
            'CARD_DECK_Pl': self.CARD_DECK_Pl,
        }
