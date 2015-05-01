# Python Final Project
# Connect Four
#
# Erik Ackermann
# Charlene Wang
#
# Connect 4 Module
# February 27, 2012

import os
import time
from Tkinter import *
from tkFont import Font 
from copy import deepcopy
from minimax_ABP import *

t = 1;
p_win = 0;
c_win = 0;
difficulty = 0;

class Player(object):
    
    name = None
    color = None
    def __init__(self, name, color):
        self.type = "Human"
        self.name = name
        self.color = color
    

class AIPlayer(Player):
    
    difficulty = None
    def __init__(self, name, color, difficulty):
        self.type = "AI"
        self.name = name
        self.color = color
        self.difficulty = difficulty

class Board:
 
  nodes = {}
 
  def __init__(self,other=None):
    self.player = 'X'
    self.opponent = 'O'
    self.empty = ' '
    self.width = 7
    self.height = 6
    self.fields = {}
    for y in range(self.height):
      for x in range(self.width):
        self.fields[x,y] = self.empty
    # copy constructor
    if other:
      self.__dict__ = deepcopy(other.__dict__)
 
  def move(self,x):
    global t
    board = Board(self)
    if t > 0:
        for y in range(board.height):
            if board.fields[x,y] == board.empty:
                board.fields[x,y] = board.player
                t = -1
                break
    elif t < 0:
        for z in range(board.height):
            if board.fields[x,z] == board.empty:
                board.fields[x,z] = board.opponent
                t = 1
                break
    return board
    
  def won(self):
    # horizontal
    for y in range(self.height):
      winning = [ ]
      for x in range(self.width):
        if self.fields[x,y] == self.opponent:
          winning.append((x,y))
          if len(winning) >= 4:
            return winning
        else:
          winning = [ ]
    # vertical
    for x in range(self.width):
      winning = [ ]
      for y in range(self.height):
        if self.fields[x,y] == self.opponent:
          winning.append((x,y))
          if len(winning) >= 4:
            return winning
        else:
          winning = [ ]
   # diagonal
    for cx in range(self.width-1):
      sx,sy = max(cx-2,0),abs(min(cx-2,0))
      winning = [ ]
      for cy in range(self.height):
        x,y = sx+cy,sy+cy
        if x<0 or y<0 or x>=self.width or y>=self.height:
          continue
        if self.fields[x,y] == self.opponent:
          winning.append((x,y))
          if len(winning) >= 4:
              return winning
        else:
          winning = [ ]
    # other diagonal
    for cx in range(self.width-1):
      sx,sy = self.width-1-max(cx-2,0),abs(min(cx-2,0))
      winning = [ ]
      for cy in range(self.height):
        x,y = sx-cy,sy+cy
        if x<0 or y<0 or x>=self.width or y>=self.height:
          continue
        if self.fields[x,y] == self.opponent:
          winning.append((x,y))
          if len(winning) == 4:
              return winning
        else:
          winning = [ ]
   
  def won_player(self):
    # horizontal
    for y in range(self.height):
      winplayer = [ ]
      for x in range(self.width):
        if self.fields[x,y] == self.player:
          winplayer.append((x,y))
          if len(winplayer) >= 4:
            return winplayer
        else:
          winplayer = [ ]
    # vertical
    for x in range(self.width):
      winplayer = [ ]
      for y in range(self.height):
        if self.fields[x,y] == self.player:
          winplayer.append((x,y))
          if len(winplayer) >= 4:
            return winplayer
        else:
          winplayer = [ ]
    # diagonal
    for cx in range(self.width-1):
      sx,sy = max(cx-2,0),abs(min(cx-2,0))
      winplayer = [ ]
      for cy in range(self.height):
        x,y = sx+cy,sy+cy
        if x<0 or y<0 or x>=self.width or y>=self.height:
          continue
        if self.fields[x,y] == self.player:
          winplayer.append((x,y))
          if len(winplayer) == 4:
              return winplayer
        else:
          winplayer = [ ]
    # other diagonal
    for cx in range(self.width-1):
      sx,sy = self.width-1-max(cx-2,0),abs(min(cx-2,0))
      winplayer = [ ]
      for cy in range(self.height):
        x,y = sx-cy,sy+cy
        if x<0 or y<0 or x>=self.width or y>=self.height:
          continue
        if self.fields[x,y] == self.player:
          winplayer.append((x,y))
          if len(winplayer) == 4:
              return winplayer
        else:
          winplayer = [ ]
   
        
