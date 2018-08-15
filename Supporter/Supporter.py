def display_board(board):
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-|-|-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-|-|-')
    print(board[1] + '|' + board[2] + '|' + board[3])

#Select Player's character
def player_input():
    marker = ""
    while marker.upper() != 'X' and marker.upper() != 'O':
        marker = input('Player 1, choose X or O: ')

    player1 = marker.upper()

    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'
        
    print(f"Player 1: {player1}, Player 2: {player2}")
    return (player1,player2)


#Checks if player wins
def win_check(board, mark):
    
    if (mark in board[1]) and (mark in board[2]) and (mark in board[3]):
        return True
    elif (mark in board[4]) and (mark in board[5]) and (mark in board[6]):
        return True
    elif (mark in board[7]) and (mark in board[8]) and (mark in board[9]):
        return True
    elif (mark in board[1]) and (mark in board[4]) and (mark in board[7]):
        return True
    elif (mark in board[2]) and (mark in board[5]) and (mark in board[8]):
        return True
    elif (mark in board[3]) and (mark in board[6]) and (mark in board[9]):
        return True
    elif (mark in board[1]) and (mark in board[5]) and (mark in board[9]):
        return True
    elif (mark in board[7]) and (mark in board[5]) and (mark in board[3]):
        return True
    else:
        return False

#Random choise which player starts first
from random import randint
def choose_first():
    pick = randint(1,2)
    print(f'\nFirst going to start Player {pick}\n')
    return pick


#Check if board is full
def full_board_check(board):
    for i in board[1:]:
        if i == " ":
            return False
    return True

#Check if the selected position in the list is empty {embedded in method player_choice(board)}
def space_check(board, position):
    return(board[position] == " ")
    
#Next player's move
def player_choice(board):
    next_choise = 0
    while (next_choise < 1 or next_choise > 9):
        try:
            next_choise = int(input("make your next move: \n"))
        except:
            print('Try to give a acceptable number from 1 to 9')
    if space_check(board,next_choise) == False:
        print(f'The place {next_choise} is full, try another one')
        return player_choice(board)
    return next_choise

#Place the choise
def place_marker(board, marker, position):
    board[position] = marker
    
#Replay the whole game
def replay():
    while True:
        replay_flag = input("Do you want to play again? Yes or No ")
        if (replay_flag.lower() == 'yes' or replay_flag.lower() == 'y'):
            return True
        elif (replay_flag.lower() == 'no' or replay_flag.lower() == 'n'):
            return False
        print("Try again")