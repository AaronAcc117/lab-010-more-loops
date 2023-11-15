maximum_stories = 10  

# Ask the user which floor they work on
user_floor = int(input("On what floor of the building is your office? "))

# my while loop
while user_floor <= 0 or user_floor > maximum_stories:
    # If the user enters an invalid number, print an error message
    print("Error: {} is not a valid floor number. The building has {} floors. Please enter a valid number.".format(user_floor, maximum_stories))

    # Ask the user again
    user_floor = int(input("Please enter a valid floor number: "))


print("Congratulations! You work on floor {}.".format(user_floor))