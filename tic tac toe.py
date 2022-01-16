
def dislpay_board(board):
    print(' ' + board[7] + '|' + board[8] + '|' + board[9])
    print('--------')
    print(' ' + board[4] + '|' + board[5] + '|' + board[6])
    print('--------')
    print(' ' + board[1] + '|' + board[2] + '|' + board[3])

def player_input():
    marker= ''
    while not (marker =='X' and marker =='O'):
        marker=input('Player1,Choose either X or O:')
        
        if marker =='X' or marker == 'x':
            return("X","O")  
        else:
            return("o","x")
def place_marker(board,marker,position):
    if position not in [1,2,3,4,5,6,7,8,9]:
        print("SORRY!! It's a wrong input")
    else:
        board[position]= marker    

def win_check(board,mark):
    return((board[7]==board[8]==board[9]==mark) or (board[4]==board[5]==board[6]==mark) or (board[1]==board[2]==board[3]==mark) or (board[7]==board[5]==board[3]==mark) or (board[1]==board[5]==board[9]==mark) or (board[7]==board[4]==board[1]==mark) or (board[8]==board[5]==board[2]==mark) or  (board[9]==board[6]==board[3]==mark))


import random

def choose_first():
    flip = random.randint(0,1)
    if flip == 0:
        return "player1"
    else:
        return "player2"

def space_check(board,position):
    return board[position] == ' '

def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False

    return True

def player_choice(board):
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position = int(input('Choose a pos:(1-9)'))
    return position

def replay():
    choice=input("WANNA PLAY AGAIN? ENTER YES OR NO:")
    return choice=='YES' or choice=='yes'


print("WELCOME TO TIC TAC TOE!!")

while True:

    the_board = [' ']*10
    player_1marker,player_2marker = player_input()

    turn = choose_first()
    print(turn + ' will go first')
    
    play_game=input('Ready to play??? YES or NO?')
    if play_game=='yes' or play_game== 'YES':
        game_on=True
    else:
        game_on=False

    while game_on:
        if (turn == 'player1'):

            dislpay_board(the_board)
            position = player_choice(the_board)
            place_marker(the_board,player_1marker,position)

            if win_check(the_board,player_1marker):
                dislpay_board(the_board)
                print("PLAYER1 HAS WON!!!")
                game_on=False
            
            else:
                if full_board_check(the_board):
                    dislpay_board(the_board)
                    print("TIE GAME!!!")
                    game_on=False
                
                else:

                    turn ='player2'
        else:
            dislpay_board(the_board)
            position=player_choice(the_board)
            place_marker(the_board,player_2marker,position)

            if win_check(the_board,player_2marker):
                dislpay_board(the_board)
                print("PLAYER2 HAS WON!!!")
                game_on=False
            else:
                if full_board_check(the_board):
                    dislpay_board(the_board)
                    print("TIE GAME!!!")
                    game_on=False
                else:
                    turn='player1'

    if not replay():
        break



