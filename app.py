import random
from flask import Flask, render_template, request, jsonify, session

# Initialize Flask application
app = Flask(__name__)
# IMPORTANT: Session secret key required to store game state
app.secret_key = 'a_very_secret_key_for_hangman' 

# List of words from your original code
WORDS = ['programming', 'data', 'python', 'code', 'geeks', 'computer', 'engineer', 'word', 'science', 
         'machine', 'java', 'college', 'player', 'mobile', 'image']

MAX_INCORRECT_GUESSES = 6 # Corresponds to your 7 hangman images (h1-h7)

def initialize_game():
    """Sets up a new game session."""
    word = random.choice(WORDS)
    session['word'] = word.lower()
    session['guessed_letters'] = []
    session['incorrect_guesses'] = 0
    session['score'] = session.get('score', 0)
    session['display_word'] = ['_' for _ in word]
    print(f"New word: {word}") # For testing/debugging
    
@app.route('/')
def index():
    """Renders the main game page."""
    if 'word' not in session:
        initialize_game()
    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def guess():
    """Handles a letter guess from the user."""
    letter = request.json.get('letter').lower()
    
    # Check if the letter has already been guessed
    if letter in session['guessed_letters']:
        return jsonify(get_game_state(message="You already guessed that letter!"))

    # Add to guessed letters
    session['guessed_letters'].append(letter)
    word = session['word']
    
    if letter in word:
        # Correct guess: reveal letters
        for i, char in enumerate(word):
            if char == letter:
                session['display_word'][i] = letter.upper()
        
        # Check for win
        if '_' not in session['display_word']:
            session['score'] += 1
            game_over = True
            message = "YOU WON! Click 'Play Again' to start the next round."
        else:
            game_over = False
            message = "Correct guess!"
    else:
        # Incorrect guess: increment count
        session['incorrect_guesses'] += 1
        
        # Check for loss
        if session['incorrect_guesses'] >= MAX_INCORRECT_GUESSES:
            game_over = True
            session['score'] = 0 # Reset score on loss, as per your original logic
            message = f"YOU LOST! The word was: {word.upper()}. Click 'Play Again' to restart."
        else:
            game_over = False
            message = "Incorrect guess!"

    return jsonify(get_game_state(message=message, game_over=game_over))

@app.route('/restart', methods=['POST'])
def restart():
    """Restarts the game, keeping the current score if the previous round was won."""
    initialize_game()
    return jsonify(get_game_state(message="Game started. Good luck!"))

def get_game_state(message="", game_over=False):
    """Compiles the current game state into a dictionary for JSON response."""
    # The hangman image uses incorrect_guesses + 1 (h1 to h7)
    hangman_img_index = session['incorrect_guesses'] + 1 
    if hangman_img_index > 7:
        hangman_img_index = 7 # Cap at the final lost image
        
    return {
        'display_word': ' '.join(session['display_word']),
        'guessed_letters': list(session['guessed_letters']),
        'incorrect_count': session['incorrect_guesses'],
        'hangman_img': f'h{hangman_img_index}',
        'score': session['score'],
        'message': message,
        'game_over': game_over
    }

if __name__ == '__main__':
    # Run the server on http://127.0.0.1:5000/
    app.run(debug=True)