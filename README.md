# Pontoon (Python)

A simple terminal-based implementation of Pontoon / Twenty-One, written in Python. The game uses a standard 52-card deck, supports coloured terminal output using colorama, and includes several classic Pontoon rules such as Pontoon hands, Five Card Tricks, dealer advantage on ties, and mandatory hits below 15.

## Features
- Standard 52-card deck
- Deck shuffling
- Alternate dealing between player and dealer
- Automatic hand scoring
- Face card scoring (Jack, Queen, King = 10)
- Flexible Ace scoring (1 or 11)
- Pontoon detection (Ace + 10-value card)
- Five Card Trick detection
- Input validation
- Dealer AI
- Colour-coded terminal output

## Rules
### Pontoon

A Pontoon is:

- Ace + 10
- Ace + Jack
- Ace + Queen
- Ace + King

Pontoon is the highest-ranking hand.

### Five Card Trick

A Five Card Trick occurs when a player reaches five cards without going bust.

A Five Card Trick beats a normal score of 21.

### Standing Rules

The player:

- Must hit when their score is below 15
- May stand when their score is 15 or higher

The dealer:

- Draws cards until their score matches or exceeds the player's score
- Wins ties
- Can achieve a Five Card Trick
- Busts if they exceed 21

### Hand Rankings

Highest to lowest:

- Pontoon
- Five Card Trick
- 21
- 20
- 19
- 18
- 17
- 16
- 15

Dealer wins any tied scores.

## Requirements

- Install Colorama:

  pip install colorama

## Running the game

- Run the Python file

  python pontoon.py

## Example gameplay

Player 1

Current hand:

King of Hearts
7 of Clubs

Score: 17

What would you like to do? (S = Stand, H = Hit)

H

Current hand:

King of Hearts
7 of Clubs
2 of Diamonds

Score: 19

## Project Structure

- score_hand(hand)

Calculates the value of a hand, including Ace handling.

- print_hand(hand, owner)

Displays a player's cards and current score.

- pontoon_check(hand)

Checks whether a hand contains a Pontoon.

## Potential features for future versions:

- Multiple rounds / replay option
- Betting system
- Split pairs
- Double down
- Suit symbols (♥ ♦ ♠ ♣)
- Statistics tracking
- Multiple players

Note: Currently the player wins with a Five Card Trick before the CPU gets the opportunity to also achieve one, this is another area of improvement.

## Author

Created as a Python learning project to practise:

- Functions
- Loops
- User input validation
- Lists and list comprehensions
- Conditional logic
- Game state management
- Terminal output formatting using Colorama
