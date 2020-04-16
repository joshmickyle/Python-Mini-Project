# This is the age validation piece of code
# If the age is less than <= 17 none of the other codes in the other files will be allowed to run
# The console or IDE will display that the user is too young to gamble
# Below there is an exception for ValueError so if the user enters a letter they will be asked to enter a number
while 1:
    try:
        user_age_entered = int(input("Please enter your age:  "))
    except ValueError:
        print("You entered a letter or character by mistake, please enter your age as a number")
    else:
        if user_age_entered <= 17:
            print("Unfortunately according to the National Gambling Act, you may not enter the lottery  ")
        break
# The break is so that if there is a ValueError the code will go back to the top and the user will have to enter a
# letter again until they enter a valid number or an age that is too young
