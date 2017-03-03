Script started on Friday 03 March 2017 03:51:55 PM IST
]0;nikita@vampire: ~/AI[01;32mnikita@vampire[00m:[01;34m~/AI[00m$ sh toi[Kurnament.sh 
tournament.sh: 3: tournament.sh: Syntax error: "(" unexpected
]0;nikita@vampire: ~/AI[01;32mnikita@vampire[00m:[01;34m~/AI[00m$ sh tournament.sh 
hello
]0;nikita@vampire: ~/AI[01;32mnikita@vampire[00m:[01;34m~/AI[00m$ sh tournament.sh 
hello
tournament.sh: 6: tournament.sh: i++: not found
]0;nikita@vampire: ~/AI[01;32mnikita@vampire[00m:[01;34m~/AI[00m$ sh tournament.sh 
hello
]0;nikita@vampire: ~/AI[01;32mnikita@vampire[00m:[01;34m~/AI[00m$ sh tournament.sh 
seq 1 to 3
]0;nikita@vampire: ~/AI[01;32mnikita@vampire[00m:[01;34m~/AI[00m$ sh tournament.sh 
seq
1
to
3
]0;nikita@vampire: ~/AI[01;32mnikita@vampire[00m:[01;34m~/AI[00m$ sh tournament.sh 
tournament.sh: 3: tournament.sh: Syntax error: "(" unexpected
]0;nikita@vampire: ~/AI[01;32mnikita@vampire[00m:[01;34m~/AI[00m$ sh tournament.sh 
{1..3}
]0;nikita@vampire: ~/AI[01;32mnikita@vampire[00m:[01;34m~/AI[00m$ sh tournament.sh 
1
2
3
]0;nikita@vampire: ~/AI[01;32mnikita@vampire[00m:[01;34m~/AI[00m$ touch results.txt
]0;nikita@vampire: ~/AI[01;32mnikita@vampire[00m:[01;34m~/AI[00m$ ls
[0m[01;32ma.out[0m    input          simulator.py           tournament.sh
bot.py   obstacles.cpp  simulator.pyc          [01;34mUltimateTicTacToeBot-master[0m
bot.pyc  results.txt    tic-tac-toe-geeks.cpp
]0;nikita@vampire: ~/AI[01;32mnikita@vampire[00m:[01;34m~/AI[00m$ bash[K[K[K[Ksh tournament.sh 
tournament.sh: 5: tournament.sh: pyhton: not found
tournament.sh: 5: tournament.sh: pyhton: not found
tournament.sh: 5: tournament.sh: pyhton: not found
tournament.sh: 5: tournament.sh: pyhton: not found
tournament.sh: 5: tournament.sh: pyhton: not found
tournament.sh: 5: tournament.sh: pyhton: not found
tournament.sh: 5: tournament.sh: pyhton: not found
]0;nikita@vampire: ~/AI[01;32mnikita@vampire[00m:[01;34m~/AI[00m$ sh tournament.sh 
	^CTraceback (most recent call last):
  File "simulator.py", line 326, in <module>
    x = gameplay(obj1, obj2)
  File "simulator.py", line 189, in gameplay
    p1_move = obj1.move(game_board, old_move, fl1)
  File "/home/nikita/AI/bot.py", line 449, in move
    next_move, optimal=self.minimax(board, old_move, isMax, -1000, 1000, 1, self.block_value)
  File "/home/nikita/AI/bot.py", line 388, in minimax
    proposed_move, value  = self.minimax(board, cell, False, alpha, beta, depth+1, block_value)
  File "/home/nikita/AI/bot.py", line 420, in minimax
    proposed_move, value  = self.minimax(board, cell, True, alpha, beta, depth + 1, block_value)
  File "/home/nikita/AI/bot.py", line 388, in minimax
    proposed_move, value  = self.minimax(board, cell, False, alpha, beta, depth+1, block_value)
  File "/home/nikita/AI/bot.py", line 420, in minimax
    proposed_move, value  = self.minimax(board, cell, True, alpha, beta, depth + 1, block_value)
  File "/home/nikita/AI/bot.py", line 362, in minimax
    state_value, block_value = self.calculate_value(board,old_move, block_value)
  File "/home/nikita/AI/bot.py", line 336, in calculate_value
    if block_value[0][3]<-1*br1 or block_value[1][2]<-1*br1 or block_value[2][1]<-1*br1 or block_value[3][0]<-1*br1:
KeyboardInterrupt

]0;nikita@vampire: ~/AI[01;32mnikita@vampire[00m:[01;34m~/AI[00m$ sh tournament.sh 
]0;nikita@vampire: ~/AI[01;32mnikita@vampire[00m:[01;34m~/AI[00m$ exit
exit

Script done on Friday 03 March 2017 07:30:23 PM IST
