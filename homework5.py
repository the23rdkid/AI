############################################################
# CIS 521: Sudoku Homework 
############################################################

student_name = "Naomi Maranga"
############################################################
# Imports
############################################################

# Include your imports here, if any are used.
import math 
import copy 
import random 
import itertools

############################################################
# Section 1: Sudoku Solver
############################################################

def sudoku_cells():
  cells = []
  for i, j in itertools.product(range(9), range(9)):
    cells.append((i, j))
  return cells
  
def sudoku_arcs():
  set_of_arcs = set()
  for i, j, k in itertools.product(range(9), range(9), range(9)):
    if k != j: 
      first_arc = ((i, j), (i, k))
      second_arc = ((j, i), (k, i))
      set_of_arcs.add(first_arc)
      set_of_arcs.add(second_arc)
  #OMIIIIII
  for i, j in itertools.product(range(9), range(9)):
    for ki, kj in itertools.product(range(3), range(3)):
      x = ki + (i // 3) * 3
      y = kj + (j // 3) * 3
      if i != x or j != y: 
        third_arc = ((i, j),(x, y))
        set_of_arcs.add(third_arc)
  return set_of_arcs


def read_board(path):
  with open(path) as infile:
    board = {}
    for line in infile:
      for char in enumerate(line.strip(), start = 1):
        if char == '*':
          board.append('0')
        elif char > 0:
          board.append([int(x) for x in line.strip('\n')])
  return board

class Sudoku(object):

    CELLS = sudoku_cells()
    ARCS = sudoku_arcs()

    def __init__(self, board):
      self.board = board 
      self.map_board = dict()
      self.check = 0
      for i, j in itertools.product(range(9), range(9)):
        symbol = board[i][j]
        tuple_range = tuple(range(1, 10))
        if symbol == 0: 
          self.map_board.update({(i,j):tuple_range})
        if symbol != 0:
          sym_set = set()
          sym_set.add(int(symbol))
          self.map_board.update({(i, j): sym_set})
          self.check += 1
        

    def get_values(self, cell):
      self.cell = cell
      return self.map_board(cell)
       
    def remove_inconsistent_values(self, cell1, cell2):
        pass

    def infer_ac3(self):
        pass

    def infer_improved(self):
        pass

    def infer_with_guessing(self):
        pass

        
print(sudoku_cells())
print(((0, 0), (0, 8)) in sudoku_arcs())
print(((0, 0), (8, 0)) in sudoku_arcs())
print(((0, 8), (0, 0)) in sudoku_arcs())
print(((0, 0), (2, 1)) in sudoku_arcs())
print(((2, 2), (0, 0)) in sudoku_arcs())
print(((2, 3), (0, 0)) in sudoku_arcs())
b = read_board("sudoku/medium1.txt")
print(Sudoku(b).get_values((0, 0)))
