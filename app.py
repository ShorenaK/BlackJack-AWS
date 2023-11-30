from flask import Flask, render_template, redirect, url_for, jsonify, render_template, request
from random import randint

app = Flask(__name__)

# Initialize global variables
CHIPS = 50
SUM_PL_CARDS= 0
SUM_DL_CARDS = 0 
HAS_BLACKJACK = False
IS_IN_GAME = False
MESSAGE_DL = []
MESSAGE = ''
CARD_DECK_Pl = []
CARD_DECK_DL = []
PLAYER = {
    'name': 'Player',
    'chips': 1000
}

def shuffle_new_card():
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
    

def start_game():
    '''
    Starts the game by initializing player's and dealer's cards.
    '''
    global SUM_PL_CARDS, SUM_DL_CARDS, CARD_DECK_Pl, CARD_DECK_DL, IS_IN_GAME
    IS_IN_GAME = True
    card_one_player = shuffle_new_card()
    card_two_player = shuffle_new_card()
    CARD_DECK_Pl = [card_one_player, card_two_player]
    SUM_PL_CARDS = card_one_player + card_two_player
    
    card_one_dl = shuffle_new_card()
    card_two_dl = shuffle_new_card()
    CARD_DECK_DL = [card_one_dl, card_two_dl]
    SUM_DL_CARDS = card_one_dl + card_two_dl 
    
    # Return a JSON response with game state
    return jsonify({
        'SUM_DL_CARDS': SUM_DL_CARDS,
        'SUM_PL_CARDS': SUM_PL_CARDS,
        'MESSAGE_DL': MESSAGE_DL,  
        'MESSAGE': MESSAGE,
        'PLAYER_CHIPS': PLAYER['chips'],
    })

def render_game():
    '''
    Renders the game state, updates messages, and displays cards.
    '''
    global MESSAGE, MESSAGE_DL, SUM_PL_CARDS, SUM_DL_CARDS, CARD_DECK_Pl, CARD_DECK_DL, PLAYER, HAS_BLACKJACK, IS_IN_GAME

    # Update total values
    total_dl_tag = f'Total: {SUM_DL_CARDS}'
    total_tag = f'Total: {SUM_PL_CARDS}'
    
    # Update messages based on game logic
    if SUM_DL_CARDS == 21:
        MESSAGE_DL = "Table Wins Black Jack!!!"
        MESSAGE = "Player lost!"
        PLAYER['chips'] -= CHIPS
        IS_IN_GAME = False
        
    elif SUM_PL_CARDS == 21:
        MESSAGE = "Player wins Black Jack!!!"
        PLAYER['chips'] += CHIPS
        HAS_BLACKJACK = True
        
    elif SUM_PL_CARDS == SUM_DL_CARDS:
        MESSAGE_DL = "It's TIE"
        MESSAGE = "It's TIE"
        
    elif SUM_PL_CARDS <= 20:
        IS_IN_GAME = True
        MESSAGE = "Would you like to hit?"
        
    elif SUM_PL_CARDS > 21:
        MESSAGE = "Bust! You lost a Bet!"
        PLAYER['chips'] -= CHIPS
        IS_IN_GAME = False

    # Update Player's chips
    player_chips_tag = f"{PLAYER['name']} has {PLAYER['chips']} chips"
    
    # Return HTML content as a response
    return jsonify({
        'SUM_DL_CARDS': SUM_DL_CARDS,
        'SUM_PL_CARDS': SUM_PL_CARDS, 
        'MESSAGE_DL': MESSAGE_DL,
        'MESSAGE': MESSAGE,
        'PLAYER_CHIPS': PLAYER['chips'],
        'CARD_DECK_PL': CARD_DECK_Pl,  # Pass the array of player's cards to the template
        'CARD_DECK_DL': CARD_DECK_DL,  # Pass the array of dealer's cards to the template
        'HTML_CONTENT': render_template('index.html', message=MESSAGE, messageDl=MESSAGE_DL, total=total_tag, totalDl=total_dl_tag, player_chips=player_chips_tag),
    })

def new_card():
    '''
    Draws a new card for the player and updates the game state.
    '''
    global SUM_PL_CARDS, CARD_DECK_Pl
    if IS_IN_GAME and not HAS_BLACKJACK:
        card = shuffle_new_card()
        SUM_PL_CARDS += card
        CARD_DECK_Pl.append(card)
    
    return jsonify({
        'SUM_DL_CARDS': SUM_DL_CARDS,
        'SUM_PL_CARDS': SUM_PL_CARDS,
        'MESSAGE_DL': MESSAGE_DL,
        'MESSAGE': MESSAGE,
        'PLAYER_CHPS': PLAYER['chips'],  
    })

# Flask route for rendering the game page
@app.route('/')
def index():
    return render_template('index.html')

# Flask route for rendering the main casino page
@app.route('/indexmain')
def indexmain():
    return render_template('indexmain.html')

# Flask route for handling game actions
@app.route('/game_action/<action>')
def game_action(action):
    '''
    Handles game actions such as starting the game or drawing a new card.
    
    Args:
        action (str): The action to perform ('startTheGame' or 'newCard')
    
    Returns:
        str: HTML page with the updated game state.
    '''
    global SUM_PL_CARDS, SUM_DL_CARDS, HAS_BLACKJACK, IS_IN_GAME, MESSAGE_DL, MESSAGE, CARD_DECK_Pl, CARD_DECK_DL, PLAYER
    
    if action == 'startTheGame':
        return start_game()
    elif action == 'newCard':
        return new_card()

if __name__ == "__main__":
    app.run(port=8008, debug=True, use_reloader=True)

