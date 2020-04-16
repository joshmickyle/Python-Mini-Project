from datetime import datetime
from Age_validation import user_age_entered
# The above lines import two functions
# This .py is for the users info like name, surname and time entered the competition
# The users selected numbers are held here as well
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
                print("You entered a letter or character, please enter a number")
            else:
                break
# The break is so that if a valueError occurs the code goes back to the top till a valid number is inputed
