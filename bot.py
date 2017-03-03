#from simulator import Board

class bot_player():
    def __init__(self):
        self.co=0
        self.block_value  = [[0 for j in range(4)] for i in range(4)]
        pass

    def game_won(self, board):
        bs = board.block_status

        cntx = 0
        cnto = 0
        cntd = 0

        for i in range(4):						#counts the blocks won by x, o and drawn blocks
            for j in range(4):
                if bs[i][j] == 'x':
                    cntx += 1
                if bs[i][j] == 'o':
                    cnto += 1
                if bs[i][j] == 'd':
                    cntd += 1

        #check if rows or columns won
        for i in range(4):
            row = bs[i]							#i'th row
            col = [x[i] for x in bs]			#i'th column
            #checking if i'th row or i'th column has been won or not
            if (row[0] =='x') and (row.count(row[0]) == 4):
                return (10000, True)
            if (col[0] =='x') and (col.count(col[0]) == 4):
                return (10000, True)
            if (row[0] =='o') and (row.count(row[0]) == 4):
                return (-10000, True)
            if (col[0] =='o') and (col.count(col[0]) == 4):
                    return (-10000, True)

        #checking if diagnols have been won or not
        if(bs[0][0] == bs[1][1] == bs[2][2] ==bs[3][3]) and (bs[0][0] == 'x'):
            return (10000, True)
        if(bs[0][3] == bs[1][2] == bs[2][1] ==bs[3][0]) and (bs[0][3] == 'x'):
            return (10000, True)
        if(bs[0][0] == bs[1][1] == bs[2][2] ==bs[3][3]) and (bs[0][0] == 'o'):
            return (-10000, True)
        if(bs[0][3] == bs[1][2] == bs[2][1] ==bs[3][0]) and (bs[0][3] == 'o'):
            return (-10000, True)

        if cntx+cnto+cntd <16:		#if all blocks have not yet been won, continue
            return (0, False)
        elif cntx+cnto+cntd == 16:							#if game is drawn
            return (0, True)

    def check_block_win(self, cell, board):
        x=cell[0]//4
        y=cell[1]//4
        #check win in row
        for i in range(4):
            if (board.board_status[4*x + i][y*4 + 0]==board.board_status[4*x + i][y*4 + 1]==board.board_status[4*x + i][y*4 + 2]==board.board_status[4*x + i][y*4 + 3]) and (board.board_status[4*x+i][4*y]!='-'):
                return 1
        #check win in column
        for i in range(4):
            if (board.board_status[4*x + 0][y*4 + i]==board.board_status[4*x + 1][y*4 + i]==board.board_status[4*x + 2][y*4 + i]==board.board_status[4*x + 3][y*4 + i]) and (board.board_status[4*x][4*y+i]!='-'):
                return 1
        #check primary diagonal
        if (board.board_status[4*x][4*y]==board.board_status[4*x+1][4*y+1]==board.board_status[4*x+2][4*y+2]==board.board_status[4*x+3][4*y+3]) and (board.board_status[4*x][4*y]!='-'):
            return 1
        #check if secondary diagonal won
        if (board.board_status[4*x][4*y + 3]==board.board_status[4*x+1][4*y+2]==board.board_status[4*x+2][4*y+1]==board.board_status[4*x+3][4*y]) and (board.board_status[4*x][4*y + 3]!='-'):
            return 1

        #block draw
        for i in range(4):
            for j in range(4):
                if board.board_status[4*x+i][4*y+j]=='-':
                    #block not won
                    return 0
        #block drawn
        return 2

    def calculate_value(self, board, old_move, block_value):
        current_block = (old_move[0]//4,old_move[1]//4)
        state_value = 0

        if board.block_status[current_block[0]][current_block[1]]=='d':
            return -100, block_value

        #evaluate rows
        for i in range(4):
            #row eavaluation of 'x'
            if board.board_status[current_block[0]*4+i].count('x') == 0:
                state_value += 0
            if board.board_status[current_block[0]*4+i].count('x') == 1:
                state_value += 10
            if board.board_status[current_block[0]*4+i].count('x') == 2:
                state_value += 30
            if board.board_status[current_block[0]*4+i].count('x') == 3:
                state_value += 100
            if board.board_status[current_block[0]*4+i].count('x') == 4:
                state_value += 1000

            #row eavaluation of 'o'
            if board.board_status[current_block[0]*4+i].count('o') == 0:
                state_value -= 0
            if board.board_status[current_block[0]*4+i].count('o') == 1:
                state_value -= 10
            if board.board_status[current_block[0]*4+i].count('o') == 2:
                state_value -= 30
            if board.board_status[current_block[0]*4+i].count('o') == 3:
                state_value -= 100
            if board.board_status[current_block[0]*4+i].count('o') == 4:
                state_value -= 1000

            #row eavaluation of 'o'
            if board.board_status[current_block[0]*4+i].count('o') == 0:
                state_value -= 0
            if board.board_status[current_block[0]*4+i].count('o') == 1:
                state_value -= 10
            if board.board_status[current_block[0]*4+i].count('o') == 2:
                state_value -= 30
            if board.board_status[current_block[0]*4+i].count('o') == 3:
                state_value -= 100
            if board.board_status[current_block[0]*4+i].count('o') == 4:
                state_value -= 1000

        #evaluate columns
        for i in range(4):
            col = [x[i] for x in board.board_status[current_block[1]*4:current_block[0]*4+4]]
            #column eavaluation of 'x'
            if col.count('x') == 0:
                state_value += 0
            if col.count('x') == 1:
                state_value += 10
            if col.count('x') == 2:
                state_value += 30
            if col.count('x') == 3:
                state_value += 100
            if col.count('x') == 4:
                state_value += 1000

            #column eavaluation of 'o'
            if col.count('o') == 0:
                state_value -= 0
            if col.count('o') == 1:
                state_value -= 10
            if col.count('o') == 2:
                state_value -= 30
            if col.count('o') == 3:
                state_value -= 100
            if col.count('o') == 4:
                state_value -= 1000

        #primary diagonal eavaluation
        diagonal = [board.board_status[current_block[0]*4+i][current_block[1]*4+i] for i in range(4)]
        #primary diagonal eavaluation for 'x'
        if diagonal.count('x') == 0:
            state_value += 0
        if diagonal.count('x') == 1:
            state_value += 10
        if diagonal.count('x') == 2:
            state_value += 30
        if diagonal.count('x') == 3:
            state_value += 100
        if diagonal.count('x') == 4:
            state_value += 1000

        #primary diagonal eavaluation for 'o'
        if diagonal.count('o') == 0:
            state_value -= 0
        if diagonal.count('o') == 1:
            state_value -= 10
        if diagonal.count('o') == 2:
            state_value -= 30
        if diagonal.count('o') == 3:
            state_value -= 100
        if diagonal.count('o') == 4:
            state_value -= 1000

        #secondary diagonal eavaluation
        diagonal = [board.board_status[current_block[0]*4+i][current_block[1]*4+(3-i)] for i in range(4)]
        #secondary diagonal eavaluation for 'x'
        if diagonal.count('x') == 0:
            state_value += 0
        if diagonal.count('x') == 1:
            state_value += 10
        if diagonal.count('x') == 2:
            state_value += 30
        if diagonal.count('x') == 3:
            state_value += 100
        if diagonal.count('x') == 4:
            state_value += 1000

        #secondary diagonal eavaluation for 'o'
        if diagonal.count('o') == 0:
            state_value -= 0
        if diagonal.count('o') == 1:
            state_value -= 10
        if diagonal.count('o') == 2:
            state_value -= 30
        if diagonal.count('o') == 3:
            state_value -= 100
        if diagonal.count('o') == 4:
            state_value -= 1000

        #update value of current block
        block_value[current_block[0]][current_block[1]] = state_value
        value=0
        br1=300
        br2=1200
        #rows
        for i in range(4):
            if block_value[i][0]>br1 or block_value[i][1]>br1 or block_value[i][2]>br1 or block_value[i][3]>br1:
                value+=10
            if block_value[i][0]>br2 or block_value[i][1]>br2 or block_value[i][2]>br2 or block_value[i][3]>br2:
                value+=20
            if( ( block_value[i][0]>br1 and block_value[i][1]>br1 ) or ( block_value[i][0]>br1 and block_value[i][2]>br1 ) or ( block_value[i][0]>br1 and block_value[i][3]>br1 ) or ( block_value[i][1]>br1 and block_value[i][2]>br1 ) or ( block_value[i][1]>br1 and block_value[i][3]>br1 ) or ( block_value[i][2]>br1 and block_value[i][3]>br1 )):
                value+=50
            if( ( block_value[i][0]>br2 and block_value[i][1]>br2 ) or ( block_value[i][0]>br2 and block_value[i][2]>br2 ) or ( block_value[i][0]>br2 and block_value[i][3]>br2 ) or ( block_value[i][1]>br2 and block_value[i][2]>br2 ) or ( block_value[i][1]>br2 and block_value[i][3]>br2 ) or ( block_value[i][2]>br2 and block_value[i][3]>br2 )):
                value+=200
            if ((block_value[i][0]>br1 and block_value[i][1]>br1 and block_value[i][2]>br1) or (block_value[i][0]>br1 and block_value[i][1]>br1 and block_value[i][3]>br1)) or (block_value[i][0]>br1 and block_value[i][2]>br1 and block_value[i][3]>br1) or (block_value[i][1]>br1 and block_value[i][2]>br1 and block_value[i][3]>br1):
                value+=500
            if ((block_value[i][0]>br2 and block_value[i][1]>br2 and block_value[i][2]>br2) or (block_value[i][0]>br2 and block_value[i][1]>br2 and block_value[i][3]>br2)) or (block_value[i][0]>br2 and block_value[i][2]>br2 and block_value[i][3]>br2) or (block_value[i][1]>br2 and block_value[i][2]>br2 and block_value[i][3]>br2):
                value+=800
            if block_value[i][0]>br1 and block_value[i][1]>br1 and block_value[i][2]>br1 and block_value[i][3]>br1:
                value+=800
            if block_value[i][0]>br2 and block_value[i][1]>br2 and block_value[i][2]>br2 and block_value[i][3]>br2:
                value+=1200

            if block_value[i][0]<-1*br1 or block_value[i][1]>br1 or block_value[i][2]<-1*br1 or block_value[i][3]<-1*br1:
                value-=10
            if block_value[i][0]<-1*br2 or block_value[i][1]<-1*br2 or block_value[i][2]<-1*br2 or block_value[i][3]<-1*br2:
                value-=20
            if( ( block_value[i][0]<-1*br1 and block_value[i][1]<-1*br1 ) or ( block_value[i][0]<-1*br1 and block_value[i][2]<-1*br1 ) or ( block_value[i][0]<-1*br1 and block_value[i][3]<-1*br1 ) or ( block_value[i][1]<-1*br1 and block_value[i][2]<-1*br1 ) or ( block_value[i][1]<-1*br1 and block_value[i][3]<-1*br1 ) or ( block_value[i][2]<-1*br1 and block_value[i][3]<-1*br1 )):
                value-=50
            if( ( block_value[i][0]<-1*br2 and block_value[i][1]<-1*br2 ) or ( block_value[i][0]<-1*br2 and block_value[i][2]<-1*br2 ) or ( block_value[i][0]<-1*br2 and block_value[i][3]<-1*br2 ) or ( block_value[i][1]<-1*br2 and block_value[i][2]<-1*br2 ) or ( block_value[i][1]<-1*br2 and block_value[i][3]<-1*br2 ) or ( block_value[i][2]<-1*br2 and block_value[i][3]<-1*br2 )):
                value-=200
            if ((block_value[i][0]<-1*br1 and block_value[i][1]<-1*br1 and block_value[i][2]<-1*br1) or (block_value[i][0]<-1*br1 and block_value[i][1]<-1*br1 and block_value[i][3]<-1*br1)) or (block_value[i][0]<-1*br1 and block_value[i][2]<-1*br1 and block_value[i][3]<-1*br1) or (block_value[i][1]<-1*br1 and block_value[i][2]<-1*br1 and block_value[i][3]<-1*br1):
                value-=500
            if ((block_value[i][0]<-1*br2 and block_value[i][1]<-1*br2 and block_value[i][2]<-1*br2) or (block_value[i][0]<-1*br2 and block_value[i][1]<-1*br2 and block_value[i][3]<-1*br2)) or (block_value[i][0]<-1*br2 and block_value[i][2]<-1*br2 and block_value[i][3]<-1*br2) or (block_value[i][1]<-1*br2 and block_value[i][2]<-1*br2 and block_value[i][3]<-1*br2):
                value-=800
            if block_value[i][0]<-1*br1 and block_value[i][1]<-1*br1 and block_value[i][2]<-1*br1 and block_value[i][3]<-1*br1:
                value-=800
            if block_value[i][0]<-1*br2 and block_value[i][1]<-1*br2 and block_value[i][2]<-1*br2 and block_value[i][3]<-1*br2:
                value-=1200

        #columns
        for i in range(4):
            if block_value[0][i]>br1 or block_value[1][i]>br1 or block_value[2][i]>br1 or block_value[3][i]>br1:
                value+=10
            if block_value[0][i]>br2 or block_value[1][i]>br2 or block_value[2][i]>br2 or block_value[3][i]>br2:
                value+=20
            if( ( block_value[0][i]>br1 and block_value[1][i]>br1 ) or ( block_value[0][i]>br1 and block_value[2][i]>br1 ) or ( block_value[0][i]>br1 and block_value[3][i]>br1 ) or ( block_value[1][i]>br1 and block_value[2][i]>br1 ) or ( block_value[1][i]>br1 and block_value[3][i]>br1 ) or ( block_value[2][i]>br1 and block_value[3][i]>br1 )):
                value+=50
            if( ( block_value[0][i]>br2 and block_value[1][i]>br2 ) or ( block_value[0][i]>br2 and block_value[2][i]>br2 ) or ( block_value[0][i]>br2 and block_value[3][i]>br2 ) or ( block_value[1][i]>br2 and block_value[2][i]>br2 ) or ( block_value[1][i]>br2 and block_value[3][i]>br2 ) or ( block_value[2][i]>br2 and block_value[3][i]>br2 )):
                value+=200
            if ((block_value[0][i]>br1 and block_value[1][i]>br1 and block_value[2][i]>br1) or (block_value[0][i]>br1 and block_value[1][i]>br1 and block_value[3][i]>br1)) or (block_value[0][i]>br1 and block_value[2][i]>br1 and block_value[3][i]>br1) or (block_value[1][i]>br1 and block_value[2][i]>br1 and block_value[3][i]>br1):
                value+=500
            if ((block_value[0][i]>br2 and block_value[1][i]>br2 and block_value[2][i]>br2) or (block_value[0][i]>br2 and block_value[1][i]>br2 and block_value[3][i]>br2)) or (block_value[0][i]>br2 and block_value[2][i]>br2 and block_value[3][i]>br2) or (block_value[1][i]>br2 and block_value[2][i]>br2 and block_value[3][i]>br2):
                value+=800
            if block_value[0][i]>br1 and block_value[1][i]>br1 and block_value[2][i]>br1 and block_value[3][i]>br1:
                value+=800
            if block_value[0][i]>br2 and block_value[1][i]>br2 and block_value[2][i]>br2 and block_value[3][i]>br2:
                value+=1200

            if block_value[0][i]<-1*br1 or block_value[1][i]<-1*br1 or block_value[2][i]<-1*br1 or block_value[3][i]<-1*br1:
                value-=10
            if block_value[0][i]<-1*br2 or block_value[1][i]<-1*br2 or block_value[2][i]<-1*br2 or block_value[3][i]<-1*br2:
                value-=20
            if( ( block_value[0][i]<-1*br1 and block_value[1][i]<-1*br1 ) or ( block_value[0][i]<-1*br1 and block_value[2][i]<-1*br1 ) or ( block_value[0][i]<-1*br1 and block_value[3][i]<-1*br1 ) or ( block_value[1][i]<-1*br1 and block_value[2][i]<-1*br1 ) or ( block_value[1][i]<-1*br1 and block_value[3][i]<-1*br1 ) or ( block_value[2][i]<-1*br1 and block_value[3][i]<-1*br1 )):
                value-=50
            if( ( block_value[0][i]<-1*br2 and block_value[1][i]<-1*br2 ) or ( block_value[0][i]<-1*br2 and block_value[2][i]<-1*br2 ) or ( block_value[0][i]<-1*br2 and block_value[3][i]<-1*br2 ) or ( block_value[1][i]<-1*br2 and block_value[2][i]<-1*br2 ) or ( block_value[1][i]<-1*br2 and block_value[3][i]<-1*br2 ) or ( block_value[2][i]<-1*br2 and block_value[3][i]<-1*br2 )):
                value-=200
            if ((block_value[0][i]<-1*br1 and block_value[1][i]<-1*br1 and block_value[2][i]<-1*br1) or (block_value[0][i]<-1*br1 and block_value[1][i]<-1*br1 and block_value[3][i]<-1*br1)) or (block_value[0][i]<-1*br1 and block_value[2][i]<-1*br1 and block_value[3][i]<-1*br1) or (block_value[1][i]<-1*br1 and block_value[2][i]<-1*br1 and block_value[3][i]<-1*br1):
                value-=500
            if ((block_value[0][i]<-1*br2 and block_value[1][i]<-1*br2 and block_value[2][i]<-1*br2) or (block_value[0][i]<-1*br2 and block_value[1][i]<-1*br2 and block_value[3][i]<-1*br2)) or (block_value[0][i]<-1*br2 and block_value[2][i]<-1*br2 and block_value[3][i]<-1*br2) or (block_value[1][i]<-1*br2 and block_value[2][i]<-1*br2 and block_value[3][i]<-1*br2):
                value-=800
            if block_value[0][i]<-1*br1 and block_value[1][i]<-1*br1 and block_value[2][i]<-1*br1 and block_value[3][i]<-1*br1:
                value-=800
            if block_value[0][i]<-1*br2 and block_value[1][i]<-1*br2 and block_value[2][i]<-1*br2 and block_value[3][i]<-1*br2:
                value-=1200

        #primary diagonal
            if block_value[0][0]>br1 or block_value[1][1]>br1 or block_value[2][2]>br1 or block_value[3][3]>br1:
                value+=10
            if block_value[0][0]>br2 or block_value[1][1]>br2 or block_value[2][2]>br2 or block_value[3][3]>br2:
                value+=20
            if( ( block_value[0][0]>br1 and block_value[1][1]>br1 ) or ( block_value[0][0]>br1 and block_value[2][2]>br1 ) or ( block_value[0][0]>br1 and block_value[3][3]>br1 ) or ( block_value[1][1]>br1 and block_value[2][2]>br1 ) or ( block_value[1][1]>br1 and block_value[3][3]>br1 ) or ( block_value[2][2]>br1 and block_value[3][3]>br1 )):
                value+=50
            if( ( block_value[0][0]>br2 and block_value[1][1]>br2 ) or ( block_value[0][0]>br2 and block_value[2][2]>br2 ) or ( block_value[0][0]>br2 and block_value[3][3]>br2 ) or ( block_value[1][1]>br2 and block_value[2][2]>br2 ) or ( block_value[1][1]>br2 and block_value[3][3]>br2 ) or ( block_value[2][2]>br2 and block_value[3][3]>br2 )):
                value+=200
            if ((block_value[0][0]>br1 and block_value[1][1]>br1 and block_value[2][2]>br1) or (block_value[0][0]>br1 and block_value[1][1]>br1 and block_value[3][3]>br1)) or (block_value[0][0]>br1 and block_value[2][2]>br1 and block_value[3][3]>br1) or (block_value[1][1]>br1 and block_value[2][2]>br1 and block_value[3][3]>br1):
                value+=500
            if ((block_value[0][0]>br2 and block_value[1][1]>br2 and block_value[2][2]>br2) or (block_value[0][0]>br2 and block_value[1][1]>br2 and block_value[3][3]>br2)) or (block_value[0][0]>br2 and block_value[2][2]>br2 and block_value[3][3]>br2) or (block_value[1][1]>br2 and block_value[2][2]>br2 and block_value[3][3]>br2):
                value+=800
            if block_value[0][0]>br1 and block_value[1][1]>br1 and block_value[2][2]>br1 and block_value[3][3]>br1:
                value+=800
            if block_value[0][0]>br2 and block_value[1][1]>br2 and block_value[2][2]>br2 and block_value[3][3]>br2:
                value+=1200

            if block_value[0][0]<-1*br1 or block_value[1][1]<-1*br1 or block_value[2][2]<-1*br1 or block_value[3][3]<-1*br1:
                value-=10
            if block_value[0][0]<-1*br2 or block_value[1][1]<-1*br2 or block_value[2][2]<-1*br2 or block_value[3][3]<-1*br2:
                value-=20
            if( ( block_value[0][0]<-1*br1 and block_value[1][1]<-1*br1 ) or ( block_value[0][0]<-1*br1 and block_value[2][2]<-1*br1 ) or ( block_value[0][0]<-1*br1 and block_value[3][3]<-1*br1 ) or ( block_value[1][1]<-1*br1 and block_value[2][2]<-1*br1 ) or ( block_value[1][1]<-1*br1 and block_value[3][3]<-1*br1 ) or ( block_value[2][2]<-1*br1 and block_value[3][3]<-1*br1 )):
                value-=50
            if( ( block_value[0][0]<-1*br2 and block_value[1][1]<-1*br2 ) or ( block_value[0][0]<-1*br2 and block_value[2][2]<-1*br2 ) or ( block_value[0][0]<-1*br2 and block_value[3][3]<-1*br2 ) or ( block_value[1][1]<-1*br2 and block_value[2][2]<-1*br2 ) or ( block_value[1][1]<-1*br2 and block_value[3][3]<-1*br2 ) or ( block_value[2][2]<-1*br2 and block_value[3][3]<-1*br2 )):
                value-=200
            if ((block_value[0][0]<-1*br1 and block_value[1][1]<-1*br1 and block_value[2][2]<-1*br1) or (block_value[0][0]<-1*br1 and block_value[1][1]<-1*br1 and block_value[3][3]<-1*br1)) or (block_value[0][0]<-1*br1 and block_value[2][2]<-1*br1 and block_value[3][3]<-1*br1) or (block_value[1][1]<-1*br1 and block_value[2][2]<-1*br1 and block_value[3][3]<-1*br1):
                value-=500
            if ((block_value[0][0]<-1*br2 and block_value[1][1]<-1*br2 and block_value[2][2]<-1*br2) or (block_value[0][0]<-1*br2 and block_value[1][1]<-1*br2 and block_value[3][3]<-1*br2)) or (block_value[0][0]<-1*br2 and block_value[2][2]<-1*br2 and block_value[3][3]<-1*br2) or (block_value[1][1]<-1*br2 and block_value[2][2]<-1*br2 and block_value[3][3]<-1*br2):
                value-=800
            if block_value[0][0]<-1*br1 and block_value[1][1]<-1*br1 and block_value[2][2]<-1*br1 and block_value[3][3]<-1*br1:
                value-=800
            if block_value[0][0]<-1*br2 and block_value[1][1]<-1*br2 and block_value[2][2]<-1*br2 and block_value[3][3]<-1*br2:
                value-=1200


        #secondary diagonal
            if block_value[0][3]>br1 or block_value[1][2]>br1 or block_value[2][1]>br1 or block_value[3][0]>br1:
                value+=10
            if block_value[0][3]>br2 or block_value[1][2]>br2 or block_value[2][1]>br2 or block_value[3][0]>br2:
                value+=20
            if( ( block_value[0][3]>br1 and block_value[1][2]>br1 ) or ( block_value[0][3]>br1 and block_value[2][1]>br1 ) or ( block_value[0][3]>br1 and block_value[3][0]>br1 ) or ( block_value[1][2]>br1 and block_value[2][1]>br1 ) or ( block_value[1][2]>br1 and block_value[3][0]>br1 ) or ( block_value[2][1]>br1 and block_value[3][0]>br1 )):
                value+=50
            if( ( block_value[0][3]>br2 and block_value[1][2]>br2 ) or ( block_value[0][3]>br2 and block_value[2][1]>br2 ) or ( block_value[0][3]>br2 and block_value[3][0]>br2 ) or ( block_value[1][2]>br2 and block_value[2][1]>br2 ) or ( block_value[1][2]>br2 and block_value[3][0]>br2 ) or ( block_value[2][1]>br2 and block_value[3][0]>br2 )):
                value+=200
            if ((block_value[0][3]>br1 and block_value[1][2]>br1 and block_value[2][1]>br1) or (block_value[0][3]>br1 and block_value[1][2]>br1 and block_value[3][0]>br1)) or (block_value[0][3]>br1 and block_value[2][1]>br1 and block_value[3][0]>br1) or (block_value[1][2]>br1 and block_value[2][1]>br1 and block_value[3][0]>br1):
                value+=500
            if ((block_value[0][3]>br2 and block_value[1][2]>br2 and block_value[2][1]>br2) or (block_value[0][3]>br2 and block_value[1][2]>br2 and block_value[3][0]>br2)) or (block_value[0][3]>br2 and block_value[2][1]>br2 and block_value[3][0]>br2) or (block_value[1][2]>br2 and block_value[2][1]>br2 and block_value[3][0]>br2):
                value+=800
            if block_value[0][3]>br1 and block_value[1][2]>br1 and block_value[2][1]>br1 and block_value[3][0]>br1:
                value+=800
            if block_value[0][3]>br2 and block_value[1][2]>br2 and block_value[2][1]>br2 and block_value[3][0]>br2:
                value+=1200

            if block_value[0][3]<-1*br1 or block_value[1][2]<-1*br1 or block_value[2][1]<-1*br1 or block_value[3][0]<-1*br1:
                value-=10
            if block_value[0][3]<-1*br2 or block_value[1][2]<-1*br2 or block_value[2][1]<-1*br2 or block_value[3][0]<-1*br2:
                value-=20
            if( ( block_value[0][3]<-1*br1 and block_value[1][2]<-1*br1 ) or ( block_value[0][3]<-1*br1 and block_value[2][1]<-1*br1 ) or ( block_value[0][3]<-1*br1 and block_value[3][0]<-1*br1 ) or ( block_value[1][2]<-1*br1 and block_value[2][1]<-1*br1 ) or ( block_value[1][2]<-1*br1 and block_value[3][0]<-1*br1 ) or ( block_value[2][1]<-1*br1 and block_value[3][0]<-1*br1 )):
                value-=50
            if( ( block_value[0][3]<-1*br2 and block_value[1][2]<-1*br2 ) or ( block_value[0][3]<-1*br2 and block_value[2][1]<-1*br2 ) or ( block_value[0][3]<-1*br2 and block_value[3][0]<-1*br2 ) or ( block_value[1][2]<-1*br2 and block_value[2][1]<-1*br2 ) or ( block_value[1][2]<-1*br2 and block_value[3][0]<-1*br2 ) or ( block_value[2][1]<-1*br2 and block_value[3][0]<-1*br2 )):
                value-=200
            if ((block_value[0][3]<-1*br1 and block_value[1][2]<-1*br1 and block_value[2][1]<-1*br1) or (block_value[0][3]<-1*br1 and block_value[1][2]<-1*br1 and block_value[3][0]<-1*br1)) or (block_value[0][3]<-1*br1 and block_value[2][1]<-1*br1 and block_value[3][0]<-1*br1) or (block_value[1][2]<-1*br1 and block_value[2][1]<-1*br1 and block_value[3][0]<-1*br1):
                value-=500
            if ((block_value[0][3]<-1*br2 and block_value[1][2]<-1*br2 and block_value[2][1]<-1*br2) or (block_value[0][3]<-1*br2 and block_value[1][2]<-1*br2 and block_value[3][0]<-1*br2)) or (block_value[0][3]<-1*br2 and block_value[2][1]<-1*br2 and block_value[3][0]<-1*br2) or (block_value[1][2]<-1*br2 and block_value[2][1]<-1*br2 and block_value[3][0]<-1*br2):
                value-=800
            if block_value[0][3]<-1*br1 and block_value[1][2]<-1*br1 and block_value[2][1]<-1*br1 and block_value[3][0]<-1*br1:
                value-=800
            if block_value[0][3]<-1*br2 and block_value[1][2]<-1*br2 and block_value[2][1]<-1*br2 and block_value[3][0]<-1*br2:
                value-=1200

        #return value, block_value
        return state_value, block_value


    def minimax(self, board, old_move, isMax, alpha, beta, depth, block_value):
        self.co+=1
        victory, isleaf=self.game_won(board)
        if isleaf:
            return (None, victory)

        #calculate value of the state
        state_value, block_value = self.calculate_value(board,old_move, block_value)
        if depth > 5:
            return (None, block_value)

        #max player playing
        if isMax:
            best=-10000000
            cells=board.find_valid_move_cells(old_move)
            if len(cells)==256:
                cells = []
                for i in range(4*1, 4*1+4):
                    for j in range(4*1, 4*1+4):
                        cells.append((i,j))

            best_move=(-1,-1)
            for cell in cells:
                board.board_status[cell[0]][cell[1]]='x'
                block_win = self.check_block_win(cell, board)
                value=-10000000
                if block_win==1:
                    board.block_status[cell[0]//4][cell[1]//4]='x'
                elif block_win==2:
                    board.block_status[cell[0]//4][cell[1]//4]='d'
                try:
                    proposed_move, value  = self.minimax(board, cell, False, alpha, beta, depth+1, block_value)
                except Exception as e:
                    print e
                board.board_status[cell[0]][cell[1]]='-'
                if block_win:
                    board.block_status[cell[0]//4][cell[1]//4]='-'
                if best<value :
                    best = value
                    best_move = cell
                if alpha <= best :
                    alpha = best

                if beta <= alpha:
                    break

            return best_move, state_value

        #min player playing
        else:
            best=-10000000
            cells=board.find_valid_move_cells(old_move)
            best_move=(-1,-1)
            for cell in cells:
                board.board_status[cell[0]][cell[1]]='o'
                block_win = self.check_block_win(cell, board)
                #print block_win
                if block_win==1:
                    board.block_status[cell[0]//4][cell[1]//4]='o'
                if block_win==2:
                    board.block_status[cell[0]//4][cell[1]//4]='d'
                value=10000000
                try:
                    proposed_move, value  = self.minimax(board, cell, True, alpha, beta, depth + 1, block_value)
                except Exception as e:
                    print e
                board.board_status[cell[0]][cell[1]]='-'
                if block_win:
                    board.block_status[cell[0]//4][cell[1]//4]='-'
                if best < value:
                    best=value
                    best_move = cell
                if beta > 16 - best :
                    beta = 16 - best

                if beta<=alpha:
                    break

            return best_move, state_value


    def move(self, board, old_move, flag):
        #print "hello"
        self.co=0

        if flag=='x':
            isMax=True;
        else :
            isMax=False;
        next_move=None

        try :
            next_move, optimal=self.minimax(board, old_move, isMax, -1000, 1000, 1, self.block_value)
            value, self.block_value = self.calculate_value(board, old_move, self.block_value)
            #print next_move
        except Exception as e:
            print e
        #board.print_board()
        print self.co
        print next_move
        #print "bye"
        return (next_move[0],next_move[1])
