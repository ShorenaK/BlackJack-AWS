from flask import Flask, render_template, url_for
from random import randint

app = Flask(__name__)

# Initialize global variable
CHIPS = 50
SUM = 0
SUM_DL_CARDS = 0 
HAS_BLACKJACK = False
IS_IN_GAME = False
MESSAGE_DL = []
MESSAGE = ''
CARD_DECK = []
CARD_DECK_DL = []
PLAYER = {
    'name': 'Player',
    'chips': 1000
}
def shuffle_new_card():
    '''
    Suffles and retunrs a new card value.
    
    Retunrs:
    int A random card value between 1 and 11. 
    
    '''
    random_num = randint(1, 13)
    if random_num > 10:
        return 10
    elif random_num == 1:
        return 11
    else:
        return random_num

def start_game():
    '''
    Starts the game by initializing player's and dealer's cards.
    '''
    global SUM, SUM_DL_CARDS, CARD_DECK, CARD_DECK_DL, IS_IN_GAME
    IS_IN_GAME = True
    card_one = shuffle_new_card()
    card_two = shuffle_new_card()
    CARD_DECK = [card_one, card_two]
    SUM = card_one + card_two
    card_one_dl = shuffle_new_card()
    card_two_dl = shuffle_new_card()
    CARD_DECK_DL = [card_one_dl, card_two_dl]
    SUM_DL_CARDS = card_one_dl + card_two_dl 
    render_game()

def render_game():
    '''
    Renders the game state, upadates messages, displays cards.
    '''
    global MESSAGE, MESSAGE_DL, SUM, SUM_DL_CARDS, CARD_DECK, CARD_DECK_DL, PLAYER

    # Display dealer's cards
    dl_cards_tag = "Dealer's Cards: "
    for card in CARD_DECK_DL:
        dl_cards_tag += f'{card} '
        
    # Desplay player's cards
    cards_tag = "Player's Cards: "
    for card in CARD_DECK:
        cards_tag += f'{card} '
    
    # Update total values
    total_dl_tag = f'Total: {SUM_DL_CARDS}'
    total_tag = f'Total: {SUM}'
    
    # Update message
    message_dl = MESSAGE_DL if MESSAGE_DL else ''
    message = MESSAGE if MESSAGE else ''
    
    # Update Player's chips
    player_chips_tag = f"{PLAYER['name']} has {PLAYER['chips']} chips"
    
    return render_template('index.html', message=message, messageDl=message_dl, total=total_tag, totalDl=total_dl_tag, player_chips=player_chips_tag, cardDeck=CARD_DECK, cardDeckDl=CARD_DECK_DL, dlCardsTag=dl_cards_tag, cardsTag=cards_tag)
    

def new_card():
    '''
    Draws a new card for the player and updates two game state.
    
    '''
    global SUM, CARD_DECK
    if IS_IN_GAME and not HAS_BLACKJACK:
        card = shuffle_new_card()
        SUM += card
        CARD_DECK.append(card)
        render_game()

# Flask route for rendering the game page
@app.route('/')
def index():
    return render_template('index.html')

# Flask route for rendering the main casino page
@app.route('/indexmain')
def indexmain():
    return render_template('indexmain.html')

# Flask route for handling game actions
@app.route('/game_action/action')
def game_action(action):
    '''
    Handles game actions such as start the game or drawing a new card.
    
    Args:
        action (str): The action to perform ('startTheGame' or 'newCard')
    
    Returns:
        str: HTML page with the updated game state.
    '''
    global SUM, SUM_DL_CARDS, HAS_BLACKJACK, IS_IN_GAME, MESSAGE_DL, MESSAGE, CARD_DECK, CARD_DECK_DL, PLAYER
    
    if action == 'startTheGame':
        start_game()
    elif action == 'newCard':
        new_card()
        
    return render_template('indexmain.html', message=MESSAGE, messageDl=MESSAGE_DL, total=SUM, totalDl=SUM_DL_CARDS, player_chips=PLAYER['chips'], cardDeck=CARD_DECK, cardDeckDl=CARD_DECK_DL)

if __name__ == "__main__":
    app.run(port=8008, debug=True, use_reloader=True)