import random

def new_game():
    # Ask the user how many questions they want to answer
    num_questions = int(input("How many questions would you like to answer? "))

    # Ensure the number of questions does not exceed the available questions
    if num_questions > len(questions):
        print(f"Sorry, we only have {len(questions)} questions available. Selecting all questions.")
        num_questions = len(questions)

    # Randomly select the specified number of questions from the list of questions
    selected_questions = random.sample(questions, num_questions)

    guesses = []
    correct_guesses = 0

    for question_data in selected_questions:
        question = question_data["question"]
        correct_answer = question_data["correct_answer"]
        options = question_data["options"]

        print("-------------------------")
        print(question)

        # Display the options for the current question
        for option in options:
            print(option)

        # Input validation to ensure only 'A', 'B', 'C', or 'D' is accepted
        guess = ""
        while guess not in ['A', 'B', 'C', 'D']:
            guess = input("Enter (A, B, C, or D): ").upper()
            if guess not in ['A', 'B', 'C', 'D']:
                print("Invalid input. Please enter A, B, C, or D.")

        guesses.append(guess)

        # Check the answer by comparing the correct answer with the guess
        correct_guesses += check_answer(correct_answer, guess)

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

    print("Guesses: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()

    score = int((correct_guesses / len(guesses)) * 100)  # Use guesses to calculate score
    print(f"Your score is: {score}%")


def play_again():
    response = input("Do you want to play again? (yes or no): ")
    response = response.upper()

    if response == "YES":
        return True
    else:
        print("Goodbye!")
        return False


# List of questions with their respective correct answers and options
questions = [
    {
        "question": "What is Jonathan Joestar's main power?",
        "correct_answer": "B",
        "options": ["A. Stand", "B. Hamon", "C. Vampiric powers", "D. Other"]
    },
    {
        "question": "What is Joseph Joestar's main ability?",
        "correct_answer": "D",
        "options": ["A. Stand", "B. Hamon", "C. Weapons", "D. A and B"]
    },
    {
        "question": "What is Jotaro Kujo's stand name?",
        "correct_answer": "A",
        "options": ["A. Star Platinum", "B. The World", "C. The Wonder of U", "D. Other"]
    },
    {
        "question": "How about Josuke from Part 4, his stand name?",
        "correct_answer": "C",
        "options": ["A. Crazed Diamond", "B. Soft and Wet", "C. Crazy Diamond", "D. Nut and Bolt"]
    },
    {
        "question": "Who is the best friend of johnny joestar",
        "correct_answer": "A",
        "options": ["A. Gyro Zeppeli", "B. Will Zeppeli", "C. Caesar Zeppeli", "D. Speedwagon"]
    },
    {
        "question": "Dio Brando's main power in Part 1?",
        "correct_answer": "A",
        "options": ["A. Vampire powers", "B. Hamon", "C. ZA WADO", "D. Pillar Men"]
    },
    {
        "question": "What group does Kars belong to?",
        "correct_answer": "B",
        "options": ["A. Dio's ghouls", "B. The Pillar Men", "C. Vampires", "D. Locacaca Organization"]
    },
    {
        "question": "Did Dio return and with what stand?",
        "correct_answer": "C",
        "options": ["A. Yes: ZA HANDO", "B. No: he's mega dead", "C. Yes, and he has The World", "D. No: he's over heaven"]
    },
    {
        "question": "Who was the real villain of Part 4?",
        "correct_answer": "D",
        "options": ["A. Toru", "B. Josefumi Kujo", "C. The Head Doctor", "D. Yoshikage Kira"]
    },
    {
        "question": "What was the name of King Crimson's user?",
        "correct_answer": "C",
        "options": ["A. The Head Doctor", "B. Jobin Hiragishita", "C. Diavolo", "D. Dopio"]
    },
    {
        "question": "What is Enrico Pucci's ultimate goal with the Heaven plan?",
        "correct_answer": "B",
        "options": ["A. To save Dio cause he is a simp", "B. He wanted to create Heaven", "C. Araki wanted to soft reset JoJo", "D. To rid the world of Joestars"]
    },
    {
        "question": "what is president valentines stand name after obtaining the corpse",
        "correct_answer": "D",
        "options": ["A. dirty deeds done dirt cheap", "B. D4C", "C. Golden Experience", "D. D4C Love train"]
    },
    {
        "question": "How does Tooru's Stand, Wonder of U symbolize his control over fate in JoJolion?",
        "correct_answer": "B",
        "options": ["A. The energy of calamity", "B. The flow of calamity", "C. the flow of death", "D. Obla di, obla da"]
    },
    {
        "question": "what is Gappy's or josuke stand in part 8?",
        "correct_answer": "A",
        "options": ["A. soft and wet + go beyond", "B. Killer queen", "C. soft and wet", "D. Ball breaker"]
    },
    {
        "question": "golden experience user is who?",
        "correct_answer": "B",
        "options": ["A. jodio joestar", "B. giornio giovana", "C. JOtaro kujo", "D. josefumi kujo"]
    },
    {
        "question": "who is Jolines father in stone ocean?",
        "correct_answer": "C",
        "options": ["A. josefumi kujo", "B.Father Pucci", "C. jotaro kujo", "D. no one"]
    },
    {
        "question": "Jodio joestars stand name is what?",
        "correct_answer": "D",
        "options": ["A. Smooth operators", "B. Bigmouth strikes again", "C. The Hustle", "D. November Rain"]
    },
    {
        "question": "Hw many act are there for Johnny joestars stand Tusk?",
        "Correct_answer": "A",
        "options": ["A. Tusk act 4", "B. 3 acts", "C. 2 acts", "D.stands can't evolve"]
    }
]

# Start the game
new_game()

while play_again():
    new_game()

print("Byeeeeee!")
