#test 9x9 grid
board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

def print_board(board):
    for i in range(len(board)):
        #dividing the 9x9 grid into 9, 3x3 boards
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - ")
        #retrieves the length of the row
        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                #end="" is to prevent going to the next line (\n)
                print("|", end="")

            #checking if its on the last row, then printing the next line char (\n)
            if j == 8:
                print(board[i][j])
            else:
                #end="" ensures chars are printed on the same line
                print(str(board[i][j]) + " ", end="")

#check if a number at a certain position is possible
def valid(bo, num, pos):
    #check row
    for i in range(len(bo[0])):
        #checking entire row if there is any number that is equal to the inputted number (cannot have 2 of the same numbers in a single row)
        #second condition checks if the position we are examining is the same position that we just inserted the number into
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    #check col (looping through every row)
    for i in range(len(bo)):
        #checking if the current column value is equivalent to the inputted number
        #second condition checks if the position we are examining is the same position that we just inserted the number into
        if bo[i][pos[1]] == num and pos[0] != i:
            return False
    
    #checking 3x3 board so that there are no duplicate numbers in that specific board
    #integer division (returns to the nearest whole number) for first column and row
    #Classification for board system using integer division:
    #     |  0,0   |  0,1  |  0,2  |
    #     --------------------------
    #     |  1,0   |  1,1  |  1,2  |
    #     --------------------------
    #     |  2,0   |  2,1  |  2,2  |
    box_x = pos[1] // 3 
    box_y = pos[0] // 3

    #loop through all 9 elements inside each board to check for duplicates
    #multiply board number by 3 to get the correst index
    for i in range(box_y * 3 , box_y * 3 + 3):
        for j in range(box_x * 3 , box_x * 3 + 3):
            if bo[i][j] == num and (i, j) != pos:
                return False
    
    return True
        
#backtracking algo using recursion that will use these functions
def solve(bo):
    #base case (if board is full)
    find = find_empty(bo)
    #if the function cannot find an empty slot, return True since that means the board is completely filled (base case)
    if not find:
        return True
    else: 
        row, col =  find
    #loop through possible values (1-9) and try them inside the solution
    for i in range (1, 10):
        if valid(bo, i, (row, col)):
            #insert number to that position
            bo[row][col] = i

            #checks if base case is satisfied (tries until solution is more or after loop ends)
            if solve(bo):
                return True
            #resets that position's value to 0, and "backtracks" (restarts function again)
            bo[row][col] = 0
    #signals that solution is no met
    return False



#find an empty square on the grid
def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            #a value of 0 represents an empty slot
            if bo[i][j] == 0:
                return (i, j)  # row, col
    #if there are no blank squares, triggers base case
    return None


#priting board before test vs after solve
print_board(board)
solve(board)
print("_________________________")
print_board(board)