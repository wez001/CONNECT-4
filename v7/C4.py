import numpy as np
import pygame
from sys import exit
import winner        #this is other code used for checking for win

RED = (180,50,50)
BLACK =(0,0,0)
YELLOW=(255,255,0)
BLUE=(0,0,255)
ROW_COUNT = 6       #for setting up the game board.
COL_COUNT = 7

turn = 0
pygame.init()       #initialise pygame

SQUARE_SIZE=100     #size for each cell
width=COL_COUNT*SQUARE_SIZE     #sizes for game grid
height=(ROW_COUNT+1)*SQUARE_SIZE    #plus one to have somewhere to drop piece
size=(width,height)

RADIUS = int(SQUARE_SIZE/2-5) #circles on board
myfont = pygame.font.SysFont("monospace",75) #this is for font size for player notification and win notificaton
game_over=False

def create_board():                         #create the gameboard using numpy, can be done with 2d array but numpy easier
    board = np.zeros((ROW_COUNT,COL_COUNT))
    return board

# def print_board(board):                     #shows the game board, flipped like connect 4 board
#     print(np.flip(board,0))                    #dont need this now

def drop_piece(board, row, col, piece):     #puts 1 or 2 on the board for p1 or p2
    board[row][col]=piece

def is_valid_location(board,col):
    return board[ROW_COUNT-1][col] == 0       #returns true or false, if space available

def get_next_open_row(board, col):
    for r in range(ROW_COUNT):
        if board[r][col]==0: return r       #returns the first empty row of chosen column

def draw_board(board):                      #The first line here creates the rectangeles, the secon the circles
    for c in range(COL_COUNT):              #+SQURESIZE is to allow black strip at top of game window
        for r in range(ROW_COUNT):
            
            #draw board to draw board and fill with black circles
            pygame.draw.rect(screen, RED, (c*SQUARE_SIZE, r*SQUARE_SIZE+SQUARE_SIZE, SQUARE_SIZE,SQUARE_SIZE))
            pygame.draw.circle(screen, BLACK, (c*SQUARE_SIZE+SQUARE_SIZE/2,r*SQUARE_SIZE+SQUARE_SIZE+SQUARE_SIZE/2), RADIUS)

    for c in range(COL_COUNT):              #we have to take the move away from height to make the counters show from bottom to top
        for r in range(ROW_COUNT):          
            if board[r][c]==1:    #player 1 slot
                pygame.draw.circle(screen, YELLOW, (c*SQUARE_SIZE+SQUARE_SIZE/2, height - (r*SQUARE_SIZE+SQUARE_SIZE/2)), RADIUS)
            elif board[r][c]==2:    #player2 slot
                pygame.draw.circle(screen, BLUE, (c*SQUARE_SIZE+SQUARE_SIZE/2, height- (r*SQUARE_SIZE+SQUARE_SIZE/2)), RADIUS)
    
    pygame.display.update() #update pygame display

def show_player(turn):
    pygame.draw.rect(screen, BLACK, (0,0, width, SQUARE_SIZE))#This blacks out the line (clears the previous text)
    text="PLAYER "+str(turn)                                    #variable to hold text
    pturn=myfont.render(text, 1, RED)                           #var to hold text var, colour, font and orientation of text to be displayed
    screen.blit(pturn, (200,10))                                 #where to put text
    pygame.display.update()                                     #update display

def end_game(WorT):             #at end of game to show winner
    if WorT: winnershow = ("PLAYER "+ str(turn+1)+ " WINNER")        #variable to show who won
    else: winnershow = ("TIE")        #variable to show TIE
    print(winnershow)                       
    label = myfont.render(winnershow, 1, RED)               #variable containing who won orientation and colour with myfont setting size and style earlier

    pygame.draw.rect(screen, BLACK, (0,0, width, SQUARE_SIZE)) #This blacks out the line (clears the previous text)
    screen.blit(label, (5,10))                              #tells pygame where to put text
    pygame.display.update()                                 #update display

    pygame.time.wait(3000)                       #pause at end of game


board=create_board()

screen = pygame.display.set_mode(size)
draw_board(board)
pygame.display.update()
show_player(1)

while not game_over:        #gameplay
    for event in pygame.event.get():    #for closing screen with x
        if event.type == pygame.QUIT:
            exit()

        if event.type==pygame.MOUSEBUTTONDOWN:      #when mouse clicked

                                                    #event.pos is where mouse was clicked
            posx=event.pos[0]/100                   #get mouse pos make int to feed to game board
            col = int(posx)
            
            if is_valid_location(board, col):       #call check location function, make sure there is a space to put the piece
                row=get_next_open_row(board, col)   #get first empty row of chosen column
                drop_piece(board, row, col, turn+1) #put piece on gameboard
            else: turn+=1

            draw_board(board)                       #show pygame board
            if turn==0:show_player(2)
            else:show_player(1)
            
            if winner.winning_move(board, COL_COUNT, ROW_COUNT, turn+1):     #check for a winner
                end_game(True)              #call the end_game func to show winner
                game_over=True          #this will end the game loop
            elif winner.tie(board, COL_COUNT, ROW_COUNT):   #check for TIE
                end_game(False)
                game_over=True

            turn += 1       #change player turn
            turn = turn % 2

   
