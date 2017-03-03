from games import check
#from bl import *


#b = [['x','o','-','o','-','-','o','-','-'],['x','o','-','-','x','-','-','x','o'],['o','x','-','-','-','-','x','o','-'],['o','o','-','x','x','-','-','x','x'],['-','-','x','x','o','-','x','x','x'],['o','x','-','-','-','-','o','o','-'],['x','o','-','o','o','-','x','-','x'],['o','x','-','-','-','x','o','-','x'],['x','x','-','-','-','x','x','x','-']]

#p_block = ['-']*9

"""b = [['-','-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-','-'],['-','-','-','x','-','-','-','-','-'],['-','-','-','-','-','-','-','-','-'],['-','-','o','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-','-'],['-','-','-','-','-','x','-','-','-'],['-','-','-','o','x','x','o','o','x']]"""

"""b = [['-','-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-','-'],['-','-','-','x','-','-','-','-','-'],['-','-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-','-']]"""


def minimax(node, depth, alpha, beta, maxnode, p_board, p_block, flag1, flag2, best_row, best_col):
	
	if depth==0:
		utility = check(p_board,p_block)
		if flag1 == 'o':
			return (-utility,best_row,best_col)
		
		return (utility,best_row,best_col)
	else:
		children_list = compute_cells(p_board,p_block,node)
		for child in children_list:
			if maxnode:
				p_board[child[0]][child[1]] = flag1
			else:
				p_board[child[0]][child[1]] = flag2
			if maxnode:
				score = minimax (child,depth-1,alpha,beta,False,p_board,p_block,flag1,flag2,best_row,best_col)
				if (score[0] > alpha):
	        	          alpha = score[0]
	        	          best_row = child[0]
	        	          best_col = child[1]
			else:
				score = minimax (child,depth-1,alpha,beta,True,p_board,p_block,flag1,flag2,best_row,best_col)
				if (score[0] < beta):
	        	          beta = score[0]
	        	          best_row = child[0]
	        	          best_col = child[1]
			p_board[child[0]][child[1]] = '-'
			if (alpha >= beta):
				 break
		if maxnode:
			return (alpha, best_row, best_col)
		else:
			return(beta, best_row, best_col)

def mminimax(node, depth, mini, maxi, maxnode, p_board, p_block, flag1, flag2, best_row, best_col):
	#global best_row, best_col
	if depth==0:
		p_board[node[0]][node[1]] = flag2
		utility = check(p_board,p_block)
		#print p_board
		p_board[node[0]][node[1]] = '-'
		
		#print 'utility = ' + str(utility)
		if flag1 == 'o':
			return (-utility,best_row,best_col)
		
		return (utility,best_row,best_col)
	if maxnode:
		v = mini
                #print 'v =' + str(v) 
		p_board[node[0]][node[1]] = flag2
		#print p_board
		children_list = compute_cells(p_board,p_block,node)
		#print node
                #print children_list
		for child in children_list:
			v1 = minimax (child,depth-1,v,maxi,False,p_board,p_block,flag1,flag2,best_row,best_col)
			print 'max', maxi
			if(depth != 4):
				p_board[node[0]][node[1]] = '-'
			#print 'v1 = ' + str(v1)
			if (v1[0] >= v):
				v = v1[0]
				best_row = child[0]
				best_col = child[1]
                                		
			if (v >= maxi): 
				return (maxi,best_row,best_col)
		return (v,best_row,best_col)
	
	else:
		v = maxi
		p_board[node[0]][node[1]] = flag1
		#print p_board
		#print 'min',                
		#print node
		children_list = compute_cells(p_board,p_block,node)
		#print children_list
		for child in children_list:
        		v1 = minimax (child,depth-1,mini,v,True,p_board,p_block,flag1,flag2,best_row,best_col)
			print 'min',mini                        
			p_board[node[0]][node[1]] = '-'
			#print 'v1 = ' + str(v1)
        		if (v1[0] <= v): 
				v = v1[0]
				best_row = child[0]
				best_col = child[1]
        		if (v <= mini): 
				return (mini,best_row,best_col)
        	return (v,best_row,best_col)

def compute_cells(p_board,p_block,old_move):
		
		
		for_corner = [0,2,3,5,6,8]
		if(old_move == (-1,-1)):
			blocks_allowed = [0,1,2,3,4,5,6,7,8]
		#List of permitted blocks, based on old move.
		else:
			blocks_allowed  = []

			if old_move[0] in for_corner and old_move[1] in for_corner:
				## we will have 3 representative blocks, to choose from

				if old_move[0] % 3 == 0 and old_move[1] % 3 == 0:
					## top left 3 blocks are allowed
					blocks_allowed = [0, 1, 3]
				elif old_move[0] % 3 == 0 and old_move[1] in [2, 5, 8]:
					## top right 3 blocks are allowed
					blocks_allowed = [1,2,5]
				elif old_move[0] in [2,5, 8] and old_move[1] % 3 == 0:
					## bottom left 3 blocks are allowed
					blocks_allowed  = [3,6,7]
				elif old_move[0] in [2,5,8] and old_move[1] in [2,5,8]:
					### bottom right 3 blocks are allowed
					blocks_allowed = [5,7,8]
				else:
					print "SOMETHING REALLY WEIRD HAPPENED!"
					sys.exit(1)
			else:
			#### we will have only 1 block to choose from (or maybe NONE of them, which calls for a free move)
				if old_move[0] % 3 == 0 and old_move[1] in [1,4,7]:
					## upper-center block
					blocks_allowed = [1]
	
				elif old_move[0] in [1,4,7] and old_move[1] % 3 == 0:
					## middle-left block
					blocks_allowed = [3]
		
				elif old_move[0] in [2,5,8] and old_move[1] in [1,4,7]:
					## lower-center block
					blocks_allowed = [7]

				elif old_move[0] in [1,4,7] and old_move[1] in [2,5,8]:
					## middle-right block
					blocks_allowed = [5]
				elif old_move[0] in [1,4,7] and old_move[1] in [1,4,7]:
					blocks_allowed = [4]

                for i in reversed(blocks_allowed):
                    if p_block[i] != '-':
                        blocks_allowed.remove(i)
	# We get all the empty cells in allowed blocks. If they're all full, we get all the empty cells in the entire board.
		cells = get_empty_out_of(p_board, blocks_allowed,p_block)
		return cells

def get_empty_out_of(gameb, blal,block_stat):
	cells = []  # it will be list of tuples
	#Iterate over possible blocks and get empty cells
	for idb in blal:
	        if(block_stat[idb] == '-'):
			id1 = idb/3
			id2 = idb%3
			for i in range(id1*3,id1*3+3):
				for j in range(id2*3,id2*3+3):
					if gameb[i][j] == '-':
						cells.append((i,j))

	# If all the possible blocks are full, you can move anywhere
	if cells == []:
		for i in range(9):
			for j in range(9):
                                no = (i/3)*3
                                no += (j/3)
				if gameb[i][j] == '-' and block_stat[no] == '-':
					cells.append((i,j))	
	return cells

"""a =minimax((5,2),4,-1000,1000,True,b[:],p_block,'x','o',-1,-1)
print 'move' , a"""

