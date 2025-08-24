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
ans= input("Do you want to play? Type Y for yes and N for no").upper()
if ans!=  
print("Let's play rock paper scissors")
while True:
    user = input("Choose 'R' for rock, 'P' for papaer or 'S' for scissors\n").upper()
    if user not in ['R', 'P', 'S']:
        print("Invalid choice. Please choose 'R' 'P' or 'S' ")
        continue
    if user == 'R':
        print("You chose rock")
        print(rock)
    elif user == 'P':
        print("You chose paper")
        print(paper)
    else:
        print("You chose scissors")
        print(scissors)

    computer = random.choice(['R', 'P', 'S'])
    if computer == user:
        print("It's a tie")
    elif (computer== 'P' and user=='R') or (computer=='S' and user=='P') or (computer=='R' and user=='S'):
        print("You lose")
    else:
        print("You win")
    
    play_again = input("Do you want to play again? Type 'Y' for yes and 'N' for no").upper()
    if play_again != 'Y':
        print("Thanks for playing")
        break