import random

width, height = 7, 6

#board = [[0 for x in range(width)]for y in range (height)]
board = [[0 for y in range(height)]for x in range (width)]


#Matrix positions
#[0][0] [1][0] [2][0] [3][0] [4][0] [5][0] [6][0]
#[0][1] [1][1] [2][1] [3][1] [4][1] [5][1] [6][1]
#[0][2] [1][2] [2][2] [3][2] [4][2] [5][2] [6][2]
#[0][3] [1][3] [2][3] [3][3] [4][3] [5][3] [6][3]
#[0][4] [1][4] [2][4] [3][4] [4][4] [5][4] [6][4]
#[0][5] [1][5] [2][5] [3][5] [4][5] [5][5] [6][5]

# This is the function used to make a move.
# The function recieves the column (that is going to be given by the intelligent algorithm), and the player number that is making the move.
# If the move can't be made, the function returns -1, else: it returns the col in which it was placed.
def place(row, player_number):
    global board, width, height
    if(row >= width or row < 0):
        return -1
    partial_height = height  - 1
    while(partial_height >= 0 and board[row][partial_height] == 0):
        partial_height-=1
    if(partial_height + 1 < height):
        board[row][partial_height+1] = player_number
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
        if(board[pos][height-1] == 0):
            available_moves = True
            break;
 
    if(checkAnyT(player_number)):
        return 1
       
    if(not available_moves): 
        return -1
        
    return 0

#Function for printing the game board
def printGame():
    global board, width, height
    print "-----------------------------"
    for x in range(height-1,-1,-1):
        for y in range(0,width):
            #if(board[x][y] == 0):
             #   print (" ")
            print "|",board[y][x],
        print "|\n----+---+---+---+---+---+----"
    print "\n"
            
def checkAnyT(player_number):
    global board, width, height
    for r in range(0,width):
        for c in range(0,height):
            if(board[r][c] == player_number):
                if(checkWinBelow(c, r, player_number)
                or checkWinAbove(c, r, player_number)
                or checkLeft(c, r, player_number)
                or checkRight(c, r, player_number)
                or checkWinBottomRight(c, r, player_number)
                or checkWinBottomLeft(c, r, player_number)
                or checkWinTopLeft(c, r, player_number)
                or checkWinTopRight(c, r, player_number)):                    
                    return True
    return False
    
def checkWinBelow(col, row, player_number):
    global board, width, height
    if(col+1 == height or row == 0 or row+1 == width): return False
    if(board[row-1][col+1] == player_number and board[row][col+1] == player_number and board[row+1][col+1] == player_number): return True
    return False

def checkWinAbove(col, row, player_number):
    global board, width, height
    if(col == 0 or row == 0 or row+1 == width): return False
    if(board[row-1][col-1] == player_number and board[row][col-1] == player_number and board[row+1][col-1] == player_number): return True
    return False
    
def checkLeft(col, row, player_number):
    global board, width, height
    if(row + 1 >= width or col + 1 >= height or col - 1 < 0 ): return False
    if(board[row+1][col-1] == board[row+1][col] == board[row+1][col+1] == player_number): return True
    return False
    
def checkRight(col, row, player_number):
    global board, width, height
    if(row - 1 < 0 or col + 1 >= height or col - 1 < 0 ): return False
    if(board[row-1][col-1] == board[row-1][col] == board[row-1][col+1] == player_number): return True
    return False
    
def checkWinBottomRight(col, row, player_number):
    global board, width, height
    if(row - 2 < 0 or col + 2 >= height): return False
    if(board[row-2][col] == player_number and board[row-1][col+1] == player_number and board[row][col+2] == player_number): return True
    return False

def checkWinBottomLeft(col, row, player_number):
    global board, width, height
    if(row + 2 >= width or col - 2 < 0): return False
    if(board[row+2][col] == player_number and board[row+1][col-1] == player_number and board[row][col-2] == player_number): return True
    return False
    
def checkWinTopLeft(col, row, player_number):
    global board, width, height
    if(row + 2 >= width or col - 2 < 0): return False
    if(board[row+2][col] == player_number and board[row+1][col-1] == player_number and board[row][col-2] == player_number): return True
    return False
    
def checkWinTopRight(col, row, player_number):
    global board, width, height
    if(row - 2 < 0 or col - 2 < 0): return False
    if(board[row-2][col] == player_number and board[row-1][col-1] == player_number and board[row][col-2] == player_number): return True
    return False

def intelligentFunction1(turn, board):
    i=0
    if (turn==1):
        for x in range(height-1,-1,-1):
            for y in range(0,width):
                if(board[y][x]!=turn and board[y][x]!=0 and board[y][x+1]==0):
                    i=y
                    for r in range(0,height-3):
                        for c in range(0,width-3):
                            if(board[r][c]==1
                            and board[r+1][c]==1
                            and board[r+2][c]==1
                            and board[r+1][c+1]==0):
                                i=r+1
    else:
        start=1
        for u in range(0,width):
            if(board[u][0]!=0):
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
                    if(board[y][x]!=turn and board[y][x]!=0 and board[y][x+1]==0):
                        i=y
            if(board[i][height-1]!=0):
                i=random.randint(0,6)
                while (board[i][5]!=0):
                    i=random.randint(0,6)
    return i

def intelligentFunction2(turn, board):
    i=random.randint(0,6)
    while (board[i][5]!=0):
        i=random.randint(0,6)
    return i

class ConectaT:
    def __init__(self, IntraBoard, depth):
        self.IntraBoard = IntraBoard
        self.depth = depth
        if(depth<=1):
            self.p1 = ConectaT(IntraBoard,depth+1)
            self.p2 = ConectaT(IntraBoard,depth+1)
            self.p3 = ConectaT(IntraBoard,depth+1)
            self.p4 = ConectaT(IntraBoard,depth+1)
            self.p5 = ConectaT(IntraBoard,depth+1)
            self.p6 = ConectaT(IntraBoard,depth+1)
            self.p7 = ConectaT(IntraBoard,depth+1)
Q=ConectaT(board,0)

def main():
    global board
    turn = 1
    loser = 0
    while(gameFinished(turn) == 0):
        printGame()
        if(turn == 1):
            turn = 2
        else: turn = 1
        if(turn == 1):
            row = intelligentFunction2(turn, board)
        if(turn == 2):
            row = intelligentFunction1(turn, board)
        if (place(row,turn) == -1):
            loser = turn
            break;
        
    #Game is a tie
    if(gameFinished(turn) == -1): print "The game is a tie!"
    elif not(loser == 0): print "The loser is ", turn
    else: 
        printGame()
        print "The winner is ", turn
    
if __name__ == '__main__':
   main()
