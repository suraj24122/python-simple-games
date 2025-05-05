import random

rock = '''
     _______
----'   ____)
      (_____)
      (_____)
      (____)
----.__(___)
'''

paper = '''
    _______
----'   ____)____
          ______)
          _______)
         _______)
----.__________)
'''

scissors = '''
    _______
----'   ____)____
          ______)
       __________)
      (____)
----.__(___)
'''

game_images = [rock, paper, scissors]
user_choice = int(input("Enter your choice \n 0 For Rock = \n 1 For Paper = \n 2 For Scissor = PLAYER"))
if user_choice >= 3 or user_choice < 0:
    print("you entered invalid number. you loose")

else:
    print(game_images[user_choice])
    computer_Choice = random.randint(0,2) 
    print("COMPUTER - ",game_images[computer_Choice])

    if computer_Choice == user_choice:
        print("Its a Draw")
    elif computer_Choice == 0 and user_choice == 2:
        print("You Loose !!!")
    elif user_choice == 0 and computer_Choice == 2:
        print("You Win !!!")
    elif computer_Choice > user_choice:
        print("You Loose !!!")
    elif user_choice > computer_Choice:
        print("You Win !!!")





































