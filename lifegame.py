def load():
    inputfile = open("/home/user/Python-3.4.3/lifegame/input_data.txt",'r')
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
#lifegame.stdscr = curses.initscr()
#curses.curs_set(0)
    curses.start_color()
    curses.init_pair(1, curses.COLOR_RED, COLOR_BLACK)
    lifegame.stdscr.attron(curses.color_pair(1))
    lifegame.stdscr.addstr(cur_board)
    lifegame.stdscr.refresh()
    lifegame.stdscr.getch()
    board = next_board
    pass

def runLifeGame(board):
    cur_board = copy.deepcopy(board)
    next_board = copy.deepcopy(cur_board)

    alive_cell = 0
    
    for i in range(cur_board[i], cur_board[i+2]):
        for j in range(cur_board[j], cur_board[j+2]):
            if cur_board[i][j] == 1:
                alive_cell += 1
    return alive_cell


    if cur_board ==1 and (alive_cell <= 1 or alive_cell >= 4):
        next_board[i][j] = 0
    else:
        pass
    
    if cur_board == 1 and alive_cell == 3:
        next_board[i][j] = 1
    else:
        pass

    pass
    return next_board
