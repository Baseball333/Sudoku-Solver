# This file contains the backtracking algorithm
# Also specifies an alternative instance of recursion

# Main Algorithm
def solve(bo):
  
    find = find_empty(bo)
    if not find:
       return True
    else:
       row, col = find
   
  
  
