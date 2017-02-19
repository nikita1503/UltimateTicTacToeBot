#from simulator import Board

class bot_player():
    def __init__(self):
        self.co=0
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
                return (cntx, True)
            if (col[0] =='x') and (col.count(col[0]) == 4):
                return (cntx, True)
            if (row[0] =='o') and (row.count(row[0]) == 4):
                return (cntx, True)
            if (col[0] =='0') and (col.count(col[0]) == 4):
                    return (cntx, True)

        #checking if diagnols have been won or not
        if(bs[0][0] == bs[1][1] == bs[2][2] ==bs[3][3]) and (bs[0][0] == 'x'):
            return (cntx, True)
        if(bs[0][3] == bs[1][2] == bs[2][1] ==bs[3][0]) and (bs[0][3] == 'x'):
            return (cntx, True)
        if(bs[0][0] == bs[1][1] == bs[2][2] ==bs[3][3]) and (bs[0][0] == 'o'):
            return (cnto, True)
        if(bs[0][3] == bs[1][2] == bs[2][1] ==bs[3][0]) and (bs[0][3] == 'o'):
            return (cnto, True)

        if cntx+cnto+cntd <16:		#if all blocks have not yet been won, continue
            return (cntx, False)
        elif cntx+cnto+cntd == 16:							#if game is drawn
            return (0, True)

    def check_block_win(self, cell, board):
        x=cell[0]//4
        y=cell[1]//4
        #check win in row
        for i in range(4):
            if (board.board_status[4*x + i][y*4 + 0]==board.board_status[4*x + i][y*4 + 1]==board.board_status[4*x + i][y*4 + 2]==board.board_status[4*x + i][y*4 + 3]) and (board.board_status[4*x+i][4*y]!='-'):
                return True
        #check win in column
        for i in range(4):
            if (board.board_status[4*x + 0][y*4 + i]==board.board_status[4*x + 1][y*4 + i]==board.board_status[4*x + 2][y*4 + i]==board.board_status[4*x + 3][y*4 + i]) and (board.board_status[4*x][4*y+i]!='-'):
                return True
        #check primary diagonal
        if (board.board_status[4*x][4*y]==board.board_status[4*x+1][4*y+1]==board.board_status[4*x+2][4*y+2]==board.board_status[4*x+3][4*y+3]) and (board.board_status[4*x][4*y]!='-'):
            return True
        #check if secondary diagonal won
        if (board.board_status[4*x][4*y + 3]==board.board_status[4*x+1][4*y+2]==board.board_status[4*x+2][4*y+1]==board.board_status[4*x+3][4*y]) and (board.board_status[4*x][4*y + 3]!='-'):
            return True
        #block not won
        return False

    def minimax(self, board, old_move, isMax, alpha, beta, depth):
        self.co+=1
        victory, isleaf=self.game_won(board)
        if isleaf:
            return (None, victory)
        if depth > 3:
            return (None, victory)

        #max player playing
        if isMax:
            best=-1000
            cells=board.find_valid_move_cells(old_move)
            best_move=(-1,-1)
            self.no=0
            for cell in cells:
                self.no+=1
                if self.no>3:
                    break
                board.board_status[cell[0]][cell[1]]='x'
                block_win = self.check_block_win(cell, board)
                if block_win:
                    board.block_status[cell[0]//4][cell[1]//4]='x'
                try:
                    proposed_move, value  = self.minimax(board, cell, False, alpha, beta, depth+1)
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
                    #alpha_move = best_move

                if beta <= alpha:
                    break

            return best_move, victory

        #min player playing
        else:
            best=-1000
            cells=board.find_valid_move_cells(old_move)
            best_move=(-1,-1)
            for cell in cells:
                board.board_status[cell[0]][cell[1]]='o'
                block_win = self.check_block_win(cell, board)
                #print block_win
                if block_win:
                    board.block_status[cell[0]//4][cell[1]//4]='o'
                try:
                    proposed_move, value  = self.minimax(board, cell, True, alpha, beta, depth + 1)
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
                    #beta_move = best_move

                if beta<=alpha:
                    break

            return best_move, victory


    def move(self, board, old_move, flag):
        #print "hello"
        self.co=0

        if flag=='x':
            isMax=True;
        else :
            isMax=False;
        next_move=None

        try :
            next_move, optimal=self.minimax(board, old_move, isMax, -1000, 1000, 1)
            #print next_move
        except Exception as e:
            print e
        #board.print_board()
        print self.co
        #print next_move
        #print "bye"
        return (next_move[0],next_move[1])
