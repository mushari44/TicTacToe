while True:
    def printBoard(board):
        print(board[7] + '|' + board[8] + '|' + board[9])
        print('-+-+-')
        print(board[4] + '|' + board[5] + '|' + board[6])
        print('-+-+-')
        print(board[1] + '|' + board[2] + '|' + board[3])
        print("\n")


    def again():
        while True:

            Q = input("would you like to play again ? : (y/n)")
            if Q.lower() == "y":
                for key in board.keys():
                    board[key] = ' '
                    printBoard(board)
                break
            elif Q.lower() == "n":
                exit()
            else:
                print("Enter (y/n)")





    def spaceIsFree(position):
        if board[position] == ' ':
            return True
        else:
            return False


    def insertLetter(letter, position):
        if spaceIsFree(position):
            board[position] = letter
            printBoard(board)


            if checkDraw():
                print("Draw!")
                again()

            if checkForWin():

                if letter == 'X':
                    print("Bot wins!")
                    again()

                else:
                    print("Player wins!")
                    again()

            return
        else:
            print("Can't insert there!")
            position = int(input("Please enter new position:  "))
            insertLetter(letter, position)
            return


    def checkForWin():
        if board[7] == board[8] == board[9] != ' ':

            return True
        elif board[4] == board[5] == board[6] != ' ':
            return True
        elif board[1] == board[2] == board[3] != ' ':
            return True
        elif board[7] == board[4] == board[1] != ' ':
            return True
        elif board[8] == board[5] == board[2] != ' ':
            return True
        elif board[9] == board[3] == board[6] != ' ':
            return True
        elif board[7] == board[5] == board[3] != ' ':
            return True
        elif board[9] == board[5] == board[1] != ' ':
            return True
        else:
            return False


    def checkWhichMarkWon(mark):
        if board[7] == board[8] == board[9] == mark:
            return True
        elif board[4] == board[5] == board[6] == mark:
            return True
        elif board[1] == board[2] == board[3] == mark:
            return True
        elif board[7] == board[4] == board[1] == mark:
            return True
        elif board[8] == board[5] == board[2] == mark:
            return True
        elif board[9] == board[3] == board[6] == mark:
            return True
        elif board[7] == board[5] == board[3] == mark:
            return True
        elif board[9] == board[5] == board[1] == mark:
            return True
        else:
            return False


    def checkDraw():
        for key in board.keys():
            if board[key] == ' ':
                return False
        return True




    def playerMove():
        position = int(input("Enter the position for 'O':  "))
        insertLetter(player, position)

        return


    def compMove():
        bestScore = -800
        bestMove = 0
        for key in board.keys():
            if (board[key] == ' '):
                board[key] = bot
                score = minimax(board, 0, False)
                board[key] = ' '
                if (score > bestScore):
                    bestScore = score
                    bestMove = key

        insertLetter(bot, bestMove)
        return


    def minimax(board, depth, isMaximizing):
        if (checkWhichMarkWon(bot)):
            return 1
        elif (checkWhichMarkWon(player)):
            return -1
        elif (checkDraw()):
            return 0

        if (isMaximizing):
            bestScore = -800
            for key in board.keys():
                if (board[key] == ' '):
                    board[key] = bot
                    score = minimax(board, depth + 1, False)
                    board[key] = ' '
                    if (score > bestScore):
                        bestScore = score
            return bestScore

        else:
            bestScore = 800
            for key in board.keys():
                if (board[key] == ' '):
                    board[key] = player
                    score = minimax(board, depth + 1, True)
                    board[key] = ' '
                    if (score < bestScore):
                        bestScore = score
            return bestScore


    board = {1: ' ', 2: ' ', 3: ' ',
             4: ' ', 5: ' ', 6: ' ',
             7: ' ', 8: ' ', 9: ' '}

    printBoard(board)

    print("Positions are as follow:")
    print("7, 8, 9 ")
    print("4, 5, 6 ")
    print("1, 2, 3 ")
    print("\n")
    player = 'O'
    bot = 'X'



    while not checkForWin():


        compMove()
        playerMove()