# Imports 
import random
import art
import data

# Function to see hwo has more followers
def more_followers(a, b):
    if a["followers"] > b["followers"]:
        return a
    else:
        return b

# Function to choose two people 
def choose_people(a, b, list_of_people):

    # First person
    print("Compare A: " + a["name"] + ", a" + a["description"] + ", " + "from " + a["country"])

    # Print vs.
    print(art.vs + "\n")

    # Print second person
    print("Against B: " + b["name"] + ", a" + b["description"] + ", " + "from " + b["country"])

    # See who has more followers
    ans = more_followers(a, b)

    # Prompt user
    user_input = input("Who has more followers? Type 'A' or 'B': ")

    # Check user's answer
    if user_input != ans:
        print("Sorry, that's wrong. ")
        return False
    else:
        print("You're right!" )
        return True




# Start game function
def play():

    # Print logo
    print(art.logo)

    # Generate random numbers for data comparison
    personA = random.choice(data.game_data)
    personB = random.choice(data.game_data)

    # Check if numbers are the same and change them
    while personB == personA:
        personB = random.choice(data.game_data)





# Play game
play()


