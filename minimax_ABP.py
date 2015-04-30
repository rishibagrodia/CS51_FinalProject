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

import copy

class node(object):
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, obj):
        self.children.append(obj)

class Minimax(object):
    
    def __init__(self, state, color):
        self.state = state
        self.color = color
     
     
#    def make_children(self, tree, state, color, depth):
 #       if depth > 0:            
  #          new_states = [None] * 7            
   #         for i in range(7):
    #            new_states[i] = state
       #         for j in xrange(6):
        #            if new_states[i][j][i] == ' ':
         #               new_states[i][j][i] = color
     #       for i in range(7):
      #          if color == "x":
       #             color = "o"
        #        else: color = "x"
         #       tree.add_child(node(new_states[i]))
          #      self.make_children(tree.children[i], new_states[i], color, depth-1)
      #  return tree

        
    def build_tree(self, state, color, depth):       
        tree = node(state)    
        if depth == 0:
            return tree
        else:
            new_states = [None] * 7
            for i in xrange(7):
                new_states[i] = copy.deepcopy(state)
                for j in xrange(6):
                    if new_states[i][j][i] == ' ':
                        new_states[i][j][i] = color
                        printState( new_states[i])
                        break                            
            if color == "x":
                color = "o"
            else: color = "x"
            for i in xrange(7):
                tree.add_child(self.build_tree(new_states[i], color, depth-1))
            return tree
                    
        
    def rank(self, state):
            comp = 'o'
            hum = 'x'        
            rank = 0
            # check for ertical 4's        
            for i in xrange(7):
                colcount = 0
                for j in xrange(5):
                    if state[j][i] == state[j+1][i]:
                        colcount += 1
                        piece = state[j][i]
                    else: break                    
                if colcount >= 4:
                    if piece == comp:
                        rank += 10
                    else:
                        rank -=15
            return rank
                

    def minimax(self, node, depth, color):      
        if depth == 0 or node.children == []:
            return self.rank(node.value)
        if color == "o":
            bestValue = -10
            for i in xrange(7):
                val = self.minimax(node.children[i], depth - 1, "x")
            bestValue = max(bestValue, val)
            return bestValue
        else:
            bestValue = 10
            for i in xrange(7):
                val = self.minimax(node.children[i], depth - 1, 'o')
            bestValue = min(bestValue, val)
            return bestValue

    def bestestMove(self, node, color, depth):     
        bestMove = None
        bestValue = -100        
        for i in xrange(7):
            currentval = self.minimax(node.children[i], depth, color)
            if currentval > bestValue:
                bestValue = currentval
                bestMove = i
        return bestMove

    def bestMove(self, difficulty, state, color):
        tree = self.build_tree(state, color, difficulty)      
        return self.bestestMove(tree, color, difficulty)

def printState(state):
        # cross-platform clear screen

        for i in xrange(5, -1, -1):
            print("\t"),
            for j in xrange(7):
                print("| " + str(state[i][j])),
            print("|")
        print("\t  _   _   _   _   _   _   _ ")
        print("\t  1   2   3   4   5   6   7 ")

m = []
for i in xrange(6):
    m.append([])
    for j in xrange(7):
        m[i].append(' ')
    

buildtree = Minimax(m, "x")
buildtree.build_tree(m, "x", 5)
       
