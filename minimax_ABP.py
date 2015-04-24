# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 23:16:32 2015

@author: RishiBagrodia
"""

# Everything in this file will be hidden from the client. The main part of our
# project will be implementing a unique and novel minimax algorithm (or genetic)
# that builds upon our connect four GUI to create an AI player that can win over
# 90% of the time. We will import this minimax algorithm to board.py in order
# to have the AI implement this method at every turn

# We will look 5 turns ahead to determine the best method. We will expose AI
# difficulty but nothing else in order to keep the AI formula hidden from the 
# player

# Minimax will take in the difficulty as an input, but nothing else (we assume
# this will have to be implented as an if else clause for different states)
"""
class Minimax(object):
    
    def bestMove(self):
        def search(....):
            # search the tree using alpha-beta pruning
        def is_legal(self):
            # checks if the best move is a legal move (probably should be)
            # but good extra corner case check given full board
        def game_over(self):
            # check if game is over 
        def value(self):
            # Evaluate all board configurations and the values for each diff
            # board config that could result from each move
        def check2_moves(self):
            # check 2 moves ahead for better AI 
            # here we will use the genetic algorithm?
        def 
"""
from connect4 import Game

class node(object):
    def __init__(self, value, children = []):
        self.value = value
        self.children = children

class Minimax(object):
    
    def __init__(self, state, color):
        self.state = state
        self.color = color
        
    def bestMove(self, difficulty, state, color):
        return 3
     
    def make_children(self, state, color):
            children = []
            for i in range(7):
                children[i]=state
                for j in xrange(6):
                    if children[i][j][i] == ' ':
                        children[i][j][i] = color
            return children
        
    def build_tree(self, state, color, depth):       
        tree = node(state, self.make_children(state, color))
        build_tree(self, state, color, depth-1)
            
            
    
    def game_over(self, state_new):
        Game.checkForFours
        
        