# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 23:10:28 2015

@author: RishiBagrodia
"""

from board import * # this will definitely import the GUI from board

def main ():
    
    # this will be the information below the board
    # give player information (wins/losses/names)
    game = Game ()
  
    
    # check for winner 
    # create new game code
    # create "replay" code?
    
    player1 = game.players[0]
    player2 = game.players[1]
    
    p1_wins = [0,0,0] # for w/l/ties
    p2_wins = [0,0,0] # w/l/t
    
    exit = False
    while not exit:
        while not game.finished:
            game.nextMove() # keep game going as long as not done
        
            # THESE MUST BE DEFINED IN BOARD.PY
          game.checkfor_fours
          game.print_board
          
          # DEFINE WINNER IN BOARD.PY AS WELL
        if game.has_won == player1: 
            p1_wins(1) += 1
        
        elif game.has_won == player2:
            p2_wins(1) += 1
        
        printStats(p1_wins, p2_wins)
        
        while True:
            play_again = str(raw_input("Would you like to play again? "))
            
            if play_again.lower() == 'y' or play_again.lower() == 'yes': 
                game.newGame()
                game.printState()
                break
            elif play_again.lower() == 'n' or play_again.lower() == 'no':
                print("Thanks for playing!")
                exit = True
                break
            else:
                print("Command not Recognized"),
        
def printStats(p1_wins, p2_wins):
    # WRITE A PRINT STATS COMMAND TO PRINT ALL THE STATS FOR PLAYER/AI BELOW
    # BOARD
if __name__ == "__main__": # Default "main method" idiom.
    main()