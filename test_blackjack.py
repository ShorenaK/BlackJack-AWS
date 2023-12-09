import unittest
from app_blackjack import BlackjackGame

# To create class TestBalckJackGame
class TestBlackjackGame(unittest.TestCase):
    def setUp(self):
        '''Set up a new instance of the BlackjackGame'''
        self.blackjack_game = BlackjackGame()

    # To test start_game funtcion
    def test_start_game(self):
        '''Test the start_game function.'''
        # Call the start_game function to initialize the game.
        game_state = self.blackjack_game.start_game()

        # Assertions based on the expected initial game state.
        self.assertTrue(game_state.get('IS_IN_GAME', True), "Game should be in progress.")
        self.assertIn('CARD_DECK_Dl', game_state, "Dealer's card deck should be present.")
        self.assertIn('CARD_DECK_Pl', game_state, "Player's card deck should be present.")

    # To test render_game function
    def test_render_game(self):
        # Start the game and draw five new cards for the player.
        self.blackjack_game.start_game()
        for _ in range(5):  # Draw 5 cards
            self.blackjack_game.new_card()

        # Render the game state and perform assertions.
        game_state = self.blackjack_game.render_game()
        print("game state", game_state)
        expected_cards = min(5, len(game_state.get('CARD_DECK_Pl', [])))
        self.assertLessEqual(expected_cards, 5, "Player should have 5 cards or less.")
        self.assertEqual(game_state['SUM_PL_CARDS'], sum(game_state.get('CARD_DECK_Pl', [])), "Player's total should be updated correctly.")

        # Check if the game is still in progress or ended due to exceeding 21.
        if game_state['SUM_PL_CARDS'] > 21:
            self.assertFalse(game_state.get('IS_IN_GAME', False), "Game should be over if the player loses.")
            self.assertTrue(game_state['MESSAGE'].startswith("Player lost a Bet"), "Game should be over if the player loses.")
        else:
            self.assertTrue(game_state.get('IS_IN_GAME', False), "Game should still be in progress.")
            self.assertEqual(game_state['MESSAGE'], "", "Player's message should be empty.")

   # To test test_new_card function 
    def test_new_card(self):
        '''Test the new_card function'''
        # Set up the game state by starting the game.
        self.blackjack_game.start_game()

        # Call new_card to draw a new card
        game_state = self.blackjack_game.new_card()

        # Assertions based on the expected new game state.
        if game_state.get('CARD_DECK_Dl'):
            # If the game is still in progress
            self.assertEqual(game_state['SUM_DL_CARDS'], int(game_state['CARD_DECK_Dl'][0]) + int(game_state['CARD_DECK_Dl'][1]), "Dealer's total should be the sum of the first two cards.")
        else:
            # If the game is over
            self.assertNotIn('CARD_DECK_Dl', game_state, "Dealer's card deck should not be present in the game over state.")

if __name__ == '__main__':
    unittest.main()