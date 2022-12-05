def winning_move(board, cols, rows, piece):
    if vert(board, cols, rows, piece): return True
    if horison(board, cols, rows, piece): return True
    if diag1(board, cols, rows, piece): return True
    if diag2(board, cols, rows, piece): return True


def vert(board, cols, rows, piece): #checking for horisontal 4
    for col_count in range (cols):              #cycle through all the columns
        for row_count in range(rows-3):         #cycle through the rows that can have win lines
            if (board[row_count+3][col_count]==piece and board[row_count+2][col_count]==piece and board[row_count+1][col_count]==piece and board[row_count][col_count]==piece):
                 return True                    #if 4 in a row then return winner
    return False
        

def horison(board, cols, rows, piece):
    for row_count in range(rows):
        for col_count in range(cols-3):
            if (board[row_count][col_count+3]==piece and board[row_count][col_count+2]==piece and board[row_count][col_count+1]==piece and board[row_count][col_count]==piece):
                return True
    return False


def diag1(board, cols, rows, piece):
    #checking for positive slope
    for col_count in range(cols-3):
        for row_count in range(rows-3):
            if (board[row_count][col_count]==piece and 
            board[row_count+1][col_count+1]==piece and 
            board[row_count+2][col_count+2]==piece and 
            board[row_count+3][col_count+3]==piece):
                return True
    return False



def diag2(board, cols, rows, piece):
    for col_count in range(cols-3):  #reverse count on columns
        for row_count in range (3,rows):
            if (board[row_count][col_count]==piece and 
            board[row_count-1][col_count+1]==piece and 
            board[row_count-2][col_count+2]==piece and 
            board[row_count-3][col_count+3]==piece):
                return True
    return False