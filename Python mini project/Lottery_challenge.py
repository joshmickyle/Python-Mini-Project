# Josh-Mickyle Baron Class 2
import random
from datetime import datetime

while 1:
    try:
        user_age_entered = int(input("Please enter your age:  "))
    except ValueError:
        print("ValueError occurred, please enter a number")
    else:
        if user_age_entered <= 17:
            print("Unfortunately according to the National Gambling Act, you may not enter the lottery  ")
        break

user_list = []


# variable for the users chosen list


def user_age():
    if user_age_entered > 17:
        # if statement for what happens if the age is less than or more than 18
        print(28 * "_", "You are eligible to take part in the lottery", 26 * "_")
        # printing that user is eligible
        if user_age_entered > 17:
            # Nested statement to ask for users name and surname
            user_name = input("You may enter your name:  ")
            # variable for users name
            user_surname = input("You may enter your surname:  ")
            # variable for users surname
            my_user_file = open("User_info.txt", "w+")
            # opening text file to store users name and surname
            n = datetime.now()
            # variable to get date
            my_user_file.write("Players name is:\n" + user_name + " " + user_surname + "\nPlayer is " +
                               str(user_age_entered) + " years old")
            # writing user info to text
            my_user_file.write("\nThe exact time " + user_name + " entered the competition was at " + "%s" % n)
            # writing date to the text file
            my_user_file.close()
            # closing the text file

    else:
        print("Unfortunately according to the National Gambling Act, you may not enter the lottery  ")
        # what happens when the user is not old enough


def user_selected_number():
    # function for user to input their six numbers
    if user_age_entered > 17:
        # if statement to ensure only old enough users see this info
        print(31 * "_", "Please enter your six lottery numbers", 30 * "_")
        # displaying the instruction
        # variable for the list
        while 2:
            try:
                while len(user_list) < 6:
                    # while loop to ensure the list is only six numbers
                    list_item = int(input("Enter a number between 1 and 49:  "))
                    # variable for the items in the list
                    if 0 < list_item < 50 and list_item not in user_list:
                        # if statement to ensure numbers in the list aren't repeated or out of range
                        user_list.append(list_item)
                        # adding the item to the list
                    else:
                        # what happens if the number was out of range or repeated
                        list_item = int(input("Please do not repeat numbers or enter a number out of range \nPick a "
                                              "number 1 through 49: "))
                        # variable for the item to be entered again
                        user_list.append(list_item)
                        # adding the item to the list
                print(30 * "_", "You selected the following numbers as your 6 picks:  ", 15 * "_", "\n",
                      sorted(user_list))
                # displays the six numbers selected by the user
            except ValueError:
                print("ValueError occurred, please enter a number")
            else:
                break


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
