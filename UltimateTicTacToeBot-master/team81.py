# Global constants
FIRST_MOVE=(-1,-1)

# block structure
# 0 | 1 | 2
# ---------
# 3 | 4 | 5
# ---------
# 6 | 7 | 8

# Don't remember why I needed this.
# Adjacent move
M_U=-3 # up
M_D=+3 # down
M_R=+1 # right
M_L=-1 # left
M_UL=M_U+M_L # up-left
M_UR=M_U+M_R # up-right
M_DL=M_D+M_L # down-left
M_DR=M_D+M_R # down-right

# corner cells
C_CORNER=[0,2,6,8]

# Adjacent cells
C_ADJ=[1,3,5,7]

# center cell
C_CENTER=[4]

# rows are defined from left to right
# top row
C_TOPR=(0,1,2)

# middle row
C_MIDDLER=(3,4,5)

# bottom row
C_BOTTOMR=(6,7,8)

C_ROWS=(C_TOPR,C_MIDDLER,C_BOTTOMR)

# columns are defined from top to bottom
# left column
C_LEFTC=(0,3,6)

# middle column
C_MIDDLEC=(1,4,7)

# right column
C_RIGHTC=(2,5,8)

C_COLS=(C_LEFTC,C_MIDDLEC,C_RIGHTC)

# diagonals are from left to right
# top-left to bottom-right
C_DIAGT=(0,4,8)

# bottom-left to top-right
C_DIAGB=(6,4,2)

C_DIAGS=(C_DIAGT,C_DIAGB)

C_ALL=C_ROWS+C_COLS+C_DIAGS

# Single rows/column/diagonal
S_LT, S_RB, S_LR = {}, {}, {}

S_LT['x']=('x','-','-') # left and top
S_RB['x']=('-','-','x') # right and bottom
S_LR['x']=('-','x','-') # middle

S_LT['o']=('o','-','-') # left and top
S_RB['o']=('-','-','o') # right and bottom
S_LR['o']=('-','o','-') # middle

# Double rows/column/diagonal - left to right and top to bottom
D_LT, D_RB, D_LR = {}, {}, {}

D_LT['x']=('x','x','-') # left and top
D_RB['x']=('-','x','x') # right and bottom
D_LR['x']=('x','-','x') # both

D_LT['o']=('o','o','-') # left and top
D_RB['o']=('-','o','o') # right and bottom
D_LR['o']=('o','-','o') # both

# Win row/column/diagonal
W_LR={}
W_LR['x']=('x','x','x')
W_LR['o']=('o','o','o')

# minimax variables
SEARCH_DEPTH=5
MOVES1=5
MOVES2=17
MOVES3=29
DI1=3
DI2=5
DI3=10

ALPHA=-100000
BETA=+100000

import random
from collections import defaultdict

class Player81:
    
    def __init__(self):
        self.__flag = '-'
        self.ST = defaultdict(list) # Search Tree
        #self.PST = [] # Pruned out moves
        self.number_of_moves=0

    def move(self, board, block, old_move, flag):

        #print old_move, board[old_move[0]][old_move[1]], flag

        self.__flag = flag
        self.ST = defaultdict(list)

        newboard=[]
        for i in range(9):
            newboard.append([[]]*9)
        if old_move == FIRST_MOVE:
            new_old_move = old_move
        else:
            new_old_move = row_column_to_block_cell((old_move[0], old_move[1]))

        for row in range(9):
            for col in range(9):
                v = board[row][col]
                (tblock,tcell) = row_column_to_block_cell((row, col))
                newboard[tblock][tcell] = v

        #if new_old_move != flag:
            #print new_old_move, newboard[new_old_move[0]][new_old_move[1]], flag
        
        depth = 0
        alpha = ALPHA
        beta = BETA
        
        new_move = old_move # redundant; only used to initialize
        move_utility = 0
        (new_move, move_utility) = self.search(newboard, block, new_old_move, flag, depth, alpha, beta)
        
        if self.number_of_moves > 1:
            if self.number_of_moves % MOVES1:
                SEARCH_DEPTH += DI1
            if self.number_of_moves % MOVES2:
                SEARCH_DEPTH += DI2
            if self.number_of_moves % MOVES3:
                SEARCH_DEPTH += DI3

        return block_cell_to_row_column(new_move)

    def search(self, board, block, old_move, flag, depth, alpha, beta):

        if depth == SEARCH_DEPTH:
            node_utility = calculate_board_utility(board, block, self.__flag)
            return (old_move, node_utility)

        WIN_STAT = check_win_board(block, self.__flag) # 1 -> win, -1 -> lose, 0 -> don't know
        if WIN_STAT == 1:
            return (old_move, WIN_BOARD)
        elif WIN_STAT == -1:
            return (old_move, -WIN_BOARD)

        # determine valid blocks
        valid_blocks = determine_valid_blocks(old_move,block) # valid_blocks is a list
        
        # determine valid cells
        valid_cells = determine_valid_cells(board,valid_blocks,block) # valid_cells is a list block-cell format
        #print valid_cells

        self.ST[old_move] = valid_cells
        oflag = flaginvert(flag) # opposite flag
        
        m_node = depth % 2 # 0->max and 1->min       

        new_move = old_move # redundant; only used to initialize

        if m_node == 0: # if depth < SEARCH_DEPTH:
            node_utility = beta
            for move in valid_cells:
                board[move[0]][move[1]] = flag
                (tmove, move_utility) = self.search(board, block, move, oflag, depth+1, node_utility, alpha)
                board[move[0]][move[1]] = '-'
                if move_utility > node_utility:
                    new_move, node_utility = move, move_utility

                if node_utility > alpha:
                    new_move = move
                    return (new_move, alpha)
                    
            return (new_move, node_utility)

        elif m_node == 1:
            node_utility = beta
            for move in valid_cells:
                board[move[0]][move[1]] = flag
                (tmove, move_utility) = self.search(board, block, move, oflag, depth+1, beta, node_utility)
                board[move[0]][move[1]] = '-'
                
                if move_utility < node_utility:
                    new_move, node_utility = move, move_utility
                    
                if node_utility < beta:
                    new_move = move
                    return (new_move, beta)

            return (new_move, node_utility)

