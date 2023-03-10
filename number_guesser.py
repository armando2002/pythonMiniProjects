import random

# get number input
top_of_range = input("Enter a number. Then guess a random number from 1 to the number entered: ")

# check number
if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Please type a number larger than 0.")
        quit()

else:
    print("Please type a number next time.")
    quit()

# generate random # based on max of input
random_number = random.randrange(0, top_of_range)
guesses = 0

# make sure that input is a number, convert it
while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)

    else:
        print("please type a number next time.")
        # go to top of loop
        continue

    if user_guess == random_number:
        print("You got it!")
        break
    elif user_guess > random_number:
        print("You were above the number")
    else:
        print("You were below the number")

print("You got it in", guesses, "guesses")

# Add test cases and add the str and float checks and a reset function
