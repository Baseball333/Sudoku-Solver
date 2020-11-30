# This file contains the backtracking algorithm
# Also specifies an alternative instance of recursion

# Main Algorithm
def solve(bo):
  
    find = find_empty(bo)
    if not find:
       return True
    else:
       row, col = find
   
# Alternative instance of recursion  
def solve(bo):
  
    find = find_empty(bo)
    if not find:
       return True
    else:
       row, col = find
        
    for i in range(1, 10):
        if valid(bo, num (row, col)):
           bo[row] [col] = 1
            
           if solve(bo):  
               return True
            
           bo[row][col] = 0
          
 return False
