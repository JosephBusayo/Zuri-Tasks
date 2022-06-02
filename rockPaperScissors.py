import random

userChoice = input("""
R for rock | P for paper | S for scissors
Enter your selection: """ )

possibleChoice = ['R', 'P', 'S']

while True:
    if userChoice not in possibleChoice:
        print("Wrong input!!!")
        userChoice = input("Enter your selection: " )
    break

botChoice = random.choice( possibleChoice) #selects at random from the list

rule = { #1 = win, 0.5=tie, 0=loss
    'R': {'S': 1, 'R': 0.5, 'P': 0},
    'P' : {'R': 1, 'P': 0.5, 'S': 0},
    'S' : {'P': 1, 'S': 0.5, 'R': 0},
}

if rule[userChoice][botChoice] == 1:
    print (f'You pick {userChoice} computer picks {botChoice}. YOU WIN!!!')
elif rule[userChoice][botChoice] == 0.5:
    print (f'You pick {userChoice} computer picks {botChoice}. That a tie!')
else:
    print (f'You pick {userChoice} computer picks {botChoice}. Sorry you loss')