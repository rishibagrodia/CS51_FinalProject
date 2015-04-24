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

class node(object):
    def __init__(self, value, children = []):
        self.value = value
        self.children = children

class Minimax(object):
    
    def __init__(self, state, color):
        self.state = state
        self.color = color
     
    def make_children(self, state, color, depth):
        if depth > 0:
            children = [None] * 7            
            new_states = [None] * 7            
            for i in range(7):
                new_states[i] = state
                for j in xrange(6):
                    if new_states[i][j][i] == ' ':
                        new_states[i][j][i] = color
            for i in range(7):
                if color == "x":
                    color = "o"
                else: color = "x"
                children[i]=node(new_states[i], self.make_children(new_states[i], color, depth-1))
            return children

        
    def build_tree(self, state, color, depth):       
        return node(state, self.make_children(state, color, depth))
        
    def rank(self, state, color):
        rank = 0               
        for i in xrange(7):
            colcount = 0
            for j in xrange(6):
                if state[i][j] == state[i][j+1]:
                    colcount += 1
                else: break                    
            if colcount >= 4:
                rank += 10                

    def minimax(self, node, depth, color):
        if depth == 0: # or node is a terminal node
            return self.rank(node[0])
        if color == "o":
            bestValue = -10
            for i in xrange(7):
                val = self.minimax(node[1][i], depth - 1, "x")
                bestValue = max(bestValue, val)
            return bestValue
        else:
            bestValue = 10
            for i in xrange(7):
                val = self.minimax(node[1][i], depth - 1, 'o')
                bestValue = min(bestValue, val)
            return bestValue

    def bestestMove(self, node, color, depth):
        bestMove = None        
        bestValue = -10        
        for i in xrange(7):
            currentval = self.minimax(node[1][i], depth, color)
            if currentval > bestValue:
                bestValue = currentval
                bestMove = i
        return bestMove

    def bestMove(self, difficulty, state, color):
        tree = self.build_tree(state, color, difficulty)
        return self.bestestMove(tree[0], color, difficulty)