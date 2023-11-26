from flask import Flask, render_template
from random import randint

app = Flask(__name__)

# Initialize global variable
CHIPS = 50
SUM = 0
SUM_DL_CARDS = 0 
HAS_BLACKJACK = False
IS_IN_GAME = False
MESSAGE_DL = []
MASSAGE = ''
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
    

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(port=8000, debug=True, use_reloader=True)