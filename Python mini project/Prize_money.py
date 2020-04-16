from Age_validation import user_age_entered
from Official_numbers import winning_list
from User_info import user_list
# This is where the users chosen numbers and the official six numbers are compared
# there is a nested if statement in a for loop and what happens is that if there is a number that is in both
# sets, then that number gets added to the variable matched_numbers
# i used len on match numbers to determine how many numbers matched
# there is a massive if statement that uses the len(matched_numbers) to determine what the user wins
# that gets written to the text file named User_info.txt
matched_numbers = []
# variable for comparing the users 6 numbers and the random 6 numbers


def compare_numbers():
    # function to compare the two lists
    if user_age_entered > 17:
        # if statement that ensures the function only runs if the user is older than 18
        for num in user_list:
            # checks the numbers in users list
            if num in winning_list:
                # if the same number is in the winning list, it will append the number to matched_numbers
                matched_numbers.append(num)
                # appends the number to matched_numbers
            else:
                # what happens if the number is only in one list
                continue
                # if so it continues to the beginning of the for statement till the list is finished


def prize_money():
    # function to determine how much money the user wins
    my_user_file = open("User_info.txt", "r+")
    # opens the text file where user info is saved
    my_user_file.readline()
    # used to ignore the first line in the text file
    user_namefromtext = my_user_file.readline().replace('\n', '')
    # reads the players name from the text file
    if user_age_entered > 17:
        # if statement to ensure only old enough players see this information
        if len(matched_numbers) > 5:
            # if statement for if the user matches 6 numbers correct
            print("Congratulations!!! You got six numbers correct and won R10 000 000.00")
            # displays the output
            my_user_file.write("\nThe Ithuba National Lottery of South Africa is required to pay " + user_namefromtext +
                               " R10 000 000.00")
            # writes how munch money needs to be paid into the text file
        elif 4 < int(len(matched_numbers)) < 6:
            # if statement for if the user matches 5 numbers correct
            print("Congratulations!!! You got five numbers correct and won R8 584.00")
            # displays the output
            my_user_file.write("\nThe Ithuba National Lottery of South Africa is required to pay " + user_namefromtext +
                               " R8 584.00")
            # writes how munch money needs to be paid into the text file
        elif 3 < int(len(matched_numbers)) < 5:
            # if statement for if the user matches 4 numbers correct
            print("Congratulations!!! You got four numbers correct and won R2 384.00")
            # displays the output
            my_user_file.write("\nThe Ithuba National Lottery of South Africa is required to pay " + user_namefromtext +
                               " R2 384.00")
            # writes how munch money needs to be paid into the text file
        elif 2 < int(len(matched_numbers)) < 4:
            # if statement for if the user matches 3 numbers correct
            print("Congratulations!!! You got three numbers correct and won R100.50")
            # displays the output
            my_user_file.write("\nThe Ithuba National Lottery of South Africa is required to pay " + user_namefromtext +
                               " R100.50")
            # writes how munch money needs to be paid into the text file
        elif 1 < int(len(matched_numbers)) < 3:
            # if statement for if the user matches 2 numbers correct
            print("Congratulations!!! You got two numbers correct and won R20.00")
            # displays the output
            my_user_file.write("\nThe Ithuba National Lottery of South Africa is required to pay " + user_namefromtext +
                               " R20.00")
            # writes how munch money needs to be paid into the text file
        elif 0 < int(len(matched_numbers)) < 2:
            # if statement for if the user matches 1 numbers correct
            print("Unfortunately, you only got one number correct and win nothing")
            # displays the output
            my_user_file.write("\nThe Ithuba National Lottery of South Africa is required to pay " + user_namefromtext +
                               " R0.00")
            # writes how munch money needs to be paid into the text file
        elif int(len(matched_numbers)) < 1:
            # if statement for if the user matches 0 numbers correct
            print("Unfortunately, you got zero numbers correct and win nothing \n")
            # displays the output
            my_user_file.write("\nThe Ithuba National Lottery of South Africa is required to pay " + user_namefromtext +
                               " R0.00")
            # writes how munch money needs to be paid into the text file
    my_user_file.close()
