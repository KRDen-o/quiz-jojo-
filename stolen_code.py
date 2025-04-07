import random
#make sure only numbers are allowed for how many questions the user wants
def int_check(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
#the meat of this sanwitch or game that makes it ask the questions
def new_game():
    ask_questions()
#a answer checker
def check_answer(answer, guess):
    if answer == guess:
        print("CORRECT!")
        return 1
    else:
        print("WRONG!")
        return 0
#after all questions are answered they can see there score
def display_score(correct_guesses, guesses):
    print("-------------------------")
    print("RESULTS")
    print("-------------------------")

    print("Guesses: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()

    score = int((correct_guesses / len(guesses)) * 100)
    print(f"Your score is: {score}%")
#making sure to see if  user wants to play again
def play_again():
    response = input("Do you want to play again? (yes or no): ").strip().upper()
    return response in ["YES","Y"]
#make sure questions live here
def ask_questions():
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
    "question": "who is Joline's father in stone ocean?",
    "correct_answer": "C",
    "options": ["A. josefumi kujo", "B.Father Pucci", "C. jotaro kujo", "D. no one"]
},
{
    "question": "Jodio joestars stand name is what?",
    "correct_answer": "D",
    "options": ["A. Smooth operators", "B. Bigmouth strikes again", "C. The Hustle", "D. November Rain"]
},
{
    "question": "How many act are there for Johnny joestars stand Tusk?",
    "correct_answer": "A",
    "options": ["A. Tusk act 4", "B. 3 acts", "C. 2 acts", "D.stands can't evolve"]
},
  {
    "question": "What is Mr. Zeppeli's role in Phantom Blood?",
    "correct_answer": "B",
    "options": ["A. Rival to Jonathan", "B. Ripple mentor to Jonathan", "C. Ally of Dio", "D. Jonathan’s brother"]
},
{
    "question": "What drives Caesar Zeppeli to take on the Pillar Men despite the risks in Battle Tendency?",
    "correct_answer": "C",
    "options": ["A. Revenge for his father's death", "B. His loyalty to the Joestar family", "C.  A desire to prove his strength and legacy", "D. To protect the Ripple technique"]
},
 {
    "question": "What is Kakyoin's initial role in Stardust Crusaders?",
    "correct_answer": "D",
    "options": ["A. He is a member of the Joestar group from the beginning.", "B. He is a Stand user who joins the group after a fight with Jotaro.", "C. He is a rival Stand user who tries to defeat Joseph Joestar.", "D. He is a villain working for Dio."]
},
  {
    "question": "What is the main ability of Okuyasu Nijimura's Stand, The Hand?",
    "correct_answer": "A",
    "options": ["A. It erases space by slashing with its hand.", "B. It can stop time.", "C. It controls people's emotions.", "D. It manipulates shadows to attack."]
},
{
"question": "What is Bruno Bucciarati's primary goal throughout Golden Wind?",
"correct_answer": "B",
"options": ["A. To defeat Giorno and take control of Passione.","B. To protect his team and bring justice to the organization.","C. To find and destroy Diavolo.","D. To become the leader of the mafia family."]
},
{
"question": "What is Hermes Costello's primary goal in *Stone Ocean*?",
"correct_answer": "C",
"options": ["A. To escape the prison and live a peaceful life.","B. To avenge her sister's death and expose the truth.","C. To help Jolene Cujoh escape and find the Stand disk.","D. To take down Enrico Pucci and stop his plan."]
},
{
"question": "What is Yasuho Hirose's primary role in *JoJolion*?",
"correct_answer": "D",
"options": ["A. To defeat Tooru and stop his plans.","B. To uncover the truth behind the Higashikata family.","C. To help Gappy and uncover the mysteries surrounding the Rock Humans.","D. To assist Gappy (Josuke) in discovering his identity."]
}

    ]
#making sure only 25 questions are allowed to be answered and randomise it
    num_questions = int_check("How many questions would you like to answer? (max is 25) ")

    if num_questions > len(questions):
        print(f"Sorry, we only have {len(questions)} questions available. Selecting all questions.")
        num_questions = len(questions)

    print(f"You will answer {num_questions} question(s).")

    selected_questions = random.sample(questions, num_questions)

    guesses = []
    correct_guesses = 0
#make sure only a b c d are accepted answers
    for question_data in selected_questions:
        question = question_data["question"]
        correct_answer = question_data["correct_answer"]
        options = question_data["options"]

        print("-------------------------")
        print(question)

        for option in options:
            print(option)

        guess = ""
        while guess not in ['A', 'B', 'C', 'D']:
            guess = input("Enter (A, B, C, or D): ").upper()
            if guess not in ['A', 'B', 'C', 'D']:
                print("Invalid input. Please enter A, B, C, or D.")

        guesses.append(guess)
        correct_guesses += check_answer(correct_answer, guess)

    display_score(correct_guesses, guesses)


# Start the game
new_game()

while play_again():
    new_game()

print("Byeeeeee!")


