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

            # check right
            if (x<7):
                if (board[y][x+1] == "-"):
                    positions.append([y, x+1])

            if (x>1):# check left
                if (board[y][x-1] == "-"):
                    positions.append([y, x-1])

            # check up
            if (y>0):
                if (board[y-1][x] == "-"):
                    positions.append([y-1, x])

            # check down
            if (y<7):
                if (board[y+1][x] == "-"):
                    positions.append([y+1, x])

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


    test1 = [['X', '-', '-', 'O', '-', '-', '-', 'X'],
            ['-', '-', '-', '-', '-', '-', '-', '@'],
            ['-', '-', 'O', '@', '-', '-', '-', '-'],
            ['-', 'O', '-', '-', '-', '@', '-', '-'],
            ['-', '-', '-', '-', 'O', '-', 'O', '@'],
            ['-', '-', '@', '-', '-', '-', '-', '-'],
            ['-', 'O', '-', 'O', '@', '-', '&', '-'],
            ['-', '-', '-', '-', '-', '-', '-', '-'],
            ['-', '-', '-', '-', '-', '-', '-', '-'],
            ['X', '-', '-', '-', '-', '-', '-', 'X']]


    findPieces(test1, black, white)

    print("\n",possibleMoves(black, test1))
    print("\n",possibleMoves(white, test1))
