# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 16:29:12 2024

@author: Mohamed Abu Samaha
"""

from random import randrange 

def display_board(board):
    print("+-------+-------+-------+")
    for row in range(3):
        print("|       |       |       |")
        for col in range(3):
            print("|   ",board[row][col],"   ",sep='',end='')
        print("|")
        print("|       |       |       |")
        print("+-------+-------+-------+")

# The function accepts the board's current status, asks the user about their move,
def human_Turn(board):
     
    valid=False
    while not valid:
        move=input("Enter your next move: ")
        valid= int(move) >= 1 and int(move) <= 9
        if not valid: # the move is out of range
            print("Please, Enter anthor vaild move from 1 to 9")
            continue
        move= int(move)-1
        row=move // 3 # get number of the row
        col=move % 3  # get number of the column
        if(board[row][col] in ('X','O')): # check if the slot is occuppied
            print("Already Occupied this slot enter an anthor move")
            valid=False
            continue
        board[row][col]='O'


def which_field_is_empty(board):
    # The function browses the board and builds a list of all the free squares;
    free_list=[]
    for row in range(3):
        for col in range(3):
            if board[row][col] not in ('X','O'):
                free_list.append((row,col))
    
    return free_list
    

# The function analyzes the board's status in order to check which won the game
def who_is_win(board, sign):   
    cross1=0
    cross2=0
    
    for i in range(3):
        if (board[i][0] == sign) and (board[i][1] == sign) and (board[i][2] == sign):
            return True
        elif (board[0][i] == sign) and (board[1][i] == sign) and (board[2][i] == sign):
            return True
        elif (board[i][i] == sign):
            cross1 += 1
            
        if (board[i][2-i] == sign):
            cross2 +=1

    if cross1==3 or cross2==3 :
        return True
    else:
        return None
# The function draws the computer's move and updates the board.
def machine_turn(board):
    free=which_field_is_empty(board)
    cnt=len(free)
    th=randrange(cnt)
    row,col=free[th]
    board[row][col]='X'
        
        
 
while(True):

    board=[[3*j+i+1 for i in range(3)] for j in range(3)]
    board[1][1]='X'
    human_turn=True
    free=which_field_is_empty(board)
    while len(free):
        display_board(board)
        if human_turn:
            human_Turn(board)
            ret_val=who_is_win(board, 'O')
            if (True==ret_val):
                display_board(board)
                print("You win !!")
                break
            human_turn= False
        else:
           machine_turn(board)
           ret_val=who_is_win(board, 'X')
           if (True==ret_val):
               display_board(board)
               print("You loss !!") 
               break
           human_turn= True
           
        free=which_field_is_empty(board)
        
    if len(free):
        break
    else:
        continue

