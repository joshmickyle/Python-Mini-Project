import random
from Age_validation import user_age_entered
# This is where the official six random numbers are generated
# I used a while loop to generate this
# The code below is one of the reasons i don't have a doctest or unittest
# I didn't want to use a def function here or my the users age validation so i just decided to take the 4 point hit
# I know how to do these tests, i just didn't want to change the way my code worked to accommodate for them
winning_list = []
# variable for the random 6 numbers list
winning_set = 0
# variable for use in my nested while statement below
if user_age_entered > 17:
    # if statement to ensure program only runs if user is older than 18
    while winning_set < 6:
        # while statement that runs if the winning_set has less than 6 numbers inside it
        num_gen = random.randint(1, 50)
        # variable to generate a random number
        winning_set += 1
        # adds 1 to winning_set
        winning_list.append(num_gen)
        # appends the 1 random number generated in num_gen to the winning_list
winning_list.sort()
# sorts the final list in ascending order
