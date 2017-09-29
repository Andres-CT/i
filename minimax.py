# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 15:14:28 2017

@author: maupe
"""
import AI
import random
import copy

def intelligentFunction1(turn, board):
    i=0
    if (turn==1):
        for x in range(height-1,-1,-1):
            for y in range(0,width):
                if(board[x][y]!=turn and board[x][y]!=0 and board[x+1][y]==0):
                    i=y
                    for r in range(0,height-2):
                        for c in range(0,width-2):
                            if(board[r][c]==turn
                            and board[r][c+1]==turn
                            and board[r][c+2]==turn
                            and board[r+1][c+1]==0):
                                i=c+1
    else:
        start=1
        for u in range(0,width):
            if(board[0][u]!=0):
                start=0
                u=width
        if(start==1):
            i=random.randint(8,9)
            if(i==8):
                i=0
            else:
                i=6
        else:
            #i=random.randint(0,6)
            #while (board[i][5]!=0):
                #i=random.randint(0,6)
            for x in range(0,height-1):
                for y in range(0,width):
                    if(board[x][y]!=turn and board[x][y]!=0 and board[x+1][y]==0):
                        i=y
                        for r in range(0,height-2):
                            for c in range(0,width-2):
                                if(board[r][c]==turn
                                and board[r][c+1]==turn
                                and board[r][c+2]==turn
                                and board[r+1][c+1]==0):
                                    i=c+1
            if(board[5][i]!=0):
               i=random.randint(0,6)
               while (board[5][i]!=0):
                   i=random.randint(0,6)
    return i

def intelligentFunction2(turn, board):
    i=random.randint(0,6)
    while (board[5][i]!=0):
        i=random.randint(0,6)
    return i


def placeChange(List,n,turn):
    change=0
    IntraBoardx=copy.deepcopy(List)
    for up in range(0,6):
        if(List[up][n]==0):
            IntraBoardx[up][n]=turn
            change=1
            return IntraBoardx
            break
        if(up==5 and change==0):
            return 0

class ConectaT:
    def __init__(self, intraBoard, depth, turn, columnaPtirar):
        self.IntraBoard = intraBoard
        self.depth = depth
        self.Turn = turn
        self.Pointers=[]
        self.CPT=columnaPtirar
        if(depth==0):
            turn=1+(turn%2)
        """print ("-----------------------------")
        for x in range(6-1,-1,-1):
            for y in range(0,7):
                print ("|",self.IntraBoard[x][y], end=" "),
            print ("|\n----+---+---+---+---+---+----")
        print ("\n")"""
        if(depth<=2):#-1 of desired level
            for k in range(0,7):
                self.Pointers.append(ConectaT(placeChange(intraBoard, k, 1+(turn%2)),depth+1,1+(turn%2),k))
Q=ConectaT(board,0,2,random.randint(0,6))
#print (Q.Pointers[6].Pointers[6].Pointers[6].IntraBoard)

def Evaluate(BOARD,playerN):
    Score=3
    if(BOARD[0][3]==1 and BOARD[1][3]==2):
        Score=165
    if(checkAnyT(playerN)):
        Score=10000
    if(checkAnyT(1+(playerN%2))):
        Score=-10000
    if(Score!=10000 and Score!=-10000):
        for x in range(0,height-1):
            for y in range(0,width-2):
                if(board[x][y]==playerN and board[x][y+2]==playerN and board[x][y+1]!=0
                   and board[x+1][y+1]==playerN and
                   ((board[x+1][y]!=0 and board[x+1][y]==0)
                   or (board[x+1][y+2]!=0 and board[x+1][y+2]==0))):
                    Score+=100
    return Score
def MejorTiro(object):
    MejorScore=0
    Candidato=0
    ElMejorTiro=0
    for ii in range(0,7):
        for jj in range(0,7):
            for hh in range(0,7):
                Candidato=(Evaluate(object.Pointers[ii].Pointers[jj].Pointers[hh].IntraBoard,object.Pointers[ii].Pointers[jj].Pointers[hh].Turn))
                if(Candidato>MejorScore):
                    ElMejorTiro=(object.Pointers[ii].Pointers[jj].Pointers[hh].CPT)
                    MejorScore=Candidato
    return ElMejorTiro

def checkAnySquare(BOARD, column, row, playerN):
   if(board[row][column+1] == playerN and board[row+1][column] == playerN and board[row+1][column+1] == playerN):
        return True

   return False

def checkL1(BOARD,row,col,turn):
    global  width, height
    if (col + 1 == width or row == 0 or row + 1 == width): return False
    if ((BOARD[row][col] and BOARD[row+1][col] and BOARD[row+1][col-1])==turn and BOARD[row][col-1]!=0):
        return True
    return False


def checkL2(BOARD,row,col,turn):
    global width, height
    if (col + 1 == width or row == 0 or row + 1 == width): return False
    if ((BOARD[row][col] and BOARD[row+1][col] and BOARD[row+1][col+1])==turn and BOARD[row][col+1]!=0):
        return True
    return False

def checkL3(BOARD, row,col,turn):
    global  width, height
    if (col + 1 == width or row == 0 or row + 1 == width): return False
    if ((BOARD[row][col] and BOARD[row][col+1] and BOARD[row+1][col+1])==turn and BOARD[row+1][col]!=0):
        return True
    return False

def checkL4(BOARD, row,col,turn):
    global width, height
    if (col + 1 == width or row == 0 or row + 1 == width): return False
    if ((BOARD[row][col] and BOARD[row][col-1] and BOARD[row+1][col-1])==turn and BOARD[row+1][col]!=0):
        return True
    return False

def IntraCheckAnyT(BOARD, player_number):
    for r in range(0, 6):
        for c in range(0, 7):
            if (BOARD[r][c] == player_number):
                if (IntraCheckWinBelow(r, c, player_number)
                    or IntraCheckWinAbove(r, c, player_number)
                    or IntraCheckLeft(r, c, player_number)
                    or IntraCheckRight(r, c, player_number)
                    or IntraCheckWinBottomRight(r, c, player_number)
                    or IntraCheckWinBottomLeft(r, c, player_number)
                    or IntraCheckWinTopLeft(r, c, player_number)
                    or IntraCheckWinTopRight(r, c, player_number)):
                    return True
    return False

def IntraCheckWinBelow(BOARD,row, col, player_number):
    if (col + 1 == 7 or row == 0 or row + 1 == 7): return False
    if (BOARD[row - 1][col + 1] == player_number and BOARD[row][col + 1] == player_number and BOARD[row + 1][
            col + 1] == player_number): return True
    return False

def IntraCheckWinAbove(BOARD,row, col, player_number):
    if (col == 0 or row == 0 or row + 1 == 6): return False
    if (BOARD[row - 1][col - 1] == player_number and BOARD[row][col - 1] == player_number and BOARD[row + 1][
            col - 1] == player_number): return True
    return False

def IntraCheckLeft(BOARD,row, col, player_number):
    if (row + 1 >= 6 or col + 1 >= 7 or col - 1 < 0): return False
    if (BOARD[row + 1][col - 1] == BOARD[row + 1][col] == BOARD[row + 1][col + 1] == player_number): return True
    return False

def IntraCheckRight(BOARD,row, col, player_number):
    if (row - 1 < 0 or col + 1 >= 7 or col - 1 < 0): return False
    if (BOARD[row - 1][col - 1] == BOARD[row - 1][col] == BOARD[row - 1][col + 1] == player_number): return True
    return False

def IntraCheckWinBottomRight(BOARD,row, col, player_number):
    if (row - 2 < 0 or col + 2 >= 7): return False
    if (BOARD[row - 2][col] == player_number and BOARD[row - 1][col + 1] == player_number and BOARD[row][
            col + 2] == player_number): return True
    return False

def IntraCheckWinBottomLeft(BOARD,row, col, player_number):
    if (row + 2 >= 6 or col - 2 < 0): return False
    if (BOARD[row + 2][col] == player_number and BOARD[row + 1][col - 1] == player_number and BOARD[row][
            col - 2] == player_number): return True
    return False

def IntraCheckWinTopLeft(BOARD,row, col, player_number):
    if (row + 2 >= 6 or col - 2 < 0): return False
    if (BOARD[row + 2][col] == player_number and BOARD[row + 1][col - 1] == player_number and BOARD[row][
            col - 2] == player_number): return True
    return False

def IntraCheckWinTopRight(BOARD,row, col, player_number):
    if (row - 2 < 0 or col - 2 < 0): return False
    if (BOARD[row - 2][col] == player_number and BOARD[row - 1][col - 1] == player_number and BOARD[row][
            col - 2] == player_number): return True
    return False