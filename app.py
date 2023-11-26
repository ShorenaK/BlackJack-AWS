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


    
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(port=8000, debug=True, use_reloader=True)