def flaginvert(flag):
    if flag == 'x':
        return 'o'
    elif flag == 'o':
        return 'x'
    else:
        return '-'

def determine_valid_blocks(old_move,block):
    temp_blocks = []

    if old_move == FIRST_MOVE:
        temp_blocks = list(range(9))
        return temp_blocks

    # Correspondence rules
    if old_move[1] == 0:
        temp_blocks = [1,3]
    elif old_move[1] == 1:
        temp_blocks = [0,2]
    elif old_move[1] == 2:
        temp_blocks = [1,5]
    elif old_move[1] == 3:
        temp_blocks = [0,6]
    elif old_move[1] == 5:
        temp_blocks = [2,8]
    elif old_move[1] == 6:
        temp_blocks = [3,7]
    elif old_move[1] == 7:
        temp_blocks = [6,8]
    elif old_move[1] == 8:
        temp_blocks = [5,7]

    # Center rule
    elif old_move[1] == 4:
        temp_blocks = [4]

    # Abandon rule
    for b in temp_blocks:
        if block[b] != '-':
            temp_blocks.remove(b)

    # Free Move
    if temp_blocks.__len__() == 0:
        for b in range(9):
            if block[b] == '-':
                temp_blocks.append(b)

    # Abandon rule
    for b in temp_blocks:
        if block[b] != '-':
            temp_blocks.remove(b)

    return temp_blocks

def determine_valid_cells(board, valid_blocks, block):
    temp_cells = []
    for bno in valid_blocks:
        for cell in C_CENTER+C_CORNER+C_ADJ:
            if board[bno][cell] == '-':
                temp_cells.append((bno, cell))
    
    if temp_cells.__len__() == 0:
        for i in range(9):
            for j in C_CENTER+C_CORNER+C_ADJ:
                if block[i]=='-' and i not in valid_blocks:
                    if board[i][j] == '-':
                        temp_cells.append((i,j))

    return temp_cells

def block_cell_to_row_column((block, cell)):
    row = (3*(block/3))+(cell/3)
    column = (3*(block%3))+(cell%3)
    return (row, column)

def row_column_to_block_cell((row, column)):
    block = (3*(row/3))+(column/3)
    cell = (3*(row%3))+(column%3)
    return (block, cell)

# Utility points

# Single points
# |->Blocked
OCC=-1 # #modify

# |->Unblocked
CENTER_CELL=8 # #modify
CORNER_CELL=6 # #modify
ADJ_CELL=4 # #modify

# Double points
# |->Blocked
D_C_B=-24 # #modify
D_S_B=-24 # #modify

# |->Unblocked
D_C_UB=60 # #modify
D_S_UB=72 # #modify

# fork
F_RC=250 # #modify
F_DIAG=200 # #modify

# Full/win
WIN_BL=1000 # #modify

WIN_BOARD=5000

