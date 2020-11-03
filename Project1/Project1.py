import termcolor as tc
def CreateBoard(field):
    for rows in range(12):

        if rows % 2 == 0:
            practicalRow = int(rows/2)

            for columns in range(13):
                if columns % 2 ==0:
                    practicalColumn = int(columns/2)
                    if columns != 13:
                        print(field[practicalRow][practicalColumn],end="")

                    else:
                        print(field[practicalRow][practicalColumn])

                else:
                    print("|",end="")

        else:
            print("\n--------------")

            #  0   1   2   3   4   5   6
PlayArea =  [[" "," "," "," "," "," "," "],  # 0
             [" "," "," "," "," "," "," "],  # 1
             [" "," "," "," "," "," "," "],  # 2
             [" "," "," "," "," "," "," "],  # 3
             [" "," "," "," "," "," "," "],  # 4
             [" "," "," "," "," "," "," "]]  # 5

CreateBoard(PlayArea)

Player = 1

# function for win condition
def WinCondition(board,x,y,piece):
    # condition for row (0-3)
    if board[0][y]==piece and board[1][y]== piece and board[2][y]== piece and board[3][y]==piece:
        return True
    # condition for row (1-4)
    if board[1][y]== piece and board[2][y]== piece and board[3][y]== piece and board[4][y]==piece:
        return True
    # condition for row (2-5)
    if board[2][y] == piece and  board[3][y] == piece and  board[4][y] == piece and  board[5][y]==piece:
        return True

    # condition for column (0-3)
    if board[x][0] == piece and   board[x][1] == piece and   board[x][2]== piece and   board[x][3]==piece :
        return True
     # condition for column (1-4)
    if board[x][1] == piece and  board[x][2] == piece and  board[x][3] == piece and  board[x][4]==piece:
        return True
    # condition for column (2-5)
    if board[x][2] == piece and  board[x][3] == piece and  board[x][4] == piece and  board[x][5]==piece:
        return True
    # condition for column (3-6)
    if board[x][3] == piece and  board[x][4] == piece and  board[x][5] == piece and  board[x][6]==piece:
        return True
    # condition for up diagonal 3
    if x+y == 3 and board[3][0] == piece and board[2][1] == piece and board[1][2] == piece and board[0][3] == piece:
        return True
    # condition for up diagonal 4 (1st possibility)
    if x+y == 4 and board[4][0] == piece and board[3][1] == piece and board[2][2] == piece and board[1][3] == piece:
        return True

    # condition for up diagonal 4 (2nd possibility)
    if x + y == 4 and  board[3][1] == piece and board[2][2] == piece and board[1][3] == piece and board[0][4] == piece:
        return True

    # condition for up diagonal 5 (1st possibility)
    if x + y == 5 and board[5][0] == piece and board[4][1] == piece and board[3][2] == piece and board[2][3] == piece:
        return True
    # condition for up diagonal 5 (2nd possibility)
    if x + y == 5 and board[4][1] == piece and board[3][2] == piece and board[2][3] == piece and board[1][4] == piece:
        return True

    # condition for up diagonal 5 (3rd possibility)
    if x + y == 5 and board[3][2] == piece and board[2][3] == piece and board[1][4] == piece and board[0][5] == piece:
        return True

    # condition for up diagonal 6 (1st possibility)
    if x + y == 6 and board[5][1] == piece and board[4][2] == piece and board[3][3] == piece and board[2][4] == piece:
        return True

    # condition for up diagonal 6 (2nd possibility)
    if x + y == 6 and board[4][2] == piece and board[3][3] == piece and board[2][4] == piece and board[1][5] == piece:
        return True

    # condition for up diagonal 6 (3rd possibility)
    if x + y == 6 and board[3][3] == piece and board[1][4] == piece and board[1][5] == piece and board[0][6] == piece:
        return True
    # condition for up diagonal 7 (1st possibility)
    if x + y == 7 and board[5][2] == piece and board[4][3] == piece and board[3][4] == piece and board[2][5] == piece:
        return True

    # condition for up diagonal 7 (2nd possibility)
    if x + y == 7  and board[4][3] == piece and board[3][4] == piece and board[2][5] == piece and board[1][6] == piece:
        return True

    # condition for up diagonal 8
    if x + y == 8 and board[5][3] == piece and board[4][4] == piece and board[3][5] == piece and board[2][6] == piece:
        return True

    # condition for down diagonal 0
    if (x+y)%2==0 and board[2][0] == piece and board[3][1] == piece and board[2][2] == piece and board[5][3] == piece:
        return True
    if (x+y)%2==0 and board[0][0] == piece and board[1][1] == piece and board[2][2] == piece and board[3][3] == piece:
        return True
    if (x+y)%2==0 and board[1][1] == piece and board[2][2] == piece and board[3][3] == piece and board[4][4] == piece:
        return True
    if (x+y)%2==0 and board[2][2] == piece and board[3][3] == piece and board[4][4] == piece and board[5][5] == piece:
        return True
    if (x+y)%2==0 and board[0][2] == piece and board[1][3] == piece and board[2][4] == piece and board[3][5] == piece:
        return True
    if (x+y)%2==0 and board[1][3] == piece and board[2][4] == piece and board[3][5] == piece and board[4][6] == piece:
        return True
    # condition for up diagonal 1
    if (x+y)%2==1 and board[1][0] == piece and board[2][1] == piece and board[3][2] == piece and board[4][3] == piece:
        return True
    if (x+y)%2==1 and board[2][1] == piece and board[3][2] == piece and board[4][3] == piece and board[5][4] == piece:
        return True
    if (x+y)%2==1 and board[0][1] == piece and board[1][2] == piece and board[2][3] == piece and board[3][4] == piece:
        return True
    if (x+y)%2==1 and board[1][2] == piece and board[2][3] == piece and board[3][4] == piece and board[4][5] == piece:
        return True
    if (x+y)%2==1 and board[2][3] == piece and board[3][4] == piece and board[4][5] == piece and board[5][6] == piece:
        return True
    if (x+y)%2==1 and board[0][3] == piece and board[1][4] == piece and board[2][5] == piece and board[3][6] == piece:
        return True
    return False

while True:
    print(f"\nPlayer {Player} turn.")       # Which player's turn; {Player} = 1/2.
    MoveRow = int(input("Please Enter the row (0-5):\n"))
    MoveColumn = int(input("Please Enter the column(0-6):\n"))
    if Player == 1:
        if PlayArea[MoveRow][MoveColumn] == " ":
            PlayArea[MoveRow][MoveColumn] = tc.colored("X","white","on_red")
            if WinCondition(PlayArea,MoveRow,MoveColumn,tc.colored("X","white","on_red")):
                print(tc.colored("Player 1 wins!! Congratulations!","grey","on_yellow",attrs=["reverse","blink"]))
                CreateBoard(PlayArea)
                break
            Player = 2      # assigns 2 in "Player" variable.

    else:
        if PlayArea[MoveRow][MoveColumn] == " ":
            PlayArea[MoveRow][MoveColumn] = tc.colored("O","white","on_grey")
            if WinCondition(PlayArea, MoveRow, MoveColumn,tc.colored("O","white","on_grey")):
                print(tc.colored("Player 2 wins!! Congratulations!","grey","on_yellow",attrs=["reverse","blink"]))
                CreateBoard(PlayArea)
                break

            Player = 1  # assigns 1 in "Player variable.

    CreateBoard(PlayArea)