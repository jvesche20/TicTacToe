#Jacob Vesche
#TicTacToe.py
# Final project
# 4-19-2020
#"I have neither given nor received unauthorized aid in completing this work, 
#nor have I presented someone else's work as my own."
#player plays against a bot that picks a random corner and tried to beat it. 
# https://stackoverflow.com/questions/27276135/python-random-system-time-seed
# https://www.w3schools.com/python/python_try_except.asp
import time
import random 
from random import seed
from random import randint
import logging


logging.basicConfig(filename ='C:/Users/Jacob/pythonclass/log/jacob.log', level = logging.INFO, format = '%(asctime)s %(message)s', filemode = 'w')

logger = logging.getLogger()




board = { '1':' ', '2':' ', '3':' ', '4':' ', '5':' ', '6':' ', '7':' ', '8':' ', '9':' '}
playAgain = 'y'

# prints the board on the screen. 
def printBoard(theBoard):
	print(theBoard['1'] + '|' + board['2'] + '|' + board['3'])
	print ('-+-+-')
	print(theBoard['4'] + '|' + board['5'] + '|' + board['6'])
	print ('-+-+-')
	print(theBoard['7'] + '|' + board['8'] + '|' + board['9'])
	

# def that starts the game. 
def game():
	logger.info('Game Started')
	random.seed(time.time())

	count = 0
	#value = randint(0,1)
	
	print("The board goes as follows:")
	print("1|2|3")
	print("-+-+-")
	print("4|5|6")
	print("-+-+-")
	print("7|8|9")
	
	
	print("The numbers are where you are to place your move.")

	# keeps going till the board is filled up.
	for i in range(100):
		
		if(count == 0):
			printBoard(board)
			print ("Player goes first. You are X, bot is O")
			print("Where would you like to go?")
			
			while True:
				

				location = input()
			
				try:
					location = int(location)
				except ValueError:
					logger.error("Error enter correct value")
					print ("Error enter correct value")
					continue
				if (0 < location < 10):
					break
				else:
					logger.error("Error enter correct value")
					print("Enter a valid range")
			
			turn = 'X'
			location = str(location)
		if(turn == 'O'):
			botTurn = randint(1,9)
			botStr = str(botTurn)
			
			if (board[botStr] == ' '):
				board[botStr] = turn
				count += 1
			
			
			else:
				continue
				
		else:
			location = str(location)
			if(count != 0):
				printBoard(board)
				print("Your turn!")
				while True:
					location = input()
			
					try:
						location = int(location)
					except ValueError:
						logger.error("Error enter correct value")
						print ("Error enter correct value")
						continue
					if (0 < location < 10):
						break
					else:
						logger.error("Error enter correct value")
						print("Enter a valid range")
				
				location = str(location)
				
			if (board[location] == ' '):
				board[location] = turn
				count += 1
			
			
			else:
				print("That spot is already in use. Please try again!")
				continue

		#1 2 3
		#4 5 6
		#7 8 9
		# checking to see if there is a winner. Cant win unless there is at least 5 turns.
		if (count >= 5):
			if (board['1'] == board['2'] == board['3'] != ' '):
				printBoard(board)
				print(turn + " won!")
				logger.info('%s won!', turn)
				break
			elif(board['1'] == board['4'] == board['7'] != ' '):
				printBoard(board)
				print(turn + " won!")
				logger.info('%s won!', turn)
				break
			elif(board['1'] == board['5'] == board['9'] != ' '):
				printBoard(board)
				print(turn + " won!")
				logger.info('%s won!', turn)
				break
			elif(board['2'] == board['5'] == board['8'] != ' '):
				printBoard(board)
				print(turn + " won!")
				logger.info('%s won!', turn)
				break
			elif(board['4'] == board['5'] == board['6'] != ' '):
				printBoard(board)
				print(turn + " won!")
				logger.info('%s won!', turn)
				break
			elif(board['3'] == board['6'] == board['9'] != ' '):
				printBoard(board)
				print(turn + " won!")
				logger.info('%s won!', turn)
				break
			elif(board['7'] == board['8'] == board['9'] != ' '):
				printBoard(board)
				print(turn + " won!")
				logger.info('%s won!', turn)
				break
			elif(board['3'] == board['5'] == board['7'] != ' '):
				printBoard(board)
				print(turn + " won!")
				logger.info('%s won!', turn)
				break
		if (count == 9):
		
			printBoard(board)
			print("Tie!")
			logger.info('Tied!')
			
		if (turn == 'X'):
			turn = 'O'
			
		else:
			turn = 'X'

		
		print('\n\n')
		
# asking the user if they want to play again. 
while(playAgain == 'y'):
	game()
	print ("Would you like to play again (Y or N)?")
	playAgain = input()
	
	playAgain = playAgain.casefold()
	if (playAgain == 'y'):
		logger.info('New Game started.')
	# clearing the board for the next game. 
	board = { '1':' ', '2':' ', '3':' ', '4':' ', '5':' ', '6':' ', '7':' ', '8':' ', '9':' '}
