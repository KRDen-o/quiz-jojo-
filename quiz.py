#this quiz will be about jojo stand names

#check interger for how many questions are allowed

# Check that users have entered a valid option based on a list
def string_checker(question, valid_ans=("yes", "no")):
    while True:
        # Get user response and make sure it is lowercase
        user_response = input(question).lower()

        for item in valid_ans:
            # check if the user response is a word in the list
            if item == user_response:
                return item

            # check if the user response uis the same as
            # the first letter of the item
            elif user_response == item[0]:
                return item

        print("Please enter a valid option")

def instructions():
    print('''
    *** Instructions ***
    there is a quiz to see how good you are knowing jojo characters stands or abilities
    
    The rules are:
    you have to input the correct stand or other ability they have to score a point 
    
    Press xxx to exit the game
    
    Good luck! 
    ''')
    # check for an interger thats more than 0
def int_check(question):
    while True:
        error = "please enter an number more than zero"
        to_check = input(question)

        try:
            responce = int(to_check)

            #cheks that the once

            if responce < 1:
                print("error")
            else:
                return  responce
        except ValueError:
            print("error")

