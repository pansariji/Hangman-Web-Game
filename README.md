Hangman Web Application

Overview of the project

This project is a fully responsive, web-based implementation of the classic Hangman word guessing game. It transforms the traditional paper-and-pencil game into an interactive digital experience. The application features a Python-based backend using Flask to handle game logic and sessions securely, paired with a modern HTML/CSS frontend for a smooth user interface. It is designed to be deployed easily on cloud platforms like Render.

Features

- Interactive Virtual Keyboard: Players can click on-screen buttons to guess letters, which disable automatically after selection.
- Dynamic Visual Feedback: The "Hangman" stick figure updates progressively (from  h1.png to  h7.png ) with every incorrect guess.
- Score Tracking: The application tracks the player's score across multiple rounds within a session.
- Responsive Design: The layout automatically adjusts for desktop, tablet, and mobile screens using Tailwind CSS.
- Secure Game Logic: All word validation and game state management occur on the server side to prevent cheating.
- Session Persistence: Uses Flask Sessions to maintain the game state even if the browser is refreshed.

Technologies/tools used

- Programming Language: Python 3.x
- Web Framework: Flask
- Frontend: HTML5, JavaScript
- Styling: Tailwind CSS
- Version Control: Git & GitHub
- Deployment: Render
- Dependencies: flask

Steps to install & run the project

1. Prerequisites

Ensure you have Python 3.x installed on your system.

2. Clone or Download the Repository

Download the project files to your local machine and navigate to the project folder in your terminal/command prompt.

3. Install Dependencies

Install the necessary Python libraries using  pip :

pip install flask 

5. Run the Application

Start the local development server:

python app.py

6. Access the Game

Open your web browser and go to the following URL:

[http://127.0.0.1:5000](http://127.0.0.1:5000)

6\. Play game on: https://hangman-web-game.onrender.com

Instructions for testing

To ensure the application is working correctly, follow these testing steps:

1. Start a Game: Load the webpage. Verify that the score is 0, the word display shows dashes (e.g.,  \_ \_ \_ \_ ), and the keyboard is visible.
1. Test Correct Guess: Click a letter you suspect is in the word (e.g., vowels like 'A' or 'E').
   1. Expected Result: The letter appears in the correct position(s) in the word display. The button becomes disabled.
1. Test Incorrect Guess: Click a letter that is likely not in the word (e.g., 'Z' or 'Q').
   1. Expected Result: The hangman image updates (drawing part of the figure), and the error count increases (e.g., "Errors: 1/6").
1. Test Win Condition: Continue guessing correct letters until the word is complete.
   1. Expected Result: A "YOU WON!" message appears, the score increments by 1, and a "Play Again" button becomes visible.
1. Test Lose Condition: Intentionally guess wrong 6 times.
- Expected Result: A "YOU LOST!" message appears revealing the correct word, the score resets to 0 (unless configured otherwise), and the "Play Again" button appears.
6. Test Restart: Click the "Play Again" button.
- Expected Result: The board resets with a new hidden word, the hangman image resets, and the keyboard buttons are re- enabled.
