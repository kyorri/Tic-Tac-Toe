# Created by mariand
# https://github.com/kyorri

import os
import random

board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
def print_board(board):
    '''This function will print the board contents on the screen'''
    print()
    for i in range(0, 3):
        print(' ', end=' ')
        for j in range(0, 3):
            print(f'{board[i * 3 + j]}', end=' ')
        print()
    print()

def place_logic(board, turn):
    '''This function will make sure the user enters a valid input, by placing his X or O on the board correctly!'''
    # Empty cells would be the board elements that are whole numbers.
    prompt = f'Choose the empty cell you want to place \'{turn}\' on. (1-9): '
    choice_made = False
    while (not choice_made):
        choice = int(input(prompt))
        if (choice in board):
            board[choice - 1] = turn
            choice_made = True
        else:
            os.system('cls')
            print_board(board)
            print(
                f'Wrong input!\n\tTry inputting the number cell that was not chosen for your \'{turn}\'! (1-9): ')

def check_draw(board):
    draw_condition = True
    # Empty cells would be the board elements that are whole numbers.
    # If there are no empty cells, the game will call for a draw!
    for i in range(1, 10):
        if (i in board):
            draw_condition = False
            return draw_condition
    return draw_condition

def check_win(board):
    win_coordinates = [
                        [0, 1, 2],
                        [3, 4, 5],
                        [6, 7, 8],
                        [0, 3, 6],
                        [1, 4, 7],
                        [2, 5, 8],
                        [0, 4, 8],
                        [2, 4, 6]
                        ]
    for win in win_coordinates:
        if (board[win[0]] == board[win[1]] and board[win[1]] == board[win[2]]):
            return board[win[0]]
    return False


def game():
    """
    This function will start the game up and will manage the player turns.
    """
    # The starting player will have a random letter. (X or O)
    players = ['X', 'O']
    turn = random.choice(players)

    end_game = False
    while (not end_game):
        os.system('cls')
        win_condition = check_win(board)
        draw_condition = check_draw(board)
        # The win or draw checks.
        if (win_condition != False):
            # We have found the winner, and we will end the game!
            print_board(board)
            print(f'The winner is \'{win_condition}\'')
            end_game = True
            continue
        if (draw_condition):
            # If the game had all of the places on the board chosen, 
            # and there were no win conditions, we will declare a draw.
            print_board(board)
            print('There is a draw!\n')
            end_game = True
            continue
        # Here we will place the player's choice on the board.
        print_board(board)
        place_logic(board, turn)
        # We will change to the other player's turn
        if (turn == 'X'):
            turn = 'O'
        elif (turn == 'O'):
            turn = 'X'

game()
print(f'Thanks for playing, {os.getlogin()}!\n')
os.system("pause")
