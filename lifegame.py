def load():
    inputfile = open("/home/user/Python-3.4.3/input_data.txt",'r')
    data = inputfile.read()
    inputfile.close()
    return data


def set_board(data):
    game_cell = []
    for i in range(0, 8):
        game_cell.append(data[(i*9) : ((i+1)*9 -1) ])

    cur_board = [[0 for col in range(8)] for row in range(8)]

    for i in range(0, len(game_cell)):
        for j in range(0, len(game_cell)):
            if(game_cell[i][j]=='X'):
                cur_board[i][j]=0
            else:
                cur_board[i][j]=1

    return cur_board

def printBoard(board):
    ###########################################################
    # 학생들은 이 부분을 구현하여 프로그램을 완성하도록 하세요.
    ###########################################################
    pass

def runLifeGame(board):
    cur_board = board[:]
    next_board = cur_board[:]
    ###########################################################
    # 학생들은 이 부분을 구현하여 프로그램을 완성하도록 하세요.
    ###########################################################
    pass
    return next_board
