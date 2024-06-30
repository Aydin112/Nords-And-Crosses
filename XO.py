def winchecker():
    win = ' '
    if 3 == [board[0],board[4],board[8]].count('X'):
        win = 'X'
    if 3 == [board[2],board[4],board[6]].count('X'):
        win = 'X'
    if 3 == [board[0],board[4],board[8]].count('O'):
        win = 'O'
    if 3 == [board[0],board[4],board[8]].count('O'):
        win = 'O'

#vertical 
    if 3 == [board[0],board[3],board[6]].count('X'):
        win = 'X'
    if 3 == [board[1],board[4],board[7]].count('X'):
        win = 'X'
    if 3 == [board[2],board[5],board[8]].count('X'):
        win = 'X'

#horzontal 
    if 3 == [board[0],board[1],board[2]].count('X'):
        win = 'X'
    if 3 == [board[3],board[4],board[5]].count('X'):
        win = 'X'
    if 3 == [board[6],board[7],board[8]].count('X'):
        win = 'X'

#vertical 
    if 3 == [board[0],board[3],board[6]].count('O'):
        win = 'O'
    if 3 == [board[1],board[4],board[7]].count('O'):
        win = 'O'
    if 3 == [board[2],board[5],board[8]].count('O'):
        win = 'O'

#horzontal 
    if 3 == [board[0],board[1],board[2]].count('O'):
        win = 'O'
    if 3 == [board[3],board[4],board[5]].count('O'):
        win = 'O'
    if 3 == [board[6],board[7],board[8]].count('O'):
        win = 'O'

    if win == 'O': 
        print('O wins!')

    if win == 'X': 
        print('L bozo!')

def drawboard(board):
    print(f"______")
    print(f"|{board[0]}|{board[1]}|{board[2]}|")
    print(f"|{board[3]}|{board[4]}|{board[5]}|")
    print(f"|{board[6]}|{board[7]}|{board[8]}|")
    print(f"⎻⎻⎻⎻⎻⎻⎻")


def clearboard():
    for index in range(len(board)):
        board[index] = ' '
        #from 0 to 8

def opponent():

    wantstogo = [4,0,2,6,8,5,7,3,1]
    for place in wantstogo:
        if board[place] == "X" or board[place] == "O":
            None
        else: 
            board[place] = "X"
            return




board =['X','X','X',
        'X',' ','X',
        'X','X','X'
        ]





drawboard(board)
clearboard()

while True:
    drawboard(board)
    choice = input(" where to go next? letter,number}")
    if(choice[0]=='A'):
        column = 0
    if(choice[0]=='B'):
        column = 1
    if(choice[0]=='C'):
        column = 2

    if(choice[1]=='1'):
        row = 0
    if(choice[1]=='2'):
        row = 3
    if(choice[1]=='3'):
        row = 6

    board[row + column] = 'O'

    drawboard(board)

    winchecker()
    opponent()
    winchecker()