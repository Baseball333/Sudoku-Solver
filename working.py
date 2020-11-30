# Sudoku Solver

# Board
board = [
   [7, 8, 0, 4, 0, 0, 1, 2, 0],
   [6, 0, 0, 0, 7, 5, 0, 0, 9],
   [0, 0, 0, 6, 0, 1, 0, 7, 8],
   [0, 0, 7, 0, 4, 0, 2, 6, 0],
   [0, 0, 1, 0, 5, 0, 9, 3, 0],
   [9, 0, 4, 0, 6, 0, 0, 0, 5],
   [0, 7, 0, 3, 0, 0, 0, 1, 2],
   [1, 2, 0, 0, 0, 7, 4, 0, 0],
   [0, 4, 9, 2, 0, 6, 0, 0, 7],
]

# Base case of recursion
def solve(bo):
   
    find = find_empty(bo)
    if not find:
       return True
    else:
       row, col = find
   
   
 def valid(bo, num, pos):
   
      # Check row
      for i in range(len(bo[0])):
          if bo[pos[0]] [i] == num and pos[1] != i:
               return False
            
      # Check column
      for i in range(len(bo)):
          if bo[i] [pos[1]] == num and(i, j) != pos:
              return False
      
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
