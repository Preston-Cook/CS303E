######################################################################
#                                                                    #
#                       Project 2: Tic Tac Toe                       #
#                                                                    #
######################################################################

"""This sets up a TicTacToe class. The basic structure is a two
dimensional representation of the 3x3 board.  Each location is
occupied by a token which is one of: " ", "X", "O".

In our very simple initial version, the user always goes first as X
and the program plays the opponent as O.  The opponent just makes a
random move."""

import random

# Some global constants:

HUMAN   = 0
MACHINE = 1

# Probably some other constants here:

initialBoard = [ [" ", " ", " "], 
                 [" ", " ", " "], 
                 [" ", " ", " "] ]

WELCOME = 'Welcome to Tic-Tac-Toe! Let\'s play!'
YOU_WON = 'YOU WON AGAINST THE MACHINE!'
YOU_LOST = 'YOU LOST AGAINST THE MACHINE!'
YOU_TIED = 'YOU TIED WITH THE MACHINE!'


class TicTacToe:
    def __init__(self, initialBoard):
        # Initialize the game with the board and current player
        self.__board = initialBoard
        self.current_player = HUMAN

    def __str__(self):
        # Return a string representation of the board.
        board = self.__board
        return f'''
----------
{board[0][0]} | {board[0][1]} | {board[0][2]}
{board[1][0]} | {board[1][1]} | {board[1][2]}
{board[2][0]} | {board[2][1]} | {board[2][2]}
----------
'''


    def getPlayer(self):
        # Return the current player.
        return self.current_player

    def isWin( self ):
        # See if the board represents a win for the current
        # player. A win is three of the current player's tokens
        # in a single row, column, or either diagonal.
        for row in self.__board:
            if len(set(row)) == 1 and ' ' not in row:
                return True
        
        for i in range(3):
            col = set()
            for j in range(3):
                col.add(self.__board[j][i])
            if len(col) == 1 and ' ' not in col:
                return True
        
        l_to_r = {self.__board[0][0], self.__board[1][1], self.__board[2][2]}
        r_to_l = {self.__board[0][2], self.__board[1][1], self.__board[2][0]}

        if (len(l_to_r) == 1 and ' ' not in l_to_r) or (len(r_to_l) == 1 and ' ' not in r_to_l):
            return True
        
        return False


    def swapPlayers( self ):
        # Change the current player from HUMAN to MACHINE or
        # vice versa.
        self.current_player = HUMAN if self.current_player == MACHINE else MACHINE
        
    def humanMove( self ):
        # Ask the HUMAN to specify a move.  Check that it's 
        # valid (syntactically, in range, and the space is 
        # not occupied).  Update the board appropriately.
        row, col = map(int, input('Enter move coordinates between 0 and 2 separated by a comma: ').split(','))
        
        while self.__board[row][col] != ' ':
            print('Error: Invalid Input')
            row, col = map(int, input('Enter move coordinates between 0 and 2 separated by a comma: '.split(',')))
        
        self.__board[row][col] = 'X'

    def machineMove( self ):
        # This is the MACHINE's move.  It picks squares randomly
        # until it finds an empty one. Update the board appropriately.
        # Note: this is a really dumb way to play tic-tac-toe.  
        print("Machine's turn:")
        while True:
            r = random.randint(0, 2)
            c = random.randint(0, 2)
            if self.__board[r][c] == " ":
                print("  Machine chooses: ", r, ", ", c, sep="")
                self.__board[r][c] = "O"
                return

def driver( ):
    """ This plays tic-tac-toe in a pretty simple-minded
    fashion.  The human player goes first with token "X" and
    alternates with the machine using token "O".  We print
    the board before the first move and after each move. """

    # Print the welcome message
    print( WELCOME )
    # Initialize the board and player
    ttt = TicTacToe(initialBoard=initialBoard)

    print( ttt )
    # There are up to 9 moves in tic-tac-toe.
    for move in range(9):
        # The current player may be HUMAN
        # or MACHINE
        if ttt.getPlayer() == HUMAN:
            # If HUMAN, take a move, print the board,
            # and see if it's a win.
            ttt.humanMove()
            print( ttt )
            if ttt.isWin():
                print( YOU_WON )
                return
        else:
            # Else Machine takes a move.  Print the
            # board and see if the machine won.
            ttt.machineMove()
            print( ttt )
            if ttt.isWin():
                print( YOU_LOST )
                return
        # Swap players.
        ttt.swapPlayers()
    # After nine moves with no winner, it's a tie.
    print( YOU_TIED )
    
driver()