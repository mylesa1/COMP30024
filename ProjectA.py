class main():

    black = []
    white = []

    def findPieces(input, black, white):

        for i in range(8):
            for j in range(8):

                if input[i][j] == "O":
                        white.append([i,j])

                if input[i][j] == "@":
                        black.append([i,j])


    def possibleMoves(player, board):

        totalPositions = []

        for i in range(len(player)):

            positions = []
            pos = player[i]

            y = pos[0]
            x = pos[1]

            if (x>0):# check left
                if (board[y][x-1] == "-"):
                    positions.append([y, x-1])
                elif x>1 and (board[y][x-1] == "@" or board[y][x-1] == "O"):

                    if (board[y][x-2] == "-"):

                        positions.append([y, x-2])

            # check up
            if (y>0):
                if (board[y-1][x] == "-"):
                    positions.append([y-1, x])
                elif y>1 and (board[y-1][x] == "@" or board[y+1][x] == "O"):
                    if (board[y-2][x] == "-"):
                        positions.append([y-2, x])

            # check right
            if (x<7):

                if (board[y][x+1] == "-"):
                    positions.append([y, x+1])

                if x<6 and (board[y][x+1] == "@" or board[y][x+1] == "O"):

                    if (board[y][x+2] == "-"):
                        positions.append([y, x+2])

            # check down
            if (y<7):
                if (board[y+1][x] == "-"):
                    positions.append([y+1, x])
                elif y<6 and (board[y+1][x] == "@" or board[y+1][x] == "O"):
                    if (board[y+2][x] == "-"):
                        positions.append([y+2, x])

            totalPositions.append(positions)

        return totalPositions

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
            ['0', '-', '-', '-', '0', '-', '-', '-'],
            ['-', '-', '-', '-', '-', '-', '-', '-'],
            ['-', '-', '0', '-', '-', '-', '-', '-'],
            ['@', '-', '@', 'O', '@', '-', '-', '-'],
            ['X', '-', '-', '-', '-', '-', '-', 'X']]


    findPieces(test1, black, white)

    movesB = possibleMoves(black, test1)
    movesW = possibleMoves(white, test1)

    print("black \n",movesB)
    print("\n white \n",movesW)
