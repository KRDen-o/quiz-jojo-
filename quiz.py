#this quiz will be about jojo stand names

#i will make funtions for new game, answer, and/or other funtions
def new_game():

    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("-------------------------")
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input("Enter (A, B, C, or D): ")
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key), guess)
        question_num += 1

    display_score(correct_guesses, guesses)


def check_answer(answer, guess):

    if answer == guess:
        print("CORRECT!")
        return 1
    else:
        print("WRONG!")
        return 0


def display_score(correct_guesses, guesses):
    print("-------------------------")
    print("RESULTS")
    print("-------------------------")

    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("Guesses: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()

    score = int((correct_guesses/len(questions))*100)
    print("Your score is: "+str(score)+"%")


def play_again():

    response = input("Do you want to play again? (yes or no): ")
    response = response.upper()

    if response == "YES":
        return True
    else:
        return False
#this is where the questions will live
questions = {
    "what is johnathan joestar main power?": "B",
    "what is joseph joestar main ability he uses?": "D",
    "what is jotaro kujo's stand name?": "A"
}

options = [["A. Stand", "B. Hamon", "C. Vampiric powers", "D. Other"],
           ["A. Stand", "B. Hamon", "C. weapons", "D. A and B"],
           ["A. Star platinum", "B. The world", "C. The wonder of U", "D. Other"],]

new_game()

while play_again():
    new_game()

print("Byeeeeee!")

