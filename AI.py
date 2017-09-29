import random
import copy

width, height = 7, 6

# board = [[0 for x in range(width)]for y in range (height)]
board = [[0 for y in range(width)] for x in range(height)]


# Matrix positions
# [5][0] [5][1] [5][2] [5][3] [5][4] [5][5] [5][6]
# [4][0] [4][1] [4][2] [4][3] [4][4] [4][5] [4][6]
# [3][0] [3][1] [3][2] [3][3] [3][4] [3][5] [3][6]
# [2][0] [2][1] [2][2] [2][3] [2][4] [2][5] [2][6]
# [1][0] [1][1] [1][2] [1][3] [1][4] [1][5] [1][6]
# [0][0] [0][1] [0][2] [0][3] [0][4] [0][5] [0][6]

# This is the function used to make a move.
# The function recieves the column (that is going to be given by the intelligent algorithm), and the player number that is making the move.
# If the move can't be made, the function returns -1, else: it returns the col in which it was placed.
def place(column, player_number):
    global board, width, height
    if (column >= width or column < 0):
        return -1
    partial_height = height - 1
    while (partial_height >= 0 and board[partial_height][column] == 0):
        partial_height -= 1
    if (partial_height + 1 < height):
        board[partial_height + 1][column] = player_number
        return partial_height + 1
    return -1


# Function used to check whether game has finished or not
# Return values:
# -1 -> game tie
# 0  -> game continues
# 1  -> game won by player_number

# Possible t's:

#   010     111     10      01      100     001     101     101
#   111     010     11      11      010     010     010     010
#                   10      01      101     101     001     100

def gameFinished(player_number):
    global board, width, height
    available_moves = False
    for pos in range(width):
        if (board[height - 1][pos] == 0):
            available_moves = True
            break
    if (checkAnyT(player_number)):
        return 1
    if (not available_moves):
        return -1
    return 0

# Function for printing the game board
def printGame():
    global board, width, height
    print ("-----------------------------")
    for row in range(height - 1, -1, -1):
        for col in range(0, width):
            print ("|",board[row][col], end=" ")
        print ("|\n----+---+---+---+---+---+----")
    print ("\n")

def checkAnyT(player_number):
    global board, width, height
    for r in range(0, 6):
        for c in range(0, 7):
            if (board[r][c] == player_number):
                if (checkWinBelow(r, c, player_number)
                    or checkWinAbove(r, c, player_number)
                    or checkLeft(r, c, player_number)
                    or checkRight(r, c, player_number)
                    or checkWinBottomRight(r, c, player_number)
                    or checkWinBottomLeft(r, c, player_number)
                    or checkWinTopLeft(r, c, player_number)
                    or checkWinTopRight(r, c, player_number)):
                    return True
    return False

def checkWinBelow(row, col, player_number):
    global board, width, height
    if (col + 1 == width or row == 0 or row + 1 == width): return False
    if (board[row - 1][col + 1] == player_number and board[row][col + 1] == player_number and board[row + 1][
            col + 1] == player_number): return True
    return False

def checkWinAbove(row, col, player_number):
    global board, width, height
    if (col == 0 or row == 0 or row + 1 == height): return False
    if (board[row - 1][col - 1] == player_number and board[row][col - 1] == player_number and board[row + 1][
            col - 1] == player_number): return True
    return False

def checkLeft(row, col, player_number):
    global board, width, height
    if (row + 1 >= height or col + 1 >= width or col - 1 < 0): return False
    if (board[row + 1][col - 1] == board[row + 1][col] == board[row + 1][col + 1] == player_number): return True
    return False

def checkRight(row, col, player_number):
    global board, width, height
    if (row - 1 < 0 or col + 1 >= width or col - 1 < 0): return False
    if (board[row - 1][col - 1] == board[row - 1][col] == board[row - 1][col + 1] == player_number): return True
    return False

def checkWinBottomRight(row, col, player_number):
    global board, width, height
    if (row - 2 < 0 or col + 2 >= width): return False
    if (board[row - 2][col] == player_number and board[row - 1][col + 1] == player_number and board[row][
            col + 2] == player_number): return True
    return False

