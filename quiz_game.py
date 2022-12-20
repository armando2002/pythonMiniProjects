print("Welcome to the State Capitols Quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    print("Fine then, loser!")
    quit()

print("Okay! Let's play!")

answer = input("What is the capital of Washington? ")
if answer.lower() == "olympia":
    print("Correct!")
else:
    print("Sorry, wrong answer.")

answer = input("What is the capital of Pennsylvania? ")
if answer.lower() == "harrisburg":
    print("Correct!")
else:
    print("Sorry, wrong answer.")

answer = input("What is the capital of Florida? ")
if answer.lower() == "tallahassee":
    print("Correct!")
else:
    print("Sorry, wrong answer.")

answer = input("What is the capital of California? ")
if answer.lower() == "sacramento":
    print("Correct!")
else:
    print("Sorry, wrong answer.")

answer = input("What is the capital of Hawaii? ")
if answer.lower() == "honolulu":
    print("Correct!")
else:
    print("Sorry, wrong answer.")