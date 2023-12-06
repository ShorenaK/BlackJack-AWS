import unittest
from app_blackjack import BlackjackGame


class TestBlackjackGame(unittest.TestCase):
    def setUp(self):
        '''Set up a new instance of the BlackjackGame'''
        self.blackjack_game = BlackjackGame()
        
    def test_shuffle_new_card(self):
        '''Test the shuffle_new_card function.'''
        card = self.blackjack_game.shuffle_new_card()
        self.assertTrue(1 <= card <= 11, "A card value should be between 1 and 11.")


    def test_start_game(self):
        '''Test the start_game function.'''
        # Call the start_game function to initialize the game.
        game_state = self.blackjack_game.start_game()

        # Assertions based on the expected initial game state.
        self.assertTrue(game_state['IS_IN_GAME'], "Game should be in progress.")
        self.assertEqual(game_state['MESSAGE'], "", "Initial message should be empty.")
        self.assertEqual(game_state['SUM_DL_CARDS'], game_state['CARD_DECK_Dl'][0] + game_state['CARD_DECK_Dl'][1], "Dealer's total should be the sum of the first two cards.")
        self.assertEqual(game_state['SUM_PL_CARDS'], game_state['CARD_DECK_Pl'][0] + game_state['CARD_DECK_Pl'][1], "Player's total should be the sum of the first two cards.")
        

    def test_render_game(self):
        '''Test the render function'''
        # Set up the game state.
        self.blackjack_game.start_game()
         # Call render_game to update the game state.
        game_state = self.blackjack_game.render_game()
        
        # Assertions based on the expected rendederd game state.
        self.assertEqual(game_state['SUM_DL_CARDS'], int(game_state['CARD_DECK_Dl'][0]) + int(game_state['CARD_DECK_Dl'][1]), "Dealer's total should be the sum of the first two cards.")
        # self.assertEqual(game_state['SUM_DL_CARDS'], game_state['CARD_DECK_Dl'][0] + game_state['CARD_DECK_Dl'][1], "Dealer's total should be the sum of the first two cards.")
        self.assertEqual(game_state['SUM_PL_CARDS'], game_state['CARD_DECK_Pl'][0] + game_state['CARD_DECK_Pl'][1], "Player's total should be the sum of the first two cards.")
        self.assertEqual(game_state['MESSAGE_DL'], "", "Dealer's message should be empty.")
        self.assertEqual(game_state['MESSAGE'], "Would you like to hit?", "Player's message should be 'Would you like to hit?'.")
        if game_state['CARD_DECK_Dl']:
            self.assertEqual(game_state['SUM_DL_CARDS'], int(game_state['CARD_DECK_Dl'][0]) + int(game_state['CARD_DECK_Dl'][1]), "Dealer's total should be the sum of the first two cards.")
        else:
            self.assertEqual(game_state['SUM_DL_CARDS'], 0, "Dealer's total should be 0.")


    def test_new_card(self):
        '''Test the new_card funtion'''
       # Set up the game state by starting the game.
        self.blackjack_game.start_game()
        
        # Call new_card to draw a new card
        game_state = self.blackjack_game.new_card()
        
        # Assertions based on the expected new game state.
        self.assertEqual(len(game_state['CARD_DECK_Pl']), 1, "One new card should be added to the player's deck.")
        self.assertEqual(len(game_state['CARD_DECK_Pl']), 2, "Two new cards should be added to the player's deck.")
        self.assertEqual(game_state['SUM_PL_CARDS'], game_state['CARD_DECK_Pl'][0], "Player's total should be updated correctly.")
        self.assertEqual(game_state['SUM_DL_CARDS'], int(game_state['CARD_DECK_Dl'][0]) + int(game_state['CARD_DECK_Dl'][1]), "Dealer's total should be the sum of the first two cards.")
        self.assertEqual(len(game_state['CARD_DECK_Pl']), 3, "One new card should be added to the player's deck.")
        self.assertEqual(game_state['MESSAGE'], "", "Player's message should be empty.")
        self.assertTrue(game_state['IS_IN_GAME'], "Game should still be in progress.")

if __name__ == '__main__':
    unittest.main()
    
    
