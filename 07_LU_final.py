# Lucky Unicorn Fully Working Program
# Program should work - neds to be tested for usability

import random

# Integer checking function:


def intcheck(question, low, high):
    valid = False
    error = "Please enter an integer between {} and {}".format(low, high)
    while not valid:
        try:
            response = int(input(question))
            if low <= response <= high:
                return response

            else:
                print(error)
                print()
        except ValueError:
            print(error)
            print()

# Function adds line above and below statement with 'decoration' character
# so that users can easily see what they have won
def statement_generator (statement, decoration):
    print(decoration * len(statement))
    print(statement)
    print(decoration * len(statement))
    

# Main routine goes here...

# welcoming
statement_generator("Welcome to the ***Lucky Unicorn*** Game!", "=")

# instructions

print()
print("=" * 10)

print("This game is all about gambling. ")
print("Each round will reward or detriment your total balance - ")
print("depending on which 'token' you receive.")
print("=" * 10)
print()

print("=" * 10)

print("Good luck! Win big!")

print("=" * 10)

print()


# Ask user how much money they want to play with (min $1, max $10)

print("-" * 10)

balance = intcheck("How much money would you like to play with? $", 1, 10)

print("-" * 10)

# keep going loop

keep_going = ""
while keep_going == "":

    # tokens list includes 16 items to prevent too many unicorns being chosen

    tokens = ["Horse", "Horse", "Horse",
              "Zebra", "Zebra", "Zebra",
              "Donkey", "Donkey", "Donkey",
              "Donkey", "Zebra", "Horse",
              "Donkey", "Zebra", "Horse",
              "Unicorn"]

    # randomly choose a token from our list above

    token = random.choice(tokens)

    print()

    print("=" * 10)


    # Adjust total correctly for a given token

    if token == "Unicorn":
        balance += 5    # wins $5
        feedback = "Congratulations.  You got a Unicorn! You won $5.00!"
        decoration = "*"
    elif token == "Donkey":
        balance -= 1    # doesn't win anything (ie: loses $1)
        feedback = "Sorry, you got a donkey and lost $1.00."
        decoration = "!"
    else:
        balance -= 0.5  # 'wins' 50c, paid $1 so loses 50c overall
        feedback = "Sorry,  you got a {} and lost 50¢.".format(token)
        decoration = "#"

    round_feedback = feedback + "You have ${:.2f} left to play with.".format(balance)
    
    statement_generator(round_feedback, decoration)
    print()
    
    # If user has enough money to play, ask if they want to play again...

    if balance < 1:
        statement_generator("Sorry, you do not have enough money to continue. Game over!", "@")
        keep_going = "end"
    else:
        keep_going = input("Press <enter> to play again or any key to quit. ")

# farewell user at the end of game.
print("=" * 10)

print("Thank you for playing. You went home with ${:.2f}".format(balance))

print("=" * 10)
