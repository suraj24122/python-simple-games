import random
import art
EASY_LEVEL_ATTEMPTS = 10
HARD_LEVEL_ATTEMPTS = 5

def set_difficulty(level_chosen):
    if level_chosen == "easy":
        return EASY_LEVEL_ATTEMPTS
    elif level_chosen == "hard":
        return HARD_LEVEL_ATTEMPTS
    else:
        print("Please enter a valid level - easy or hard")
        return set_difficulty(input("Enter level - easy or hard - "))
    
def check_answer(guessed_number, answer, attempts):
    if guessed_number < answer:
        print("Your guess is too low !!!")
        return attempts-1
    elif guessed_number > answer:
        print("Your guess is too high !!!")
        return attempts-1
    else:
        print(f"You guessed right... the answer was {answer}")

def game():
    print(art.logo)
    print("Let me think of number btwn 1 to 50 : ")
    answer = random.randint(1,50)
    # print(answer)

    level = input("Enter level - easy or hard - ")
    attempts = set_difficulty(level)

    if attempts != EASY_LEVEL_ATTEMPTS and attempts != HARD_LEVEL_ATTEMPTS:
        print("Please enter a valid level - easy or hard")
        return

    guessed_number = 0
    while guessed_number!=answer:
        print(f"you have {attempts} remaining to guess the number")
        guessed_number = int(input("Guess the number = "))
        attempts = check_answer(guessed_number,answer,attempts)
        if attempts == 0:
           print("You are out of guesses....you lose !!!")
           return
        elif guessed_number != answer:
            print("Guess Again")
game()


















