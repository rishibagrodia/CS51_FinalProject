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
        if depth == 0 or self.check_board(state, "X", 4) >= 1 or self.check_board(state, "O", 4) >= 1:
            return tree
        else:
            new_states = [None] * 7
            for i in xrange(7):
                new_states[i] = copy.deepcopy(state)
                for j in xrange(6):
                    if new_states[i][j][i] == ' ':
                        new_states[i][j][i] = color
                        break                            
            if color == "X":
                color = "O"
            else: color = "X"
            for i in xrange(7):
                tree.add_child(self.build_tree(new_states[i], color, depth-1))
            return tree
                    
        
    def check_board(self, state, color, length):
        total = 0 
        

        # check for UNBLOCKED vertical's        
        for i in xrange(7):
            count = 0
            for j in xrange(6):                
                if state[j][i] == color:
                        count += 1
                        if count == length and j < 5:
                            if state[j+1][i] == ' ':
                                total += 1
                        elif count > length:
                            total -= 1                       
                else: 
                    count = 0
        
        
        
        
        # check for UNBLOCKED horizontal's
        for j in xrange(6):
            count = 0
            for i in xrange(7):                
                if state[j][i] == color:
                        count += 1
                        if count == length:
                            if length == 4:                        
                                total += 1
                            elif length == 3:
                                if count == length and (i - 3) >= 0:
                                    if state[j][i-3] == ' ':
                                        total +=1
                                elif count == length and i+1 < 7:
                                    if state[j][i+1] == ' ':
                                        total += 1
                            elif length == 2:
                                if count == length and (i-3) >= 0:
                                    if state[j][i-2] == ' ' and state[j][i-3] == ' ':
                                        total += 1
                                if count == length and i+2 < 7:
                                    if state[j][i+1] == ' ' and state[j][i+2] == ' ':
                                        total += 1
                                if count == length and i+1 < 7 and i-2 >= 0:
                                    if state[j][i+1] == ' ' and state[j][i-2] == ' ':
                                        total += 1                                                      
                        elif count > length:
                            total -= 1
                else: count = 0 

        
        # check for positive diagonal's
        for i in xrange(4):
            for b in xrange(3):
                count = 0
                c = i
                for j in xrange(b, 6):
                    if c > 6: break
                    if state[j][c] == color:
                        count += 1
                        if count == length: 
                            total += 1
                        elif count > length:
                            total -= 1
                    else:
                        count = 0
                    c+=1
        
        # check for negative diagonal's
        for i in xrange(4):
            for b in xrange(5, 2, -1):
                count = 0
                c = i            
                for j in xrange(b, -1, -1):
                    if c > 6: break
                    if state[j][c] == color:
                        count += 1
                        if count == length: 
                            total += 1
                        elif count > length:
                            total -= 1
                    else:
                        count = 0
                    c+=1
        
        
        # check for split threes in positve x direction
        if length == 10:        
            for j in xrange(6):
                count = 0
                for i in xrange(5):
                    if state[j][i] == color:
                            if state[j][i+1] == color:
                                    if (state[j][i+1] == ' ' and state[j][i+2] == color): 
                                        total += 1
                    else: count = 0   
            
            # check for split threes in negative x direction
            for j in xrange(6):
                count = 0
                for i in range(6,1,-1):
                    if state[j][i] == color:
                            if state[j][i-1] == color:
                                    if (state[j][i-1] == ' ' and state[j][i-2] == color): 
                                        total += 1
                    else: count = 0   
        

        
        return total
        
        
            
            
    def rank(self, state):
            comp = 'O'
            hum = 'X'        
            rank = 0
            
            # check for own vertical 3's and 4's            
            own_three = self.check_board(state, comp, 3)
            own_four = self.check_board(state, comp, 4)
            own_splits = self.check_board(state, comp, 10)            
            own_two = self.check_board(state, comp, 2)            
            
            other_three = self.check_board(state, hum, 3)
            other_four = self.check_board(state, hum, 4)
            other_splits = self.check_board(state, hum, 10)            
            other_two = self.check_board(state, hum, 2)
            
            rank += 10000 * own_four
            rank -= 10000 * other_four
            rank += 35 * own_three
            rank -= 40 * other_three
            rank += 35 * own_splits
            rank -= 40 * other_splits
            rank += 5 * own_two
            rank -= 7 * other_two
                      
           
            
            return rank
                        

    def minimax(self, node, depth, alpha, beta, player):
        value = self.rank(node.value)
        if depth == 0 or node.children == [] or self.check_board(node.value, 'O', 4) >= 1 or self.check_board(node.value, 'X', 4) >= 1:
            return value
        if player:
            val = -10000000
            for i in xrange(7):
                val = max(val, self.minimax(node.children[i], depth - 1, alpha, beta, False))         
                alpha = max(alpha, val)
                if beta <= alpha:
                    break
            return val
        else:
            val = 10000000
            for i in xrange(7):
                val = min(val, self.minimax(node.children[i], depth - 1, alpha, beta, True))
                beta = min(beta, val)                
                if beta <= alpha:
                    break
            return val  

    def bestestMove(self, node, depth, state):     
        bestMove = None
        bestValue = -10000000        
        for i in xrange(7):
            currentval = self.minimax(node.children[i], depth, -100000000000, 100000000000, False)
            if currentval > bestValue and node.children[i].value != state:
                bestValue = currentval
                bestMove = i        
        return bestMove

    def bestMove(self, difficulty, state, color):
        tree = self.build_tree(state, color, difficulty)      
        return self.bestestMove(tree, difficulty, state)