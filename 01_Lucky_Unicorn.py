# Iszac Jarvis 3/02/2020
# v1 Lucky Unicorn

# donkey = 0
# zebra & horse = 0.5
# unicorn = 5

# if user spends $10 - game will not allow you to continue
# game allows user to stop & continue at any time provided they have not lost all their $
# display end of round results e.g. how much $ was lost/won & how much money they have left
# end game when user has no $ left

# Generate a random token

# import random

# tokens = ["horse", "zebra", "donkey", "unicorn"]

# for item in range(1,15):

#     chosen = random.choice(tokens)
#     print(chosen)

# Integer checking function


def intcheck(question, low, high):
    valid = False
    while not valid:
        error = "Please enter an integer between {} " \
                "and {}".format(low, high)
        try:
            response = int(input("Enter an integer between {} "
                                 "and {}: ".format(low, high)))

            if low <= response <= high:
                return response
            else:
                print(error)
                print()

        except ValueError:
            print(error)

# main routine goes here

how_much = intcheck("How much mondey do you want to play with? ", 1, 10)

