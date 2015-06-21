import sys
sys.path.append("/home/user/git/lifegame")

import lifegame, os
import curses

lifegame.stdscr = curses.initscr()
curses.curs_set(0)
lifegame.win1 = curses.newwin(22, 52, 1, 2)
curses.noecho()
curses.start_color()
curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
while True:
    lifegame.stdscr.attron(curses.color_pair(1))
    lifegame.stdscr.border("#","#","#","#","#","#","#","#")
    lifegame.stdscr.addstr(20,30,"Press any key to START")
    lifegame.stdscr.getch()
    lifegame.stdscr.refresh()
    lifegame.startGame()
    
curses.endwin()