class GUI:
    
  board = None
  round = None
  game_name = u"Connect Four"
  finished = None
  winner = None
  turn = None
  units = [None, None]
  colors = ["red", "black"]
 
  def __init__(self):
    global difficulty
    os.system( [ 'clear', 'cls' ][os.name == 'nt' ] )
    print(u"Welcome to {0}!".format(self.game_name))
    player_name = str(raw_input("What is Player 1's name? "))
    self.units[0] = Player(player_name, self.colors[0])
    while difficulty == 0: 
        diff = int(raw_input("How badly do you want to lose to the AI? (1 - 3) "))
        if diff > 3 or diff < 1:
            print("Invalid input")
        else:
            difficulty = diff + 1
    print(u"Generating Computer: Prepare to lose")
    comp_name = "Comp" 
    self.units[1] = AIPlayer(comp_name, self.colors[1], difficulty)
    print("{0} will be {1}".format(self.units[0].name, self.colors[0]))    
    print("{0} will be {1}".format(self.units[1].name, self.colors[1]))
    time.sleep(1)      

    self.clocktime = time.strftime("%I:%M:%S")
    self.app = Tk()
    self.app.title('The Gang Plays Connect Four')
    self.app.resizable(width=False, height=False)
    self.board = Board()
    self.buttons = {}
    self.frame = Frame(self.app, borderwidth=1, relief="raised")
    self.tiles = {}
   
    for x in range(self.board.width):
      handler = lambda x=x: self.move(x)
      button = Button(self.app, command=handler, font=Font(family="Arial", size=14), text=x+1)
      button.grid(row=0, column=x, sticky="WE")
      self.buttons[x] = button
    self.frame.grid(row=1, column=0, columnspan=self.board.width)
    for x,y in self.board.fields:
      tile = Canvas(self.frame, width=60, height=50, bg="navy", highlightthickness=0)
      tile.grid(row=self.board.height-1-y, column=x)
      self.tiles[x,y] = tile
    handler = lambda: self.reset()
    self.newgame = Button(self.app, command=handler, text='Start Over')
    self.newgame.grid(row=2, column=2, columnspan=(self.board.width/2), sticky="WE")
    self.wins = Text(self.app, height=2, width=15)
    self.wins.insert(END, player_name)
    self.wins.insert(END, " Wins:\n%.0f" % p_win)
    self.wins.tag_configure("center", justify='center')
    self.wins.tag_add("center", 1.0, "end")
    self.wins.grid(row=3, column = 0, columnspan=(self.board.width/3), sticky="WE")
    self.compinfo = Text(self.app, height=2, width=15)
    self.compinfo.insert(END, comp_name)
    self.compinfo.insert(END, " Wins:\n%.0f" % c_win)
    self.compinfo.tag_configure("center", justify='center')
    self.compinfo.tag_add("center", 1.0, "end")
    self.compinfo.grid(row=3, column = 5, columnspan=(self.board.width/3), sticky="WE")
    self.update()
  
  def change(self, GUI_board):
      mm_board = []
      for i in xrange(6):
          mm_board.append([])
          for j in xrange(7):
              mm_board[i].append(' ')
      for y in range(6):
          for x in range(7):
              mm_board[y][x] = GUI_board[x,y]
      return mm_board  
 
  def reset(self):
    global t
    self.board = Board()
    self.update()
    t = 1
    self.newgame["text"] = "Start Over"
    
  def move(self,x):
    global difficulty
    self.board = self.board.move(x)
    self.update()
    fields = self.board.fields
    self.state = self.change(fields)
    m = Minimax(self.state, "O")
    best_move = m.bestMove(difficulty, self.state, "O")
    self.board = self.board.move(best_move)
    self.update()

 
  def update(self):
    global c_win, p_win, t
    for (x,y) in self.board.fields:
      text = self.board.fields[x,y]
      if (text==' '):
        self.tiles[x,y].create_oval(10, 5, 50, 45, fill="yellow", outline="blue", width=1)
      if (text=='X'):
        self.tiles[x,y].create_oval(10, 5, 50, 45, fill="red", outline="blue", width=1)
      if (text=='O'):
        self.tiles[x,y].create_oval(10, 5, 50, 45, fill="black", outline="blue", width=1)
    for x in range(self.board.width):
      if self.board.fields[x,self.board.height-1]==self.board.empty:
        self.buttons[x]['state'] = 'normal'
      else:
        self.buttons[x]['state'] = 'disabled'
    winning = self.board.won()
    winplayer = self.board.won_player()
    if winning:
      for x,y in winning:
        self.tiles[x,y].create_oval(10, 5, 50, 45, fill="white")
      for x in range(self.board.width):
        self.buttons[x]['state'] = 'disabled'
      c_win += 1
      t = 1
      self.compinfo.delete('2.0')
      self.compinfo.insert(END, c_win)
      self.newgame["text"] = "Play Again?"
      print "You lost (of course), click play again to play (lose) again!"
    if winplayer:
       for x,y in winplayer:
         self.tiles[x,y].create_oval(10, 5, 50, 45, fill="white")
       for x in range(self.board.width):
         self.buttons[x]['state'] = 'disabled'
       p_win += 1
       t = 1
       self.wins.delete('2.0')
       self.wins.insert(END, p_win)
       self.newgame["text"] = "Play Again?"
       print "You won (somehow), click play again to play (lose) now!"
  
  def mainloop(self):
    self.app.mainloop()
 
if __name__ == '__main__':
  GUI().mainloop()