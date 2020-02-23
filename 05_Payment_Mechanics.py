# Lucky Unicorn - payment mechanics

# To do
# Adjust total correctly for a given token
#   - if it's a unicorn, add $5
#   - if it's a zebra / horse, subtract 0.5
#   - if it's a donkey, subtract 1
# Give user feedback based on winnings...
# State new total

# Assume starting amount is $10

total = 10

# Allow manual token input for testing purposes

token = input("Enter a token: ")

# Adjust total correctly for a given token

if token == "unicorn":
    total += 5
    feedback = "Congratulations! You won $5.00!"
elif token == "donkey":
    total -= 1
    feedback = "Sorry, you did not win anything this round"
else:
    total += 0.5
    feedback = "Congratulations! You won 50c!"

print()

print(feedback)
if total >= 1:
    print("You have ${} to play with.".format(total))
elif total == 0.5:
    print("You have {}c to play with.".format(total))
