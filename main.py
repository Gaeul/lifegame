
import sys
sys.path.append("/home/Python-3.4.3/lifegame")

import lifegame, os, curses

data = lifegame.load()
cur_board = lifegame.set_board(data)
print(cur_board)
time = 500
time_integration = 0

lifegame.stdscr = curses.initscr()
curses.curs_set(0)

lifegame.printBoard(next_board)

while True:
    next_board = lifegame.runLifeGame(cur_board) 
    lifegame.printBoard(next_board)
    cur_board = next_board

    curses.napms(time)
    time_integration+=time
    if(time_integration>5000):
        break
    
curses.endwin()