def checkWinBottomLeft(row, col, player_number):
    global board, width, height
    if (row + 2 >= height or col - 2 < 0): return False
    if (board[row + 2][col] == player_number and board[row + 1][col - 1] == player_number and board[row][
            col - 2] == player_number): return True
    return False

def checkWinTopLeft(row, col, player_number):
    global board, width, height
    if (row + 2 >= height or col - 2 < 0): return False
    if (board[row + 2][col] == player_number and board[row + 1][col - 1] == player_number and board[row][
            col - 2] == player_number): return True
    return False

def checkWinTopRight(row, col, player_number):
    global board, width, height
    if (row - 2 < 0 or col - 2 < 0): return False
    if (board[row - 2][col] == player_number and board[row - 1][col - 1] == player_number and board[row][
            col - 2] == player_number): return True
    return False

#ARBOLES#############

def checkAnySquare(BOARD, column, row, playerN):
   if(BOARD[row][column+1] == playerN and BOARD[row+1][column] == playerN and BOARD[row+1][column+1] == playerN):
       if(BOARD[row+2][column]==0 or BOARD[row+2][column+1]==0):
           return True
   return False

def checkAnyCone(BOARD, column, row, playerN):
    if(column <= 5):
      if(BOARD[row+1][column+1]== playerN and BOARD[row][column+2]== playerN):
          return True
      return False
    return False

def checkL1(BOARD,row,col,turn):
    global  width, height
    if (col + 1 == width or row == 0 or row + 1 == width): return False
    if ((BOARD[row][col] and BOARD[row+1][col] and BOARD[row+1][col-1])==turn and BOARD[row][col-1]!=0 and BOARD[row][col+1]!=0 and BOARD[row+1][col+1]==0):
        return True
    return False


def checkL2(BOARD,row,col,turn):
    global width, height
    if (col + 1 == width or row == 0 or row + 1 == width): return False
    if ((BOARD[row][col] and BOARD[row+1][col] and BOARD[row+1][col+1])==turn and BOARD[row][col+1]!=0 and BOARD[row][col-1]!=0 and BOARD[row+1][col-1]==0):
        return True
    return False

def checkL3(BOARD, row,col,turn):
    global  width, height
    if (col + 1 == width or row == 0 or row + 1 == width): return False
    if ((BOARD[row][col] and BOARD[row][col+1] and BOARD[row+1][col+1])==turn and BOARD[row+1][col]!=0 and BOARD[row][col+2]==0):
        return True
    return False

def checkL4(BOARD, row,col,turn):
    global width, height
    if (col + 1 == width or row == 0 or row + 1 == width): return False
    if ((BOARD[row][col] and BOARD[row][col-1] and BOARD[row+1][col-1])==turn and BOARD[row+1][col]!=0and BOARD[row][col-2]==0):
        return True
    return False

def checkHorizontal(BOARD, row, col, turn):
    global width, height
    if (col + 1 == width or row == 0 or row + 1 == width): return False
    if ((BOARD[row][col] and BOARD[row][col+1] and BOARD[row][col+2])==turn and BOARD[row+1][col+1]!=0):
        return True
    return False

def checkVertical(BOARD, row, col, turn):
    global width, height
    if (col + 1 == width or row == 0 or row + 1 == width): return False
    if (((BOARD[row][col] and BOARD[row+1][col] and BOARD[row+2][col])==turn) and ((BOARD[row][col-1]!=0) or (BOARD[row][col+1]!=0)) and ((BOARD[row+1][col-1]==0)or (BOARD[row+1][col+1]==0))):
        return True
    return False

def checkDiagonales(BOARD, row, col, turn):
    global width, height
    if (col + 1 == width or row == 0 or row + 1 == width): return False
    if ((BOARD[row][col] and BOARD[row+1][col+1] and BOARD[row+2][col+2])==turn) and (BOARD[row][col+1]!=0) and (BOARD[row][col+2]!=0)and (BOARD[row+1][col]!=0) and (BOARD[row+1][col+2]!=0):
        return True
    if ((BOARD[row][col] and BOARD[row+1][col-1] and BOARD[row+2][col-2])==turn) and (BOARD[row][col-1]!=0) and (BOARD[row][col-2]!=0)and (BOARD[row+1][col]!=0) and (BOARD[row+1][col-2]!=0):
        return True
    return False

