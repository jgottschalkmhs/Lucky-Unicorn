# Lucky Unicorn - end mechanics

# To do
# Ask user how much money they have to play with
# If the total is less than $1, quit
# If the total is more than $1, ask user if they want to keep going


# Assume starting ammount is $10

total = int(input("How much money would you like to play with? $"))

keep_going = ""
while keep_going == "":

    # Allow manual token input for testing purposes:

    token = input("Enter a token: ")

    # Adjust total correctly for a given token

    if token == "unicorn":
        total += 5
        feedback = "Congratulations! You won $5.00"

    elif token == "donkey":
        total -= 1
        feedback = "Sorry, you did not win anything this round"

    else:
        total += 0.5
        feedback = "Congratulations! You won 50c"

    print()

    print(feedback)
    if total >= 1:
        print("You have ${} to play with.".format(total))
    elif total == 0.5:
        print("You have {}c to play with.".format(total))

    if total < 1:
        print("You don't have enough money to continue. Game over")
        keep_going = "end"
    else:
        keep_going = input("Press <enter> to play again or any key to quit ")

print("Thank you for playing!")
