# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 22:50:40 2015

@author: RishiBagrodia
"""

# This module will be for the connect4 GUI, so the entire game board 
# player interface. 

# We will provide abstractions for the player and the AI and of course the 
# algorithm will be hidden from the client. The board will be visible and the 
# relevant player informations will all be visible as well.

#  All values will be shown except for round number (maybe), AI difficulty - 
#  as in the level of best moves the AI will pick, and player's past moves
#  if we store it in a database for the replay feature

# the client will simply need to run (MAIN.py) and input their name, possibly
# the difficulty of the AI. 

# This component will ensure complete board functionality (not all of the display)
# as a lot will be in main.py as well. 
"""
class Game(object):
    #definitions for variables
    # board
    # players
    # score (current games won/lost/drew)
    # time (clock to keep track of time?)
    # turn 
    # pieces (1 vs 2 maybe or x vs o)
    # round (number of rounds played so far)
    def switch_turns(self):
            # switch turn from comp to player and vice versa
    def pause_game(self):
        # pause timer, and don't let player or comp move 
    def undo(self):
            # undos a move if player goofs by accident
    def game_over(self):
        # check available moves, check if it is a stalemate, check next move
        # player
    def checkfor_fours(self):
            # check vertical fours
            # def check_vertical(self, row, col)
            # check horizontal fours
            # def check_horizontal(self, row,col)
            # check diagonal fours
            # def check_diagonal(self,row, col)
    def winning_four(self):
        # color the winning four chips if player or AI gets four in a row
    def print_board(self)
        # Print the board after each turn
 def printState(self):
        # cross-platform clear screen
        os.system( [ 'clear', 'cls' ][ os.name == 'nt' ] )
        print(u"{0}!".format(self.game_name))
        print("Round: " + str(self.round))

        for i in xrange(5, -1, -1):
            print("\t"),
            for j in xrange(7):
                print("| " + str(self.board[i][j])),
            print("|")
        print("\t  _   _   _   _   _   _   _ ")
        print("\t  1   2   3   4   5   6   7 ")

        if self.finished:
            print("Game Over!")
            if self.winner != None:
                print(str(self.winner.name) + " is the winner")
            else:
                print("Game was a draw")
class Player(object):

    
    type = None # possible types are "Human" and "AI"
    name = None
    color = None
    def __init__(self, name, color):
        self.type = "Human"
        self.name = name
        self.color = color
    
    def move(self, state):
        print("{0}'s turn.  {0} is {1}".format(self.name, self.color))
        column = None
        while column == None:
            try:
                choice = int(raw_input("Enter a move (by column number): ")) - 1
            except ValueError:
                choice = None
            if 0 <= choice <= 6:
                column = choice
            else:
                print("Invalid choice, try again")
        return column


class AIPlayer(Player):

    
    difficulty = None
    def __init__(self, name, color, difficulty=5):
        self.type = "AI"
        self.name = name
        self.color = color
        self.difficulty = difficulty
        
    def move(self, state):
        print("{0}'s turn.  {0} is {1}".format(self.name, self.color))
        
        # sleeping for about 1 second makes it looks like he's thinking
        #time.sleep(random.randrange(8, 17, 1)/10.0)
        #return random.randint(0, 6)
        
        m = Minimax(state)
        best_move, value = m.bestMove(self.difficulty, state, self.color)
        return best_move
"""