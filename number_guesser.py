import random

# get number input
top_of_range = input("Type a number: ")

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
print(random_number)



