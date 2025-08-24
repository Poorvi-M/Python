import random

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
images= [rock, paper, scissors]
choice= int(input("Type 0 for rock, 1 for paper and 2 for scissors\n"))
if choice >=0 and choice < 3:
    print(images[choice])
comp_choice= random.randint(0, 2)
print(f"Computer chose")
print(images[comp_choice])
if choice >=3:
    print("Invalid choice")
    
elif comp_choice > choice:
    print
    print("You lose")
elif comp_choice < choice:
    print("You win")
elif comp_choice == choice:
    print("Tie")
