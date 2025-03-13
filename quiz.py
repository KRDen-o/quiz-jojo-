#this quiz will be about jojo stand names

#i will make funtions for new game, answer, and/or other funtions
def new_game():
#this will display not only the questions but also some answers and the user input
    guesses = []
    correct_guesses = 0
    question_num= 1

    for key in questions:
        print("----------------------------------------")
        print (key)
        for i in options[question_num-1]:
            print(i)
        quess = input("Enter (A, B, C, or D: ")
        quess = quess.upper()
        question_num += 1

def check_answer():
    pass
def display_score():
    pass
def play_again():
    pass

questions = {
    "what is johnathan joestar main power?": "B",
    "what is joseph joestar main ability he uses?": "D",
    "what is jotaro kujo's stand name?": "A"
}

options = [["A. Stand", "B. Hamon", "C. Vampiric powers", "D. Other"],
           ["A. Stand", "B. Hamon", "C. weapons", "D. A and B"],
           ["A. Star platinum", "B. The world", "C. The wonder of U", "D. Other"],]

new_game()
