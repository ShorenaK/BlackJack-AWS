## Shorena K. Anzhilov CS5001 Final Project - "BlackJack Game"

## Game Descriptiion:
The "BlackJack" card game is tailored for one player competing against the dealer. The game begins with the player clicking the "Start the game" button, prompting the shuffling of two cards for the player. The objective is to beat the dealer by achieving a score as close to 21 as possible or hitting 21 itself.

After the initial card deal, players can draw a new card using the "New Card" button. If the cumulative card value exceeds 21, the player receives a "You lost a Bet!" message. Achieving a card value of 21 results in a victory for the player, with an additional 50 chips added to the total. Player starts with 1000 chips, and winning earns a 50 chips, while losing deducts 50 chips.

Card values from 2 to 10 correspond to their face value, and Jack, Queen, and King are valued at 10. The default value of an Ace is set to 11 but can be changed to one. Notably, the game uses a unique approach, displaying only numerical representations.

In case of a tie, where both the player and the dealer have the same card value, a "It's a TIE" message is displayed. If the dealer hits Black Jack, the player automatically loses, with 50 chips deducted and the message "'Table Wins Black Jack! is displayed"

A third button " End Game" is incorporated for navigation to the main page, serving as the entrance to the casino and the starting point to enter Black Jack Table.

## Preview 
![alt text](/static/images/new_back.png)
![alt text](/static/images/image1.png)


## Go to app:
[CLICK HERE!]()


## Technologies Implemented - Tech Stack:

- Server-side: Python3, Flask
- Frontend: HTML, JavaScript (with Ajax for asynchronous requests)
- CSS

Description:

Server-side: The backend of the application is powered by Python3 with the Flask lightwaight web framework, handling the game logic and serving responses to client requests.

Frontend: The user interface is built using HTML for structure, JavaScript for dynamic interactions (including Ajax for asynchronous communication with the Flask server), and CSS for styling.

## Resources:
- 1. [Flask Documentation](https://flask.palletsprojects.com/en/2.0.x/): Official documentation for Flask, the web framework used in this project.
- 2. [JQuery Documentation](https://api.jquery.com/): Documentation for JQuery, a JavaScript library used for making asynchronous requests in this project.
- 3. [Python Documentation](https://docs.python.org/3/): Official documentation for the Python programming language.
- 4. [Blackjack Rules](https://bicyclecards.com/how-to-play/blackjack/): A resource explaining the basic rules of Blackjack for reference.
- 5. [CSS Tricks](https://css-tricks.com/): Helpful tips and tricks for working with CSS.

- 6. [Flask Tutorial](https://flask.palletsprojects.com/en/2.0.x/tutorial/): Step-by-step guide for getting started with Flask. A great resource if you're new to Flask development.
- Stak OverFlow

## Missing Features:
- Multiplayer Support
- User Authentication
- Graphics and Animation
- Sound Effects
- Betting Options
- Game Statistics

## Next Steps - Features Implementations:
1. Multiplayer Functionality:
Enhance the gaming experience by introducing multiplayer functionality, allowing multiple players to compete against the dealer.

2. User Authentication:
Implement user authentication to provide a personalized gaming experience and enable tracking of individual player statistics.

3. Game Statistics:
Introduce a statistics feature to keep track of players' performance, including win-loss records and other relevant gameplay metrics.

4. Dealer's Unrevealed Cards:
Mimic the real blackjack experience by initially keeping all of the dealer's cards unrevealed. Unveil the cards as the game progresses, following the player's actions.

5. Enhanced Dealer Interaction:
Create a more realistic gaming environment by allowing the dealer to draw a third card based on specific conditions, similar to real blackjack rules.

6. Improved User Interface:
Enhance the user interface to provide a visually appealing and intuitive gaming experience for players.

7. Integration of Real Blackjack Rules:
Further align the game with traditional blackjack rules, ensuring a more authentic representation of the classic card game.

## Challenges:

## Highlights:  


## Developer:
- [Shorena K. Anzhilov](https://github.com/ShorenaK)


## Support: 
 If you have any concerns or questions, you are welcome to reach out via email at skadigitalllc@gmail.com 