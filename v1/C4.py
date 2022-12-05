import numpy as np
import extra        #this is used for checing for win


ROW_COUNT = 6       #for setting up the game board.
COL_COUNT = 7



def create_board():                         #create the gameboard using numpy, can be done with 2d array but numpy easier
    board = np.zeros((ROW_COUNT,COL_COUNT))
    return board

def print_board(board):                     #shows the game board, flipped like connect 4 board
    print(np.flip(board,0))


def drop_piece(board, row, col, piece):     #puts 1 or 2 on the board for p1 or p2
    board[row][col]=piece




def is_valid_location(board,col):
    return board[ROW_COUNT-1][col] == 0       #returns true or false, if space available



def get_next_open_row(board, col):
    for r in range(ROW_COUNT):
        if board[r][col]==0: return r       #returns the first empty row of chosen column






board=create_board()
game_over=False
print_board(board)                          #show board before first move
turn = 0


while not game_over:
    #ask p1 inp
    if turn==0:
        col = int(input ("Player 1 make your selection (0-6): "))


    else: #ask p2 input
        col = int(input ("Player 2 make your selection (0-6): "))

    if is_valid_location(board, col):       #call check location function, make sure there is a space to put the piece
        row=get_next_open_row(board, col)   #get first empty row of chosen column
        drop_piece(board, row, col, turn+1) #put piece on gameboard



    print_board(board)                      #show the gameboard with moves
    
    if extra.winning_move(board, COL_COUNT, ROW_COUNT, turn+1):     #check for a winner
        print("WINNER")
        game_over=True

    turn += 1       #change player turn
    turn = turn % 2

   