def checkZetas(BOARD, row, col, turn):
    global width, height
    if (col + 1 == width or row == 0 or row + 1 == width): return False
    if (((BOARD[row][col] and BOARD[row][col+1] and BOARD[row+1][col+1] and BOARD[row+1][col+2]) ==turn) and (BOARD[row][col+2]!=0) and ((BOARD[row+1][col]==0) or (BOARD[row+2][col+1]==0))):
        return True
    if (((BOARD[row][col] and BOARD[row][col-1] and BOARD[row+1][col-1] and BOARD[row+1][col-2]) ==turn) and (BOARD[row][col-2]!=0) and ((BOARD[row+1][col]==0) or (BOARD[row+2][col-1]==0))):
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
        i=random.randint(0,6)
        Q=ConectaT(board,0,turn,random.randint(0,6))
        i=Q.CPT
        """
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
                   i=random.randint(0,6)"""
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
        self.CPT=MejorTiro(self)

def Evaluate(BOARD,playerN):
    Score=3
    if(IntraCheckAnyT(playerN)):
        Score=10000
    if(IntraCheckAnyT(1+(playerN%2))):
        Score=-10000
    if(Score!=10000 and Score!=-10000):
        for r in range(0,height-2):
            for c in range(0,width-1):
                if(checkAnySquare(BOARD,c,r,playerN)):
                    Score+=100
    return Score

def MejorTiro(object):
    MejorScore=0
    Candidato=0
    ElMejorTiro=0
    NoTirar=[]
    Fail=0
    for ii in range(0,7):
        if(Evaluate(object.Pointers[ii].IntraBoard,object.Pointers[ii].Turn)==10000):
            ElMejorTiro=object.Pointers[ii].CPT
            MejorScore=10000
            break
    for ii in range(0,7):
        for jj in range(0,7):
            if(Evaluate(object.Pointers[ii].Pointers[jj].IntraBoard,object.Pointers[ii].Pointers[jj].Turn)==10000):
                NoTirar.append(object.Pointers[ii].Pointers[jj].CPT)
    if(MejorScore!=10000):
        for ii in range(0,7):
            for NOUSES in range(0,len(NoTirar)):
                if(ii==NoTirar[NOUSES]):
                    Fail=1
                    break
                if(Fail==0):
                    for jj in range(0,7):
                        for hh in range(0,7):
                            Candidato=(Evaluate(object.Pointers[ii].Pointers[jj].Pointers[hh].IntraBoard,object.Pointers[ii].Pointers[jj].Pointers[hh].Turn))
                            if(Candidato>MejorScore):
                                ElMejorTiro=(object.Pointers[ii].Pointers[jj].Pointers[hh].CPT)
                                MejorScore=Candidato
    return ElMejorTiro


#ARBOLES#############

def main():
    global board
    Kee="z"
    while(Kee!="a" and Kee!="b"):
        print("¿Quién va a comenzar el juego?\n\ta)Un humano\n\tb)El programa")
        Kee=input()
        if(Kee=="a" or Kee=="b"):
            if(Kee=="a"):
                turn=2
            else:
                turn=1
        else:
            print("Caracter inválido")
    loser = 0
    while (gameFinished(turn)==0):
        printGame()
        turn=1+(turn%2)
        if (turn == 1):
            column = int(input("Columna para tirar: "))
        if (turn == 2):
            column = intelligentFunction1(turn, board)
        if (place(column, turn) == -1):
            loser = turn
            break

    # Game is a tie
    if (gameFinished(turn) == -1): print("The game is a tie!")
    elif not (loser == 0): print ("The loser is ", turn)
    else:
        printGame()
        print ("The winner is ", turn)



if __name__ == '__main__':
    main()
