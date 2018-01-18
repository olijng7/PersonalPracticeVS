
from random import randint
def game():
    player = input("rock (r), paper (p), or scissors (s)?")
    chosen = randint(1,3)
    if chosen == 1:
        computer = "r"
    elif chosen == 2:
        computer = "p"
    else:
        computer = "s"
    print(player, "vs.", computer)
    if computer == player:
        print('Its a tie!')
    else:
        if player == 'r' and computer == 's' or player == 's' and computer == 'p' or player == 'p' and computer == 'r':
            print("You win!")
        else:
            print('You lose!')
    again()
def again():
    again = input('Play again? (y/n)')
    if again == 'y':
        while True:
            game()
    else:
        exit()
game()