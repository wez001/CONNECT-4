import numpy as np
import pygame
from sys import exit
from random import randint
import winner

class Con4:             #class to hold game variables including gameboard
    def __init__(self):
        self.red=(180,50,50)
        self.black=(0,0,0)
        self.yellow=(255,255,0)
        self.blue=(0,0,255)
        self.row_count=6
        self.col_count=7
        self.square_size=100
        self.width=self.col_count*self.square_size
        self.height=(self.row_count+1)*self.square_size
        self.size=(self.width,self.height)
        self.radius=int(self.square_size/2-5)
        self.turn=0
        self.gameover=False
        self.one_player=False
        self.create_board()

    def create_board(self):
        self.board=np.zeros((self.row_count,self.col_count))
        
def draw_board():       #show pygame board with counters
    for c in range(game.col_count):              #+SQURESIZE is to allow black strip at top of game window
        for r in range(game.row_count):
            
            #draw board to draw board and fill with black circles
            pygame.draw.rect(screen, game.red, (c*game.square_size, r*game.square_size+game.square_size, game.square_size,game.square_size))
            pygame.draw.circle(screen, game.black, (c*game.square_size+game.square_size/2,r*game.square_size+game.square_size+game.square_size/2), game.radius)

    for c in range(game.col_count):              #we have to take the move away from height to make the counters show from bottom to top
        for r in range(game.row_count):          
            if game.board[r][c]==1:    #player 1 slot
                pygame.draw.circle(screen, game.yellow, (c*game.square_size+game.square_size/2, game.height - (r*game.square_size+game.square_size/2)), game.radius)
            elif game.board[r][c]==2:    #player2 slot
                pygame.draw.circle(screen, game.blue, (c*game.square_size+game.square_size/2, game.height - (r*game.square_size+game.square_size/2)), game.radius)
    
    pygame.display.update() #update pygame display

def one_two():          #select one or two players
    ot=True
    while ot:
        pygame.draw.rect(screen, game.black, (0,0, game.width, game.square_size))#This blacks out the line (clears the previous text)
        text="ONE  or  TWO"                                    #variable to hold text
        pturn=myfont.render(text, 1, game.red)                           #var to hold text var, colour, font and orientation of text to be displayed
        screen.blit(pturn, (80,10))                                 #where to put text
        pygame.display.update()   
        for event in pygame.event.get():
            if event.type==pygame.MOUSEBUTTONDOWN:
                posx=event.pos[0]/100
                if posx <3.5: 
                    ot=False
                    return True                 #return true if one hit
                else:   
                    ot=False      
                    return False                #return false if 2 hit

def is_valid_location(col):     #check valid location
    return game.board[game.row_count-1][col] == 0       #returns true or false, if space available

def get_next_open_row(col):     #find next row
    for r in range(game.row_count):
        if game.board[r][col]==0: return r       #returns the first empty row of chosen column

def drop_piece( row, col, piece):     #puts 1 or 2 on the board for p1 or p2
    game.board[row][col]=piece

def show_player(pl):    #show whos turn it is
    pygame.draw.rect(screen, game.black, (0,0, game.width, game.square_size))#This blacks out the line (clears the previous text)
    text="PLAYER "+str(pl)                                    #variable to hold text
    pturn=myfont.render(text, 1, game.red)                           #var to hold text var, colour, font and orientation of text to be displayed
    screen.blit(pturn, (200,10))                                 #where to put text
    pygame.display.update()                                     #update display

def end_game(WorT):             #at end of game to show winner
    if WorT: winnershow = ("PLAYER "+ str(game.turn+1)+ " WINNER")        #variable to show who won
    else: winnershow = ("TIE")        #variable to show TIE
    print(winnershow)                       
    label = myfont.render(winnershow, 1, game.red)               #variable containing who won orientation and colour with myfont setting size and style earlier

    pygame.draw.rect(screen, game.black, (0,0, game.width, game.square_size)) #This blacks out the line (clears the previous text)
    screen.blit(label, (5,10))                              #tells pygame where to put text
    pygame.display.update()                                 #update display

    pygame.time.wait(3000)                       #pause at end of game

def comp_play():    #computers random turn
    cgo=False
    while not cgo:
        col=randint(0,6)
        if is_valid_location(col):         #return the first random number with a valid location
            cgo=True
            return col

def check_win():    #check for win or tie
    if winner.winning_move(game.board, game.col_count,game.row_count,game.turn+1):
        end_game(True)      #call endgame func to show winner
        return True
    elif winner.tie(game.board,game.col_count,game.row_count):
        end_game(False)     #call endgame function to show tie
        return True
    return False

##################################################################################################

game=Con4()         #game object initialised
pygame.init()       #pygame init
screen = pygame.display.set_mode(game.size) #screen init
myfont=pygame.font.SysFont("monospace",75)  #set font
draw_board()                                #show board
game.one_player=one_two()                   #one player - true of false

show_player(1)      #show player 1s turn at start of game

while not game.gameover:                #game start loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:   #for closing screen with x
            exit()

        if event.type==pygame.MOUSEBUTTONDOWN:      #when mouse clicked

            posx=event.pos[0]/100                   #get mouse pos make int to feed to game board
            col = int(posx)


            gofin=False                             #player 1 turn (and p2 on 2 player)
            while not gofin:
                if is_valid_location(col):       #call check location function, make sure there is a space to put the piece
                    row=get_next_open_row(col)   #get first empty row of chosen column
                    drop_piece(row, col, game.turn+1) #put piece on gameboard
                    gofin=True
                   
            draw_board()                        #show pygame board

            if check_win(): 
                game.gameover=True  #check for win
                break
                
            game.turn^=1
            show_player(game.turn+1)            #show whos turn

            if game.one_player==True:           #only use this if one player selected
                col=comp_play()                 #get computers go and put piece on board
                row=get_next_open_row(col)
                drop_piece(row,col,game.turn+1)

                draw_board()                    #show board
                if check_win(): game.gameover=True
                game.turn^=1
                show_player(game.turn+1)        #show whos turn