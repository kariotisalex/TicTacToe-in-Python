from Supporter import Supporter
if __name__ == '__main__':
    print('Welcome in Tic Tac Toe\n')
    print('how to play:')
    print('This game is multiplayer game\nChoose your character and which player are you, player 1 or player 2')
print("game choose randomly who's going to start first")
print('every number of the numpad is one cell')
print('the map of the numpad is like this')
d = ["$",'1','2','3','4','5','6','7','8','9']
Supporter.display_board(d)
import os
repeater = True
while repeater:

    #Create the list of gameplay
    board = ['#']+[" "]*9

    #Choose X or O for each player
    (player1, player2) =  Supporter.player_input()
    
    #Choose who is going to start first
    holder = Supporter.choose_first()
    if holder == 1:
        players_turn_flag = True
    else:
        players_turn_flag = False

    Supporter.display_board(board)
    while True:
            # Player 1 plays
            if players_turn_flag == True:
                print(f'\n Turn of Player 1: {player1}\n')
                nc1 = Supporter.player_choice(board)
                Supporter.place_marker(board,player1,nc1)
                os.system('cls')
                Supporter.display_board(board)
                if (Supporter.win_check(board,player1) == True):
                    print("Player 1 wins")
                    break
                if (Supporter.full_board_check(board) == True):
                    print("Tie game!")
                    break
                players_turn_flag = False
            # Player 2 plays
            if players_turn_flag == False:
                print(f'\nTurn of player 2: {player2}\n')
                nc2 = Supporter.player_choice(board)
                Supporter.place_marker(board,player2,nc2)
                os.system('cls')
                Supporter.display_board(board)
                if (Supporter.win_check(board,player2) == True):
                    print("Player 2 wins")
                    break
                if (Supporter.full_board_check(board) == True):
                    print("Tie game!")
                    break
                players_turn_flag = True
    repeater = Supporter.replay()
print("thank you for playing my first game")


