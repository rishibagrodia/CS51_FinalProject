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
                        break                            
            if color == "x":
                color = "o"
            else: color = "x"
            for i in xrange(7):
                tree.add_child(self.build_tree(new_states[i], color, depth-1))
            return tree
                    
        
    def check_board(self, state, color, length):
        total = 0
        
        """
        # check for vertical's        
        for i in xrange(7):
            count = 0
            for j in xrange(6):                
                if state[j][i] == color:
                        count += 1
                        if count == length:
                            total += 1
                        elif count > length:
                            total = 0                       
                else: count = 0
        
        # check for horizontal's
        for j in xrange(6):
            count = 0
            for i in xrange(7):                
                if state[j][i] == color:
                        count += 1
                        if count == length:
                            total += 1
                        elif count > length:
                            total = 0
                else: count = 0                
        """
        


        # check for diag's
        for i in xrange(7):
            count = 0            
            for j in xrange(6):
                while (i < 7 and j < 6):                
                    if state[j][i] == color:
                        count += 1
                        if count == length: 
                            total += 1
                        elif count > length:
                            total = 0
                        i += 1
                        j += 1
            
     
        """               
        # check for negative diagonal's 
        for i in xrange(4):
            count = 0
            for j in xrange(4,6):                                
                if state[j][i] == color:
                        count += 1
                        if count == length:
                            total += 1
                        elif count > length:
                            total = 0
                else: count = 0
                i += 1
        """                    
            
        
        
        
        return total     
            
            
    def rank(self, state):
            comp = 'o'
            hum = 'x'        
            rank = 0
            
            # check for own vertical 3's and 4's            
            own_three = self.check_board(state, comp, 3)
            own_four = self.check_board(state, comp, 4)
            
            other_three = self.check_board(state, hum, 3)
            other_four = self.check_board(state, hum, 4)
            other_two = self.check_board(state, hum, 2)
            
            rank += (-100 * other_three -2500 * other_four +1000* own_three +  2500*own_four)            
            
            return rank
                        

    def minimax(self, node, depth, me):
        value = self.rank(node.value)
        if depth == 0 or node.children == [] or self.check_board(node.value, 'o', 4) >= 1 or self.check_board(node.value, 'x', 4) >= 1:
            return value
        if me:
            bestValue = -100000
            for i in xrange(7):
                val = self.minimax(node.children[i], depth - 1, False)         
                bestValue = max(bestValue, val)
            return bestValue
        else:
            bestValue = 100000
            for i in xrange(7):
                val = self.minimax(node.children[i], depth - 1, True)
                bestValue = min(bestValue, val)
            return bestValue  

    def bestestMove(self, node, depth, state):     
        bestMove = None
        bestValue = -100000        
        for i in xrange(7):
            currentval = self.minimax(node.children[i], depth, False)
            if currentval > bestValue and node.children[i].value != state:
                bestValue = currentval
                bestMove = i
        print "BEST MOVE IS",bestMove
        print "BEST VALUE IS",bestValue
        return bestMove

    def bestMove(self, difficulty, state, color):
        tree = self.build_tree(state, color, difficulty)      
        return self.bestestMove(tree, difficulty, state)