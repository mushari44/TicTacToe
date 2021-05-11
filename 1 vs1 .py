
theboard = {'7':' ','8':' ','9':' ',
            '4':' ','5':' ','6':' ',
            '1':' ','2':' ','3':' '}
bord_keys = []
for key in theboard:
    bord_keys.append(key)
def game():


    turn = 'X'
    count = 0

    while True:
        printboard(theboard)
        move=input()
        if theboard[move]== " ":
            theboard[move] = turn
            count+=1
        else:
            print("this place is already taken")
            continue

        if count >=0:
            if theboard['7']==theboard['8']==theboard['9']!=' ':
                printboard(theboard)
                print("Game Over,\n----"+turn+"----""won")
                break

            elif theboard['4']==theboard['5']==theboard['6']!=' ':
                printboard(theboard)
                print("Game Over,\n----"+turn+ "----""won")
                break
            elif theboard['1']==theboard['2']==theboard['3']!=' ':
                printboard(theboard)
                print("Game Over,\n----"+turn+ "----""won")
                break
            elif theboard['7']==theboard['4']==theboard['1']!=' ':
                printboard(theboard)
                print("Game Over,\n----"+turn+ "----""won")
                break
            elif theboard['8']==theboard['5']==theboard['2']!=' ':
                printboard(theboard)
                print("Game Over,\n----"+turn+ "----""won")
                break

            elif theboard['9']==theboard['3']==theboard['6']!=' ':
                printboard(theboard)
                print("Game Over,\n----"+turn+ "----""won")
                break

            elif theboard['7']==theboard['5']==theboard['3']!=' ':
                printboard(theboard)
                print("Game Over,\n----"+turn+ "----""won")
                break
            elif theboard['9']==theboard['5']==theboard['1']!=' ':
                printboard(theboard)
                print("Game Over,\n----"+turn+ "----""won")
                break
        if count==9:
            print("Game Over ,\n it is a tie")
            printboard(theboard)
            break
        if turn=='X':
            turn='O'

        else:
            turn='X'
def printboard(board):
    print(board['7']+'|'+board['8']+'|'+board['9'])
    print("-----")
    print(board['4']+'|'+board['5']+'|'+board['6'])
    print("-----")
    print(board['1']+'|'+board['2']+'|'+board['3'])
game()

while True:
        again = input("do you want to play again?  (yes/no)")
        if again.lower()=='yes':

             for key in bord_keys:
                 theboard[key] = ' '
             game()
        if again.lower()=='no':
            exit()

        else:
            respinse = input("Enter yes or no")
            if respinse=="yes":
                for key in bord_keys:
                    theboard[key] = ' '
                game()

            elif respinse == "no":
                print("thank you")
                break