def solve_puzzle(board, pos = 0, visited = None): # Make sure to add input parameters here
    """Returns True(False) if a given board is (is not) solveable"""

    if pos == len(board) - 1:
         return True                           #base case
    
    if visited is None:
         visited = set()
    
    if pos not in visited:      
        visited.add(pos)    
    else:
         return False
   
    
    #clockwise
    cw = (pos + board[pos]) % len(board)
   
    

    #counterclockwise
    ccw = (pos - board[pos]) % len(board)
   

    
    return solve_puzzle(board, cw, visited) or solve_puzzle(board, ccw, visited)
   
   
   
    # 1) Base case: have you found a valid solution?

    # 2) Find all valid next-steps

    # 3) Recursively explore next-steps, returning True if any valid solution is found
