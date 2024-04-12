#!/usr/bin/env python3

import sys
import os

#
# ==========
#
def print_board(board: list):

    print('\n')
    print('\t     |     |')
    print('\t  {}  |  {}  |  {}'.format(board[0], board[1], board[2]))
    print('\t_____|_____|_____')
 
    print('\t     |     |')
    print('\t  {}  |  {}  |  {}'.format(board[3], board[4], board[5]))
    print('\t_____|_____|_____')
 
    print('\t     |     |')
 
    print('\t  {}  |  {}  |  {}'.format(board[6], board[7], board[8]))
    print('\t     |     |')
    print('\n')


#
# ==========
#
def check_for_winner(moves: list, current_player: str) -> bool:

	winning_moves = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
	for win in winning_moves:
		if all(move in moves[current_player] for move in win):
			return True
	return False       

#
# ==========
#
def check_for_draw(moves: list) -> bool:
	if (len(moves['X']) + len(moves['O']) == 9):
		return True
	return False

#
# ==========
#
def main() -> int:

	# setup a blank board
	board = [x+1 for x in range(9)]

	print('\n')
	player1 = input('Choose a board piece for player 1 (\'X\' or \'O\'): ')
	player1 = player1.upper()
	if player1 == 'X':
		player2 = 'O'
	else:
		player2 = 'X'
	print('Player 1: {}, Player 2: {}'.format(player1, player2))

	moves = {
		player1 : [],
		player2 : []
	}

	print_board(board=board)

	current_player = player1

	while (True):

		print('\n')

		try:
			print('Player \'', current_player, '\' turn. Which box (\'0\' to end game)? : ', end='')
			move = int(input()) 
		except ValueError:
			print('Invalid box. Try again...')
			continue
 
		if move == 0:
 			break

		if move < 1 or move > 9:
			print('Invalid box. Try again...')
			continue

		if (move in moves[player1]) or (move in moves[player2]):
			print('Box occupied. Try again...')
			continue

		moves[current_player].append(move)

		board[move - 1] = current_player

		print_board(board=board)

		if (check_for_winner(moves=moves, current_player=current_player)):
			print('Player \'', current_player, '\' is the winner!')
			break
		
		if (check_for_draw(moves=moves)):
			print('Game is a draw!')
			break

		if current_player == 'X':
			current_player = 'O'
		else:	
			current_player = 'X'

	print('\n')
	
	return 0

#
# ==========
#
if __name__ == "__main__":
	sys.exit(main())