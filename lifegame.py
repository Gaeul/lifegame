import copy

def load():
    inputfile = open("/home/user/Python-3.4.3/lifegame/input_data.txt",'r')
    data = inputfile.read()
    inputfile.close()
    return data
 

def set_board(data):
    print(data)
    game_cell = []
    for i in range(0, 8):
        game_cell.append(data[(i*9) : ((i+1)*9 -1) ])

    cur_board = [[0 for col in range(8)] for row in range(8)]

    for i in range(0, len(game_cell)):
        for j in range(0, len(game_cell)):
            if(game_cell[i][j]=='x'):
                cur_board[i][j]=0
            else:
                cur_board[i][j]=1

    return cur_board

def printBoard(board):
    stdscr.clear()
    curses.start_color()
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)

    stdscr.attron(curses.color_pair(1))
    stdscr.border("#","#","#","#","#","#","#","#")
    stdscr.addstr(cur_board)
    stdscr.refresh()
    stdscr.getch()
    board = next_board
    pass

def runLifeGame(board):
    cur_board = copy.deepcopy(board)
    next_board = copy.deepcopy(cur_board)

    alive_cell = 0

    x = cur_board
    y = cur_board

    for a in range(8):
        for i in range(0, 2):
            for j in range(0, 2):
                if cur_board[i][j] == 1:
                    alive_cell += 1
    x += 1
    y += 1

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
