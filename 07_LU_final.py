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

# welcoming
print("=" * 10)

print("Welcome to the ***Lucky Unicorn*** Game!")

print("=" * 10)

# instructions

print()
print("=" * 10)

print("This game is all about gambling. ")
print("Each round will reward or detriment your total balance - ")
print("depending on which 'token' you receive.")

print()

print("=" * 10)

print("Good luck! Win big!")

print("=" * 10)

print()

# Main routine

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

    if token == "Unicorn":
        print("You got a **{}**!".format(token))
    else:
        print("You got a {}!".format(token))

    print()

    # Adjust total correctly for a given token

    if token == "Unicorn":
        balance += 5    # wins $5
        feedback = "Congratulations! You won $5.00!"
    elif token == "Donkey":
        balance -= 1    # doesn't win anything (ie: loses $1)
        feedback = "Sorry, you did not win anything this round."
    else:
        balance -= 0.5  # 'wins' 50c, paid $1 so loses 50c overall
        feedback = "Sadly, you lost 50¢."

    print(feedback)
    print("=" * 10)
    print()
    print("=" * 10)
    print("You have ${} left to play with.".format(balance))
    print("=" * 10)
    print()

    # If user has enough money to play, ask if they want to play again...

    if balance < 1:
        print("Sorry, you do not have enough money to continue. Game over!")
        keep_going = "end"
    else:
        keep_going = input("Press <enter> to play again or any key to quit. ")

# farewell user at the end of game.
print("=" * 10)

print("Thank you for playing. You went home with ${}".format(balance))

print("=" * 10)
