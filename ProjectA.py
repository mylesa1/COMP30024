class main():

    black = []
    white = []
    totalPositions = []

    def findPieces(input, black, white):

        for i in range(8):
            for j in range(8):
                if input[i][j] == "O":
                        white.append([i,j])

                if input[i][j] == "@":
                        black.append([i,j])

        if input[8] == "Moves":
            print("moves")


    def possibleMoves(player, board, totalPositions):

        totalmoves = 0

        for i in range(len(player)):

            positions = []
            y = player[i][0]
            x = player[i][1]

            if (x>0):# check left
                if (board[y][x-1] == "-"):
                    positions.append([y, x-1])
                    totalmoves += 1
                elif x>1 and (board[y][x-1] == "@" or board[y][x-1] == "O"):
                    if (board[y][x-2] == "-"):
                        positions.append([y, x-2])
                        totalmoves += 1

            # check up
            if (y>0):
                if (board[y-1][x] == "-"):
                    positions.append([y-1, x])
                    totalmoves += 1
                elif y>1 and (board[y-1][x] == "@" or board[y+1][x] == "O"):
                    if (board[y-2][x] == "-"):
                        positions.append([y-2, x])
                        totalmoves += 1

            # check right
            if (x<7):

                if (board[y][x+1] == "-"):
                    positions.append([y, x+1])
                    totalmoves += 1
                elif x<6 and (board[y][x+1] == "@" or board[y][x+1] == "O"):
                    if (board[y][x+2] == "-"):
                        positions.append([y, x+2])
                        totalmoves += 1

            # check down
            if (y<7):
                if (board[y+1][x] == "-"):
                    positions.append([y+1, x])
                    totalmoves += 1
                elif y<6 and (board[y+1][x] == "@" or board[y+1][x] == "O"):
                    if (board[y+2][x] == "-"):
                        positions.append([y+2, x])
                        totalmoves += 1

            totalPositions.append(positions)

        print(totalPositions)
        return totalmoves

    empty = [['X', '-', '-', '-', '-', '-', '-', 'X'],
            ['-', '-', '-', '-', '-', '-', '-', '-'],
            ['-', '-', '-', '-', '-', '-', '-', '-'],
            ['-', '-', '-', '-', '-', '-', '-', '-'],
            ['-', '-', '-', '-', '-', '-', '-', '-'],
            ['-', '-', '-', '-', '-', '-', '-', '-'],
            ['-', '-', '-', '-', '-', '-', '-', '-'],
            ['-', '-', '-', '-', '-', '-', '-', '-'],
            ['-', '-', '-', '-', '-', '-', '-', '-'],
            ['X', '-', '-', '-', '-', '-', '-', '-']]

    test1 = [['X', '-', '@', 'O', '-', '-', '-', 'X'],
            ['-', '-', '-', '@', '-', '-', '-', '@'],
            ['-', '-', '-', '-', '-', '-', '-', '-'],
            ['O', '-', '-', '-', 'O', '-', '-', '-'],
            ['-', '-', '-', '-', '-', '-', '-', '-'],
            ['-', '-', '-', '-', '-', '-', '-', '-'],
            ['@', '-', '@', '-', '@', '-', '-', '-'],
            ['X', '-', '-', '-', '-', '-', '-', 'X'],
            "Moves"]

    findPieces(test1, black, white)

    movesB = possibleMoves(black, test1, totalPositions)
    movesW = possibleMoves(white, test1, totalPositions)

    print(movesB)
    print(movesW)
