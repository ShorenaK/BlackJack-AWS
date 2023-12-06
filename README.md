## Shorena K. Anzhilov CS5001 Final Project - "BlackJack Game"

## Game Descriptiion:
The "BlackJack" card game is tailored for one player competing against the dealer. The game begins with the player clicking the "Start the game" button, prompting the shuffling of two cards for the player. The objective is to beat the dealer by achieving a score as close to 21 as possible or hitting 21 itself.

After the initial card deal, players can draw a new card using the "New Card" button. If the cumulative card value exceeds 21, the player receives a "You lost a Bet!" message. Achieving a card value of 21 results in a victory for the player, with an additional 50 chips added to the total. Player starts with 1000 chips, and winning earns a 50 chips, while losing deducts 50 chips.

Notably, the game uses a unique approach, displaying only numerical representations.

In case of a tie, where both the player and the dealer have the same card value, a "It's a TIE" message is displayed. If the dealer hits Black Jack, the player automatically loses, with 50 chips deducted and the message "'Table Wins Black Jack! is displayed"

A third button " End" is incorporated for navigation to the main page, and to end the game. The main page is serving as the entrance to the casino and the starting point to enter Black Jack Table.

## Preview 
![alt text](/static/images/new_back.png)
![alt text](/static/images/image1.png)


## Go to app:
[CLICK HERE!]()


## Technologies Implemented - Tech Stack:

- Server-side: Python3, Flask
- Frontend: HTML, JavaScript (with Ajax for asynchronous requests)
- CSS
- Hosted and deployed on AWS (Amazon Web Services). 

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
- Google & Stak OverFlow.

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

#### I encountered challenges while running unit tests on a Python file with Flask framework.RuntimeError specifically: "Working outside of application context." Additionally, faced "Unable to build URLs outside an active request" due to missing configurations like 'SERVER_NAME' and 'APPLICATION_ROOT.

### Steps Taken:

-  Added Flask app context using self.app.app_context().
-  Modified the BlackjackGame class to handle both Flask and non-Flask contexts.
-  Separated Flask-dependent logic to run only when the context is available.

![alt text](/static/images/git_self_app1.png)

![alt text](/static/images/git_self_app2.png)

### Persisting Issue:

#### Despite these changes, a RuntimeError persisted, indicating Flask's inability to build URLs outside an active request. I think a configuration change is needed, but I haven't found the solution yet.

### Alternate Approach:
#### To ensure unit testing functionality, I have created a separate Python file, app_blackjack.py, detached from Flask, it is only for testing purposes. This file is connected to test_blackjack.py file, to run unittests. 

![alt text](/static/images/git_test1.png)

![alt text](/static/images/git_test2.png)

## Highlights:  

- Multilingual Development: Crafted the project using a combination of Python and JavaScript.

- Learning AJAX: Implemented AJAX to enhance the project's scripting capabilities.

- Python Flask Framework: Leveraged the Python Flask framework for efficient development.

- AWS Deployment: Successfully deployed the project on AWS, specifically on an Amazon Web Server (AWS) EC2 instance. Witnessing it live for the first time was truly fulfilling.

## Developer:
- [Shorena K. Anzhilov](https://github.com/ShorenaK)



## Support: 
 If you have any concerns or questions, you are welcome to reach out via email at skadigitalllc@gmail.com 
