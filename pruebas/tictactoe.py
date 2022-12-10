from IPython.display import clear_output

row1 =[' ', ' ',' ']
row2 =[' ', ' ',' ']
row3 =[' ', ' ',' ']
board = [row1,row2,row3]
moves = (1,2,3,4,5,6,7,8,9)
dict_moves = {1:(2,0),2:(2,1),3:(2,2),4:(1,0),5:(1,1),6:(1,2),7:(0,0),8:(0,1),9:(0,2)}

def init_game():
    choice = 'wrong'

    while choice not in ['Y','N']:
        clear_output()
        choice = input('Do you want to play a game? (Y/N):')
        if choice not in ['Y','N']:
            print("Don't waste my time. Do you want to play or not? (Y/N):")
    
    return choice == 'Y'

def display_board():
    for n in board:
        print(n[0]+'|'+n[1]+'|'+n[2])

def init_players():
    choice = 'wrong'
    choices = ['X','O']
    while choice not in choices:
        clear_output()
        choice = input('Player 1. Choose X or O:')
        if choice not in choices:
            print('Please Player 1, choose from X or O.')
    
    player1 = choice
    choices.remove(choice)
    player2 = choices[0]
    print('Player 1: '+ player1)
    print('Player 2: '+ player2)
    return {'1':player1,'2':player2}

def check_win(board):
    #horizontal win
    for row in board:        
        if row[0]==row[1]==row[2]:
            if row[0]!=' ':
                return row[0]

    #vertical win
    for col in range(0,3):        
        if board[0][col]==board[1][col]==board[2][col]:
            if board[0][col]!=' ':
                return board[0][col]
    
    #diagonal win
    if board[0][0]==board[1][1]==board[2][2] or board[0][2]==board[1][1]==board[2][0]:
        if board[1][1]!=' ':
            return board[1][1]
    
    #no win yet
    return 'N'

def check_move(move,board):
    if move not in moves:
        return False
    
    x=dict_moves[move][0]
    y=dict_moves[move][1]

    if board[x][y] != ' ':
        return False
    else:
        return True

def game_on(dict_players,board):
    turn = '1'
    next_turn = False
    while check_win() == 'N':
        while not next_turn:
            move = input('Player '+turn+" it's your turn (0/9):")
            next_turn = False    
            if not check_move(move,board):
                clear_output()
                print('Player '+turn+' , stop being silly.')
            else:
                #update board
                x=dict_moves[move][0]
                y=dict_moves[move][1]
                board[x][y] = dict_players[turn]  
                #alternate turns              
                if turn == '1':
                    turn = '2'
                else:
                    turn = '1'
                next_turn = True

if init_game():
    dict_players = init_players()
    print(dict_players)
    display_board()
    game_on(dict_players)
else:
    print('See you later') 
