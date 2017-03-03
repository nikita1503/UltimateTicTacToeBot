#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8

from copy import deepcopy
import time
from random import shuffle


class Player76:

    def __init__(self):
        self.INF = 1000000000000000000
        self.t0 = 0
        self.complete = False

        self.visited = {}

    def block_win(self,player,game,base1,base2):
        base1*=3
        base2*=3
        if game[base1+0][base2+0]==player and game[base1+1][base2+1]==player and game[base1+2][base2+2]==player:
            return 1
        if game[base1+0][base2+2]==player and game[base1+1][base2+1]==player and game[base1+2][base2+0]==player:
            return 1
        for i in range(0,3):
            if game[base1+i][base2+0]==player and game[base1+i][base2+1]==player and game[base1+i][base2+2]==player:
                return 1
            if game[base1+0][base2+i]==player and game[base1+1][base2+i]==player and game[base1+2][base2+i]==player:
                return 1
        return 0

    def board_win(self,player,game):
        blocks = [[0,0,0],[0,0,0],[0,0,0]]
        for i in range(0,3):
            for j in range(0,3):
                blocks[i][j]=self.block_win(player,game,i,j)
        if blocks[0][0]==1 and blocks[1][1]==1 and blocks[2][2]==1:
            return 1
        if blocks[0][2]==1 and blocks[1][1]==1 and blocks[2][0]==1:
            return 1
        for i in range(0,3):
            if blocks[i][0]==1 and blocks[i][1]==1 and blocks[i][2]==1:
                return 1
            if blocks[0][i]==1 and blocks[1][i]==1 and blocks[2][i]==1:
                return 1
        return 0

    def completed_board(self,game):
        for i in range(0,9):
            for j in range(0,9):
                if game[i][j]=='-' and self.block_win('x',game,i/3,j/3)==0 and self.block_win('o',game,i/3,j/3)==0:
                    return 0
        return 1

    def completed_block(self,game,a,b):
        if self.block_win('x',game,a,b) or self.block_win('o',game,a,b):
            return 1
        for i in range(0,3):
            for j in range(0,3):
                if game[i+a*3][j+b*3]=='-':
                    return 0
        return 1

    #HEURISTIC - DOESNT WORK WELL!
    def assumedScore(self,game,depth,player,flag):
        depth = min(depth, 85)
        in1 = 1
        in2 = 8
        in3 = 100
        in1op = 1
        in2op = 8
        in3op = 100
        final_score = 0.0
        if self.board_win(flag,game):
            return self.INF * ((1.0/depth)**(1.0/3.0))
        elif self.board_win(('x' if flag == 'o' else 'o'),game):
            return -self.INF * ((1.0/depth)**(1.0/3.0))
        block = [[0,0,0],[0,0,0],[0,0,0]]
        block2 = [[0,0,0],[0,0,0],[0,0,0]]
        finished = [[0,0,0],[0,0,0],[0,0,0]]
        for i in range(0,3):
            for j in range(0,3):
                if self.block_win(flag,game,i,j):
                    finished[i][j]=1
                    final_score += 12
                elif self.block_win(('x' if flag == 'o' else 'o'),game,i,j):
                    finished[i][j]=2
                    final_score -= 12
                elif self.completed_block(game,i,j):
                    finished[i][j]=3
        flagop = ('x' if flag == 'o' else 'o')
        for i in range(0,3):
            for j in range(0,3):
                captured=0
                br = i * 3
                bc = j * 3
                for ii in range(0,3):
                    if (game[br+ii][bc+0]==flag or game[br+ii][bc+0]=='-') and (game[br+ii][bc+1]==flag or game[br+ii][bc+1]=='-')  and (game[br+ii][bc+2]==flag or game[br+ii][bc+2]=='-'):
                        if game[br+ii][bc+0]==flag:
                            captured += in1
                        if game[br+ii][bc+1]==flag:
                            captured += in1
                        if game[br+ii][bc+2]==flag:
                            captured += in1
                        if game[br+ii][bc+0]==flag and game[br+ii][bc+1]==flag:
                            captured += in2
                        if game[br+ii][bc+0]==flag and game[br+ii][bc+2]==flag:
                            captured += in2
                        if game[br+ii][bc+1]==flag and game[br+ii][bc+2]==flag:
                            captured += in2
                        if game[br+ii][bc+0]==flag and game[br+ii][bc+1]==flag and game[br+ii][bc+2]==flag:
                            captured += in3

                    elif (game[br+ii][bc+0]==flagop or game[br+ii][bc+0]=='-') and (game[br+ii][bc+1]==flagop or game[br+ii][bc+1]=='-') and (game[br+ii][bc+2]==flagop or game[br+ii][bc+2]=='-'):
                        if game[br+ii][bc+0]==flagop:
                            captured -= in1op
                        if game[br+ii][bc+1]==flagop:
                            captured -= in1op
                        if game[br+ii][bc+2]==flagop:
                            captured -= in1op
                        if game[br+ii][bc+0]==flagop and game[br+ii][bc+1]==flagop:
                            captured -= in2op
                        if game[br+ii][bc+0]==flagop and game[br+ii][bc+2]==flagop:
                            captured -= in2op
                        if game[br+ii][bc+1]==flagop and game[br+ii][bc+2]==flagop:
                            captured -= in2op
                        if game[br+ii][bc+0]==flagop and game[br+ii][bc+1]==flagop and game[br+ii][bc+2]==flagop:
                            captured -= in3op

                    if (game[br+0][bc+ii]==flag or game[br+0][bc+ii]=='-') and (game[br+1][bc+ii]==flag or game[br+1][bc+ii]=='-') and (game[br+2][bc+ii]==flag or game[br+2][bc+ii]=='-'):
                        if game[br+0][bc+ii]==flag:
                            captured += in1
                        if game[br+1][bc+ii]==flag:
                            captured += in1
                        if game[br+2][bc+ii]==flag:
                            captured += in1
                        if game[br+0][bc+ii]==flag and game[br+1][bc+ii]==flag:
                            captured += in2
                        if game[br+0][bc+ii]==flag and game[br+2][bc+ii]==flag:
                            captured += in2
                        if game[br+1][bc+ii]==flag and game[br+2][bc+ii]==flag:
                            captured += in2
                        if game[br+0][bc+ii]==flag and game[br+1][bc+ii]==flag and game[br+2][bc+ii]==flag:
                            captured += in3
                        
                    if (game[br+0][bc+ii]==flagop or game[br+0][bc+ii]=='-') and (game[br+1][bc+ii]==flagop or game[br+1][bc+ii]=='-') and (game[br+2][bc+ii]==flagop or game[br+2][bc+ii]=='-'):
                        if game[br+0][bc+ii]==flagop:
                            captured -= in1op
                        if game[br+1][bc+ii]==flagop:
                            captured -= in1op
                        if game[br+2][bc+ii]==flagop:
                            captured -= in1op
                        if game[br+0][bc+ii]==flagop and game[br+1][bc+ii]==flagop:
                            captured -= in2op
                        if game[br+0][bc+ii]==flagop and game[br+2][bc+ii]==flagop:
                            captured -= in2op
                        if game[br+1][bc+ii]==flagop and game[br+2][bc+ii]==flagop:
                            captured -= in2op
                        if game[br+0][bc+ii]==flagop and game[br+1][bc+ii]==flagop and game[br+2][bc+ii]==flagop:
                            captured -= in3op

                #DIAGONAL 1
                if (game[br+0][bc+0]==flag or game[br+0][bc+0]=='-') and (game[br+1][bc+1]==flag or game[br+1][bc+1]=='-') and (game[br+2][bc+2]==flag or game[br+2][bc+2]=='-'):
                    if game[br+0][bc+0]==flag:
                        captured += in1
                    if game[br+1][bc+1]==flag:
                        captured += in1
                    if game[br+2][bc+2]==flag:
                        captured += in1
                    if game[br+0][bc+0]==flag and game[br+1][bc+1]==flag:
                        captured += in2
                    if game[br+1][bc+1]==flag and game[br+2][bc+2]==flag:
                        captured += in2
                    if game[br+0][bc+0]==flag and game[br+2][bc+2]==flag:
                        captured += in2
                    if game[br+0][bc+0]==flag and game[br+1][bc+1]==flag and game[br+2][bc+2]==flag:
                        captured += in3

                if (game[br+0][bc+0]==flagop or game[br+0][bc+0]=='-') and (game[br+1][bc+1]==flagop or game[br+1][bc+1]=='-') and (game[br+2][bc+2]==flagop or game[br+2][bc+2]=='-'):
                    if game[br+0][bc+0]==flagop:
                        captured -= in1op
                    if game[br+1][bc+1]==flagop:
                        captured -= in1op
                    if game[br+2][bc+2]==flagop:
                        captured -= in1op
                    if game[br+0][bc+0]==flagop and game[br+1][bc+1]==flagop:
                        captured -= in2op
                    if game[br+1][bc+1]==flagop and game[br+2][bc+2]==flagop:
                        captured -= in2op
                    if game[br+0][bc+0]==flagop and game[br+2][bc+2]==flagop:
                        captured -= in2op
                    if game[br+0][bc+0]==flagop and game[br+1][bc+1]==flagop and game[br+2][bc+2]==flagop:
                        captured -= in3op

                #DIAGONAL 2
                if (game[br+2][bc+0]==flag or game[br+2][bc+0]=='-') and (game[br+1][bc+1]==flag or game[br+1][bc+1]=='-') and (game[br+0][bc+2]==flag or game[br+0][bc+2]=='-'):
                    if game[br+2][bc+0]==flag:
                        captured += in1
                    if game[br+1][bc+1]==flag:
                        captured += in1
                    if game[br+0][bc+2]==flag:
                        captured += in1
                    if game[br+2][bc+0]==flag and game[br+1][bc+1]==flag:
                        captured += in2
                    if game[br+1][bc+1]==flag and game[br+0][bc+2]==flag:
                        captured += in2
                    if game[br+2][bc+0]==flag and game[br+0][bc+2]==flag:
                        captured += in2
                    if game[br+2][bc+0]==flag and game[br+1][bc+1]==flag and game[br+0][bc+2]==flag:
                        captured += in3

                if (game[br+2][bc+0]==flagop or game[br+2][bc+0]=='-') and (game[br+1][bc+1]==flagop or game[br+1][bc+1]=='-') and (game[br+0][bc+2]==flagop or game[br+0][bc+2]=='-'):
                    if game[br+2][bc+0]==flagop:
                        captured -= in1op
                    if game[br+1][bc+1]==flagop:
                        captured -= in1op
                    if game[br+0][bc+2]==flagop:
                        captured -= in1op
                    if game[br+2][bc+0]==flagop and game[br+1][bc+1]==flagop:
                        captured -= in2op
                    if game[br+1][bc+1]==flagop and game[br+0][bc+2]==flagop:
                        captured -= in2op
                    if game[br+2][bc+0]==flagop and game[br+0][bc+2]==flagop:
                        captured -= in2op
                    if game[br+2][bc+0]==flagop and game[br+1][bc+1]==flagop and game[br+0][bc+2]==flagop:
                        captured -= in3op

                max_val = 24*in1 + 24*in2 + 8*in3
                block[i][j]=(captured*((1.0/depth)**(1.0/3.0)))*1.0/max_val + 1.0

        '''for iii in range(0,3):
            for jjj in range(0,3):
                print block[iii][jjj],
            print ''
        '''

        out1 = 1
        out2 = 1
        out3 = 1
        final_score = 0.0
        for i in range(0,3):
            if (finished[i][0]==1 or finished[i][0]==0) and (finished[i][1]==1 or finished[i][1]==0) and (finished[i][2]==1 or finished[i][2]==0):
            	final_score += out3*(block[i][0]*block[i][1]*block[i][2])

            elif (finished[i][0]==2 or finished[i][0]==0) and (finished[i][1]==2 or finished[i][1]==0)and (finished[i][2]==2 or finished[i][2]==0):
                final_score += out3*(block[i][0]*block[i][1]*block[i][2])
            else:
                final_score += out3*(1.0)

            if (finished[0][i]==1 or finished[0][i]==0) and (finished[1][i]==1 or finished[1][i]==0)and (finished[2][i]==1 or finished[2][i]==0):
            	final_score += out3*(block[0][i]*block[1][i]*block[2][i])
            
            elif (finished[0][i]==2 or finished[0][i]==0) and (finished[1][i]==2 or finished[1][i]==0)and (finished[2][i]==2 or finished[2][i]==0):
                final_score += out3*(block[0][i]*block[1][i]*block[2][i])
            else:
                final_score += out3*(1.0)
        #DIAGONAL 1

        if (finished[0][0]==1 or finished[0][0]==0) and (finished[1][1]==1 or finished[1][1]==0) and (finished[2][2]==1 or finished[2][2]==0):
       	    final_score += out3*(block[0][0]*block[1][1]*block[2][2])

        elif (finished[0][0]==2 or finished[0][0]==0) and (finished[1][1]==2 or finished[1][1]==0)and (finished[2][2]==2 or finished[2][2]==0):
            final_score += out3*(block[0][0]*block[1][1]*block[2][2])
        else:
            final_score += out3*(1.0)
        
        #DIAGONAL 2

        if (finished[2][0]==1 or finished[2][0]==0) and (finished[1][1]==1 or finished[1][1]==0) and (finished[0][2]==1 or finished[0][2]==0):
            final_score += out3*(block[2][0]*block[1][1]*block[0][2])

        elif (finished[2][0]==2 or finished[2][0]==0) and (finished[1][1]==2 or finished[1][1]==0)and (finished[0][2]==2 or finished[0][2]==0):
            final_score += out3*(block[2][0]*block[1][1]*block[0][2])
        else:
            final_score += out3*(1.0)

        return final_score

    def minimax(self,player,game,firstcall,depth,alpha,beta,selected_block,flag,maxdepth):

    	maxdepth = min(maxdepth,85-depth)

        #print self.assumedScore(game,depth,player,flag))
    	#return (0,0)

    	state_string = self.getStateString(game)
    	if state_string in self.visited and firstcall != 0:
    	    return self.visited[state_string]

        if time.clock() - self.t0 >=9 and firstcall != 0:
            self.complete = False
            return self.assumedScore(game,depth,player,flag)

        if alpha>=beta:
            if player==flag:
                #Parent is minimizer
                return 1000*self.INF
            else:
                #Parent is maximizer
                return -1000*self.INF
        #The game is complete (All blocks filled) or if there is a winner of the game, then return the heruistic based cost function values
        if self.board_win('o',game) or self.board_win('x',game) or self.completed_board(game) or depth>=maxdepth: 
            return self.assumedScore(game,depth,player,flag)

        scores = []
        moves = []
        copy = deepcopy(game)

        available=[[0,0,0],[0,0,0],[0,0,0]]
        if selected_block==0:
            if self.completed_block(copy,0,1) and self.completed_block(copy,1,0):
                selected_block=-1
            if not self.completed_block(copy,0,1):
                available[0][1]=1
            if not self.completed_block(copy,1,0):
                available[1][0]=1
        if selected_block==1:
            if self.completed_block(copy,0,2) and self.completed_block(copy,0,0):
                selected_block=-1
            if not self.completed_block(copy,0,2):
                available[0][2]=1
            if not self.completed_block(copy,0,0):
                available[0][0]=1
        if selected_block==2:
            if self.completed_block(copy,0,1) and self.completed_block(copy,1,2):
                selected_block=-1
            if not self.completed_block(copy,0,1):
                available[0][1]=1
            if not self.completed_block(copy,1,2):
                available[1][2]=1
        if selected_block==3:
            if self.completed_block(copy,0,0) and self.completed_block(copy,2,0):
                selected_block=-1
            if not self.completed_block(copy,0,0):
                available[0][0]=1
            if not self.completed_block(copy,2,0):
                available[2][0]=1
        if selected_block==4:
            if self.completed_block(copy,1,1):
                selected_block=-1
            if not self.completed_block(copy,1,1):
                available[1][1]=1
        if selected_block==5:
            if self.completed_block(copy,0,2) and self.completed_block(copy,2,2):
                selected_block=-1
            if not self.completed_block(copy,0,2):
                available[0][2]=1
            if not self.completed_block(copy,2,2):
                available[2][2]=1
        if selected_block==6:
            if self.completed_block(copy,1,0) and self.completed_block(copy,2,1):
                selected_block=-1
            if not self.completed_block(copy,1,0):
                available[1][0]=1
            if not self.completed_block(copy,2,1):
                available[2][1]=1
        if selected_block==7:
            if self.completed_block(copy,2,0) and self.completed_block(copy,2,2):
                selected_block=-1
            if not self.completed_block(copy,2,0):
                available[2][0]=1
            if not self.completed_block(copy,2,2):
                available[2][2]=1
        if selected_block==8:
            if self.completed_block(copy,1,2) and self.completed_block(copy,2,1):
                selected_block=-1
            if not self.completed_block(copy,1,2):
                available[1][2]=1
            if not self.completed_block(copy,2,1):
                available[2][1]=1
        if selected_block==-1: #Any move allowed
            for i in range(0,3):
                for j in range(0,3):
                    if not self.completed_block(copy,i,j):
                        available[i][j]=1
      
        alphatemp = deepcopy(alpha)
        betatemp = deepcopy(beta)
 
        for i in range(0,9):
            for j in range(0,9):
                if copy[i][j]=='-' and available[i/3][j/3]==1:
                    copy[i][j]=player
                    if player==flag:
                        cur_score = self.minimax(('x' if player == 'o' else 'o'),copy,1,depth+1,alphatemp,betatemp,(i%3)*3+j%3,flag,maxdepth)
                        scores.append(cur_score)
                        alphatemp = max(alphatemp, cur_score)
                    else:
                        cur_score = self.minimax(('x' if player == 'o' else 'o'),copy,1,depth+1,alphatemp,betatemp,(i%3)*3+j%3,flag,maxdepth)
                        scores.append(cur_score)
                        betatemp = min(betatemp, cur_score)
                    copy[i][j]='-'
                    moves.append((i)*10+(j))


        #If we are playing
        if player==flag:
            max_score_index = scores.index(max(scores))
            j=(moves[max_score_index])%10
            i=(moves[max_score_index]/10)%10
            copy[i][j] = player
            state_string = self.getStateString(copy)
            self.visited[state_string] = scores[max_score_index]
            copy[i][j] = '-'
            if firstcall==0:
                return (int(i),int(j))
            return scores[max_score_index]
        else:
            min_score_index = scores.index(min(scores))
            j=(moves[min_score_index])%10
            i=(moves[min_score_index]/10)%10
            copy[i][j] = player
            state_string = self.getStateString(copy)
            self.visited[state_string] = scores[min_score_index]
            copy[i][j] = '-'
            if firstcall==0:
                return (int(i),int(j))
            return scores[min_score_index]

    def getStateString(self, temp_board):
    	ret_string = ''
    	for i in range(0,9):
    		for j in range(0,9):
    			if temp_board[i][j] == 'o':
    				ret_string += '1'
    			elif temp_board[i][j] == 'x':
    				ret_string += '2'
    			elif temp_board[i][j] == '-':
    				ret_string += '0'
    	return ret_string

    def move(self, temp_board, temp_block, old_move, flag):
        self.__init__()
        self.t0 = time.clock()
        previous_move_r, previous_move_c = old_move[0], old_move[1]
    	if previous_move_c==-1 and previous_move_r==-1:
    	    selected_block=-1
    	else:
    	    selected_block = ((previous_move_c)%3+((previous_move_r)%3)*3) #x is the column y is the row
        self.complete = True
        answer = self.minimax(flag,temp_board,0,1,-self.INF,self.INF,selected_block,flag,5)
        t1 = time.clock()
        return answer
        max_depth = 5
        while t1-self.t0 <= 8:
            self.complete = True
            answer1 = self.minimax(flag,temp_board,0,1,-self.INF,self.INF,selected_block,flag,max_depth)
            if self.complete == True:
                answer = answer1
                max_depth += 1
                t1 = time.clock()
            else:
                break
        return answer