def calculate_board_utility(board, block, flag):

    WIN_STAT = check_win_board(block, flag)
    if WIN_STAT == 1:
        return WIN_BOARD
    elif WIN_STAT == -1:
        return -WIN_BOARD
    

    if flag == 'x':
        o_flag = 'o'
    elif flag == 'o':
        o_flag = 'x'

    MU=0 # Max utility
    block_utility=list(range(9))
    for b in range(9):
        if block[b]==flag:
            block_utility[b]=WIN_BL
        elif block[b]==o_flag:
            block_utility[b]=-2*WIN_BL # #modify
        else:
            block_utility[b]=calculate_block_utility(board[b], flag)

    #for b in range(9):
    #    block_utility[b]=block_utility[b]
    
    for b in block_utility:
        MU += b

    return MU

def calculate_block_utility(block, flag):
    MU=0
    MU+=check_sp(block, flag) # single points
    MU+=check_dp(block, flag) # double points
    MU+=check_fp(block, flag) # fork points
    #MU+=check_wp(block, flag) # win points
    return MU

def check_sp(block, flag):
    MU = 0
    for t in C_DIAGS+(C_MIDDLER, C_MIDDLEC):
        if check_tuple(block, t, S_LR[flag]):
            MU += CENTER_CELL
        else:
            MU += OCC

    for t in (C_TOPR, C_LEFTC, C_DIAGT)+(C_BOTTOMR, C_RIGHTC, C_DIAGT):
        if check_tuple(block, t, S_LT[flag]) or check_tuple(block, t, S_RB[flag]):
            MU += CORNER_CELL
        else:
            MU += OCC

    for t in (C_TOPR, C_LEFTC, C_BOTTOMR, C_RIGHTC):
        if check_tuple(block, t, S_LR[flag]):
            MU += ADJ_CELL
        else:
            MU += OCC

    return MU

def check_dp(block, flag):
    MU = 0
    for t in C_DIAGS+(C_MIDDLER, C_MIDDLEC):
        if check_tuple(block, t, D_LT[flag]) or check_tuple(block, t, D_RB[flag]):
            MU += D_C_UB
        else:
            MU += D_C_B

    for t in C_ALL:
        if check_tuple(block, t, D_LR[flag]):
            MU += D_S_UB
        else:
            MU += D_S_B

    for t in (C_TOPR, C_LEFTC, C_BOTTOMR, C_RIGHTC):
        if check_tuple(block, t, D_LT[flag]) or check_tuple(block, t, D_RB[flag]):
            MU += D_S_UB
        else:
            MU += D_S_B
    
    return MU

def check_fp(block, flag):
    MU = 0

    for t1 in (C_TOPR,C_MIDDLER):
        for t2 in (C_LEFTC,C_MIDDLEC):
            if (check_tuple(block, t1, D_LT[flag]) or check_tuple(block, t1, D_LR[flag])) and (check_tuple(block, t2, D_LT[flag]) or check_tuple(block, t2, D_LR[flag])):
                MU += F_RC
                break

    for t1 in (C_TOPR,C_MIDDLER):
        for t2 in (C_RIGHTC,C_MIDDLEC):
            if (check_tuple(block, t1, D_RB[flag]) or check_tuple(block, t1, D_LR[flag])) and (check_tuple(block, t2, D_LT[flag]) or check_tuple(block, t2, D_LR[flag])):
                MU += F_RC
                break

    for t1 in (C_BOTTOMR,C_MIDDLER):
        for t2 in (C_LEFTC,C_MIDDLEC):
            if (check_tuple(block, t1, D_LT[flag]) or check_tuple(block, t1, D_LR[flag])) and (check_tuple(block, t2, D_RB[flag]) or check_tuple(block, t2, D_LR[flag])):
                MU += F_RC
                break

    for t1 in (C_BOTTOMR,C_MIDDLER):
        for t2 in (C_RIGHTC,C_MIDDLEC):
            if (check_tuple(block, t1, D_RB[flag]) or check_tuple(block, t1, D_LR[flag])) and (check_tuple(block, t2, D_RB[flag]) or check_tuple(block, t2, D_LR[flag])):
                MU += F_RC
                break
    
    if (check_tuple(block, C_DIAGT, D_LT[flag]) or check_tuple(block, C_DIAGT, D_RB[flag])) and (check_tuple(block, C_DIAGB, D_LT[flag]) or check_tuple(block, C_DIAGB, D_RB[flag])):
        MU += F_DIAG

    return MU


def check_wp(block, flag):
    MU = 0
    for t in C_ALL:
        if check_tuple(block, t, W_LR[flag]):
            MU += WIN_BL
            break

    return MU

def check_tuple(block, tindex, ctuple):
    tmp = []
    for i in tindex:
        tmp.append(block[i])
    temp = tuple(tmp)
    if temp == ctuple:
        return True
    else:
        return False

def check_win_board(block, flag):
    oflag=flaginvert(flag)
    for t in C_ALL:
        if check_tuple(block, t, W_LR[flag]):
            return +1
        if check_tuple(block, t, W_LR[oflag]):
            return -1
    return 0
