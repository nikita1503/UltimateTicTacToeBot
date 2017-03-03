def test(game,flag):
    in1 = 1
    in2 = 10
    in3 = 100
    in1op = 1
    in2op = 10
    in3op = 100
    if flag == 'x':
        flagop = 'o'
    else:
        flagop = 'x'
    captured=0
    br = 0
    bc = 0
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
        if (game[br+ii][bc+0]==flagop or game[br+ii][bc+0]=='-') and (game[br+ii][bc+1]==flagop or game[br+ii][bc+1]=='-') and (game[br+ii][bc+2]==flagop or game[br+ii][bc+2]=='-'):
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

    print captured


test([
    ['x','x','x'],
    ['x','x','x'],
    ['x','x','x'],
    ],
    'x')
