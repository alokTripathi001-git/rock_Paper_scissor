from random import choice
options = choice([('rock','1',),('paper','2'),('scissor','3')])
count_player = 0
count_system = 0
while True:
    user_input = input("Choose between rock/paper/scissor: ")
    if user_input in ('rock','1'): 
        if options== ('rock','1'):
            print("Tie")
            print("Do you wanna play again!!")
            count_system = count_system
            count_player = count_player
        elif options==('scissor','3'):
            print("Better luck next time.")
            print("Do you wanna play again!!")
            count_system+=1
            count_player = count_player
        elif options ==('paper','2'):
            print("Well played")
            print("Do you wanna play again!!")
            count_system= count_system
            count_player += 1
    elif user_input in  ('paper','2'):
        if options == ('paper','2'):
            print("Tie")
            print("Do you wanna play again!!")
            count_system = count_system
            count_player = count_player
        elif options ==('rock','1'):
            print("Better luck next time.")
            print("Do you wanna play again!!")
            count_system+=1
            count_player = count_player
        elif options ==('scissor','3'):
            print("Well played")
            print("Do you wanna play again!!")
            count_system= count_system
            count_player += 1
    elif user_input in ('scissor','3'):
        if options == ('scissor','3'):
            print("Tie")
            print("Do you wanna play again!!")
            count_system = count_system
            count_player = count_player
        elif options ==('paper','2'):
            print("Better luck next time.")
            print("Do you wanna play again!!")
            count_system+=1
            count_player = count_player
        elif options == ('rock','1'):
            print("Well played")
            print("Do you wanna play again!!")
            count_system= count_system
            count_player += 1
    elif user_input == 'n':
            # if count_player>count_system:
            #     print("You won!!")
            #     print(f"Your score:{count_player}   Opponent's score:{count_system}")
            # else:
            #     print("Better Luck Next time!!")
            #     print(f"Opponent's score:{count_system}   Your score:{count_player}")
            # break
        if(count_system>count_player):
            print("You lose!")
            print(f"Your score:{count_player}  Opponents score:{count_system}")
            break
        else:
            print("You won!")
            print(f"Your score:{count_player}  Opponents score:{count_system}")
            break