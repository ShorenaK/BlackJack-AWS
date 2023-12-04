import unittest
from app.py import BlackjackGame

class TestBlackjackGame(unittest.TestCase):
    def setUp(self):
        '''Set up a new instance of the BlackjackGame'''
        self.blackjack_game = BlackjackGame()
        
    def test_shuffle_new_card(self):
        '''Test the shuffle_new_card function.'''
        card = self.blackjack_game.shuffle_new_card()
        self.assertTrue(1 <= card <= 11, " A card value should be between 1 and 11." )
        
    
    