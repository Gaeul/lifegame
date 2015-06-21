import copy
import curses
import lifegame


def load():
    inputfile = open("/home/user/git/lifegame/input_data.txt",'r')
    data = inputfile.read()
    inputfile.close()
    return data
 

def set_board(data):
    game_cell = []
    for i in range(0, 20):
        game_cell.append(data[(i*51) : ((i+1)*51 -1) ])
    
    cur_board = [[0 for col in range(50)] for row in range(20)]

    for i in range(20):
        for j in range(50):
            if(game_cell[i][j]=='X'):
                cur_board[i][j] = 0
            else:
                cur_board[i][j] = 1
    return cur_board

def printBoard(board):
    win1 = curses.newwin(22, 52, 1, 2)
    curses.noecho()
    curses.start_color()
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
    stdscr.attron(curses.color_pair(1))
    stdscr.border("#","#","#","#","#","#","#","#")
    stdscr.addstr(20,30,"Press any key to START")
    stdscr.getch()
    stdscr.refresh()
           
    pass

def runLifeGame(board):
    cur_board = [[0 for col in range(50)] for row in range(20)]
    next_board = [[0 for col in range(50)] for row in range(20)]

    for i in range(20):
        for j in range(50):
            cur_board[i][j] = next_board[i][j] = board[i][j]
            
    for a in range(20):
        for b in range(50):
            alive_cell = 0
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if i==0 and j==0:
                        continue
                    try :
                        if cur_board[a + i][b + j] == 1:
                            alive_cell += 1
                    except IndexError:
                        continue
                        

            if cur_board[a][b] == 1 and (alive_cell <= 1 or alive_cell >= 4):
                next_board[a][b] = 0
            
            elif cur_board[a][b] == 1  and (alive_cell == 3 or alive_cell == 2):
                continue

            elif cur_board[a][b] == 0 and alive_cell == 3:
                next_board[a][b] = 1

    pass
    return next_board

def newWindow(board):

    curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    win1.attron(curses.color_pair(2))
    win1.border("#","#","#","#","#","#","#","#")
    for i in range(20):
        for j in range(50):
            y = i+1
            x = j+1
            if board[i][j] == 1:
                win1.addstr(y, x, "*")
            else:
                win1.addstr(y, x, " ")
    win1.refresh()


def startGame():
    cur_board = []
    next_board = []

    data = load()
    cur_board = set_board(data)
    time = 500
    time_integration = 0
    #printBoard(cur_board)
    win1.nodelay(1)
    while True:
        c = win1.getch()
        if c != -1:
            break
        next_board = runLifeGame(cur_board)
        newWindow(next_board)
        cur_board = next_board

        curses.napms(time)
        time_integration+=time
        
        if(time_integration>5000):
            break
