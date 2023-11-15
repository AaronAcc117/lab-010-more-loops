user_number = int(input("Gimme a number greater than 100 plz: "))

# while loop 
while user_number <= 100:
    # If the user enters a number less than or equal to 100, ask again
    user_number = int(input("This number is less than 100, dummy. Try again… I’ve got all day: "))


print(str(user_number) + " is greater than 100! Good work.")