# Josh-Mickyle Baron Class 2
from Age_validation import user_age_entered
from Official_numbers import winning_list
from Prize_money import compare_numbers, prize_money
from User_info import user_age, user_selected_number
# The 4 lines above get information from the various python files
# This Main.py is where the program is run from
# All the different functions are called and run here
if user_age_entered > 17:
    # if statement to ensure functions are only called if user is old enough
    user_age()
    # calling the function to be run
    user_selected_number()
    # calling the function to be run
    compare_numbers()
    # calling the function to be run
    print(30 * "_", "The official six lotto number are", 35 * "_", "\n", winning_list)
    # displaying the winning six numbers
    print(46 * "_", "outcome", 45 * "_")
    # displaying how many numbers match between the users list and winning list
    prize_money()
    # calling the function to be run
    print(18 * "_-" + "Please play again soon!!! " + 19 * "-_")
    # displays the output
