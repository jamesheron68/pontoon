import random

from colorama import init, Fore

# Initialise colorama
init()

# Function to calculate score for a given hand
def score_hand(hand):

    score = 0
    aces = 0

    for card in hand:
        rank = card.split()[0]

        # Handle face cards
        if rank in ["Jack", "Queen", "King"]:
            score += 10
        elif rank == "Ace":
            aces += 1
            score += 11
        else:
             score += int(rank)

    # Handle ace is high or low option
    while score > 21 and aces > 0:
        score -= 10
        aces -= 1

    return score

# Function to display the user a given hand
def print_hand(hand, owner):
    print(owner)
    print("Current hand:\n")
    for card in hand:
        print(Fore.WHITE + card)
    print(f"\nScore: {score_hand(hand)}")
    print()

# Function to check if they player has 'pontoon' - an ace and a 10-value card
def pontoon_check(hand):

    aces = 0
    tens = 0

    for card in hand:
        rank = card.split()[0]

        if rank == "Ace":
            aces += 1
        elif rank in ["10", "Jack", "Queen", "King"]:
            tens += 1

    return aces == 1 and tens == 1

# Create a standard 52 card deck of playing cards
suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

deck = [f"{rank} of {suit}" for suit in suits for rank in ranks]

# Shuffle the deck
random.shuffle(deck)

# Deal initial hands - players alternate for cards dealt
dealer_hand = []
hand = []

for _ in range(2):
    hand.append(deck.pop())
    dealer_hand.append(deck.pop())

# Check for Pontoon - Win condition
player_pontoon = pontoon_check(hand)
dealer_pontoon = pontoon_check(dealer_hand)

if player_pontoon or dealer_pontoon:
    if player_pontoon and dealer_pontoon:
        print(Fore.RED + "Both players have Pontoon! Dealer wins!")

    elif player_pontoon:
        print(Fore.GREEN + "You have Pontoon! You win!")

    elif dealer_pontoon:
        print(Fore.RED + "Dealer has Pontoon! Dealer wins!")

    print_hand(hand, Fore.BLUE + "Player 1")
    print_hand(dealer_hand, Fore.YELLOW + "Dealer")

    exit()

# Flag for 5 card trick
five_card_trick = False
dealer_five_card_trick = False

# Main gameplay loop, the player sees their hand and chooses to 'hit' or 'stand'
while score_hand(hand) < 21:

    print_hand(hand, Fore.BLUE + "Player 1")

    if score_hand(hand) < 15:
        print(Fore.CYAN + "Your score is below 15, so you must hit.")

    # Error handling for invalid inputs
    while True:
        action = input(Fore.CYAN + "What would you like to do? (S = Stand, H = Hit)\n").upper()

        # Players can not stand on a score less than 15
        if action == "S" and score_hand(hand) < 15:
            print(Fore.RED + "You can not stand on a score less than 15.")
            continue

        if action in ["S", "H"]:
            break

        print(Fore.RED + "Invalid response.")

    # If they choose to 'hit' then another card is dealt
    if action == "H":
        hand.append(deck.pop())
    else:
        break

    # 5 card trick
    if len(hand) == 5:
        five_card_trick = True
        break

# If the player goes over 21 then they go bust and the game ends
if score_hand(hand) > 21:
    print_hand(hand, Fore.BLUE + "Player 1")
    print(Fore.RED + "Unlucky! You went bust!")
    exit()

# If the player gets a 5 card trick, they win
if five_card_trick:
    print_hand(hand, Fore.BLUE + "Player 1")
    print(Fore.GREEN + "5 Card Trick! You win!")
    exit()

# The dealer then takes their turn and tries to beat or match the score of the player
while (
    score_hand(dealer_hand) < score_hand(hand)
    and len(dealer_hand) < 5
):
    dealer_hand.append(deck.pop())

# If the dealer goes bust then the player wins
if score_hand(dealer_hand) > 21:
    print_hand(dealer_hand, Fore.YELLOW + "Dealer")
    print(Fore.GREEN + "The dealer went bust! You win!")
    exit()

# If the dealer gets a 5 card trick, they win
if len(dealer_hand) == 5:
        dealer_five_card_trick = True

if dealer_five_card_trick:
    print_hand(dealer_hand, Fore.YELLOW + "Dealer")
    print(Fore.RED + "Dealer 5 Card Trick! The dealer wins!")
    exit()

# If both the player and dealer are still in the game, the winner is calculated
if score_hand(hand) > score_hand(dealer_hand):
    print(Fore.GREEN + "Congratulations! You win!")
elif score_hand(hand) < score_hand(dealer_hand):
    print(Fore.RED + "Better luck next time! The dealer wins!")
else:
    print(Fore.RED + "It's a draw! The dealer wins!")

# Show the final hands to the player
print_hand(hand, Fore.BLUE + "Player 1")
print("--- --- --- ---")
print_hand(dealer_hand, Fore.YELLOW + "Dealer")