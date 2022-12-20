print("Welcome to the State Capitols Quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    print("Fine then, loser!")
    quit()

print("Okay! Let's play!")
score = 0

answer = input("What is the capital of Washington? ")
if answer.lower() == "olympia":
    print("Correct!")
    score += 1
else:
    print("Sorry, wrong answer.")

answer = input("What is the capital of Pennsylvania? ")
if answer.lower() == "harrisburg":
    print("Correct!")
    score += 1
else:
    print("Sorry, wrong answer.")

answer = input("What is the capital of Florida? ")
if answer.lower() == "tallahassee":
    print("Correct!")
    score += 1
else:
    print("Sorry, wrong answer.")

answer = input("What is the capital of California? ")
if answer.lower() == "sacramento":
    print("Correct!")
    score += 1
else:
    print("Sorry, wrong answer.")

answer = input("What is the capital of Hawaii? ")
if answer.lower() == "honolulu":
    print("Correct!")
    score += 1
else:
    print("Sorry, wrong answer.")

print(f"Your got a {str(score)} out of 5.")
