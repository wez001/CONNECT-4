import numpy as np
import pygame
from sys import exit
import winner        #this is other code used for checking for win

RED = (180,50,50)
BLACK =(0,0,0)
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

def draw_board(board):                      #The first line here creates the rectangeles, the secon the circles
    for c in range(COL_COUNT):
        for r in range(ROW_COUNT):
            pygame.draw.rect(screen, RED, (c*SQUARE_SIZE, r*SQUARE_SIZE+SQUARE_SIZE, SQUARE_SIZE,SQUARE_SIZE))
            pygame.draw.circle(screen, BLACK, (c*SQUARE_SIZE+SQUARE_SIZE/2,r*SQUARE_SIZE+SQUARE_SIZE+SQUARE_SIZE/2), RADIUS)



board=create_board()
game_over=False
print_board(board)                          #show board before first move
turn = 0

pygame.init()       #initialise pygame

SQUARE_SIZE=100     #size for each cell

width=COL_COUNT*SQUARE_SIZE     #sizes for game grid
height=(ROW_COUNT+1)*SQUARE_SIZE    #plus one to have somewhere to drop piece
size=(width,height)

RADIUS = int(SQUARE_SIZE/2-5) #circles on board

screen = pygame.display.set_mode(size)
draw_board(board)
pygame.display.update()



while not game_over:        #gameplay
    
    for event in pygame.event.get():    #for closing screen x
        if event.type == pygame.QUIT:
            exit()

        if event.type==pygame.MOUSEBUTTONDOWN:
            continue


            # #ask p1 inp
            # if turn==0:
            #     col = int(input ("Player 1 make your selection (0-6): "))

            # else: #ask p2 input
            #     col = int(input ("Player 2 make your selection (0-6): "))

            # if is_valid_location(board, col):       #call check location function, make sure there is a space to put the piece
            #     row=get_next_open_row(board, col)   #get first empty row of chosen column
            #     drop_piece(board, row, col, turn+1) #put piece on gameboard



            print_board(board)                      #show the gameboard with moves
            
            if winner.winning_move(board, COL_COUNT, ROW_COUNT, turn+1):     #check for a winner
                print("PLAYER "+ str(turn+1)+ " IS THE WINNER!")
                game_over=True

            turn += 1       #change player turn
            turn = turn % 2

   
