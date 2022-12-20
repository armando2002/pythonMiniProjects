import random

# get number input
top_of_range = input("Type a number to generate a random number. You'll then guess the random number: ")

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
        # commas let you use a variable easily
        print("You got it!")
        break
    elif user_guess > random_number:
        print("You were above the number")
    else:
        print("You were below the number")

print("You got it in", guesses, "guesses")
