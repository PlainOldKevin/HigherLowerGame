# Imports 
import random
import art
import data
import os

# Function to see who has more followers
def more_followers(a, b):
    if a["follower_count"] > b["follower_count"]:
        return 'a'
    else:
        return 'b'

# Function to choose two people 
def choose_people(a, b, score):

    # First person
    print("Compare A: " + a["name"] + ", a " + a["description"] + ", " + "from " + a["country"])

    # Print vs.
    print(art.vs + "\n")

    # Print second person
    print("Against B: " + b["name"] + ", a " + b["description"] + ", " + "from " + b["country"])

    # See who has more followers
    ans = more_followers(a, b)

    # Prompt user
    user_input = input("Who has more followers? Type 'A' or 'B': ").lower()

    # Check user's answer
    if user_input != ans:
        # Clear console:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"Sorry, that's wrong. Final score: {score}")
        return False
    else:
        return True


# Start game function
def play():

    # Print logo
    print(art.logo)

    # Generate random list choice
    personA = random.choice(data.game_data)
    personB = random.choice(data.game_data)

    # Check if people are the same and change them
    while personB == personA:
        personB = random.choice(data.game_data)

    # Int to track score
    curr_score = 0

    # Run function once to start game
    return_val = choose_people(personA, personB, curr_score)

    # Run choose function repeatedly for gameplay
    while return_val != False:

        # Clear console:
        os.system('cls' if os.name == 'nt' else 'clear')

        # Print logo
        print(art.logo)

        # Keep second person in the game
        personA = personB

        # Generate random list choice for second option
        personB = random.choice(data.game_data)

        # Check if people are the same and change them
        while personB == personA:
            personB = random.choice(data.game_data)

        # Increase score (if loop makes it this far answer is correct)
        curr_score += 1
        print(f"You're right! Current score: {curr_score}") 

        # Run function
        return_val = choose_people(personA, personB, curr_score)

# Play game
play()


