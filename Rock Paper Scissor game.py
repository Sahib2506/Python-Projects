rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


import random

choice = [rock, paper, scissors]

user_choice = int(input("Kindly Enter 0 for rock, 1 for Paper, 2 for scissors\n"))

if user_choice >=3 or user_choice < 0 :
   print("You made an incorrect entry, You lost")

else:
   print(choice[user_choice])

   comp_choice = random.randint(0,2)
   print("Computer Choice:")
   print(choice[comp_choice])

   if comp_choice == user_choice:
     print("Oh no! it's a draw, nobody wins") 

   elif user_choice  == 0 and comp_choice == 2:
     print("Congrats You Won")

   elif user_choice  == 2 and comp_choice == 0:
     print("Sorry, You Lost, Computer won this time")

   elif comp_choice > user_choice:
     print("Sorry, You Lost, Computer won this time")

   elif comp_choice < user_choice:
     print("Congratulations, You won this time")

   else :
     print("You lost")