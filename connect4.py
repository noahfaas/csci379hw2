from typing import Tuple, List
from copy import deepcopy
import random

class Connect4:
    def __init__(self, state=None, turn="O", rows=6, cols=7,):
        assert rows >= 4, "Must have 4 or more rows"
        assert cols >= 4, "Must have 4 or more cols"

        self.rows = rows
        self.cols = cols
        if state is None:
            self.board = [["." for _ in range(cols)] for _ in range(rows)]
        else:
            self.board = state
        self.turn = turn

    def welcome(self):
        print("Welcome to Connect 4!")
        print("Place a token in a column and it will")
        print("fall to the next available spot.")
        print("To win, you must get 4 in a row.")
        print("This can be vertical, horizontal,")
        print("or on a diagonal.")

    def to_move(self) -> str:
        return self.turn

    # Print board
    def display(self):
        header = " "
        for i in range(self.cols):
            header += str(i) + " "
        print(header) # Column headers for the players
        print("-" * (self.cols*2+1))
        
        for row in self.board:
            print("|", end="")
            for cell in row:
                print(cell, end="|") # Player 1
            print()
        
        print("-" * (self.cols*2+1))

    def actions(self) -> List[int]:
        possible = [i for i in range(self.cols) if self.board[0][i] == "."]

        return possible

    # Determine if move is valid
    def is_valid(self, col:int) -> bool:
        if col > self.cols or col < 0:
            print(f"Invalid col: {col} is not a valid column")
            return False
        elif self.board[0][col] == ".": # Check if column has room
            return True
        else:
            print(f"Invalid col: Column {col} is full")
            return False
    
    # Return a deepcopy of the board
    # Python will use pointers for lists
    # Must be a deep copy
    def state(self) -> List[List[str]]:
        return deepcopy(self.board)
    
    # Check if move is valid
    # If it is, look for empty spot
    # Start at bottom and work way up
    def make_move(self, col:int):
        if self.is_valid(col):
            for row in range(self.rows-1, -1, -1):
                if self.board[row][col] == ".":
                    self.board[row][col] = self.turn
                    if self.turn == "O":
                        self.turn = "X"
                    else:
                        self.turn = "O"
                    break

    # Check all three win conditions
    def is_terminal(self) -> Tuple[bool, str]:
        for check in [self._is_row_win, self._is_col_win, self._is_diag_win]:
            has_won, winner = check()
            if has_won:
                return True, winner
        
        if all(cell != "." for cell in self.board[0]):
            return True, "Tie"

        return False, None

    def _is_row_win(self) -> Tuple[bool, str]:
        # Check each row
        for row in self.board:
            # Check [0, self.cols-3) as starting point of win
            # Typically [0, 3]
            for i in range(0, self.cols-3):
                #If you start with a ".", can't be a win
                if row[i] == ".":
                    continue

                # If i-i+4 include the same value, that's the winner
                if all([x == row[i] for x in row[i:i+4]]):
                    return True, row[i]
        return False, None
    
    def _is_col_win(self) -> Tuple[bool, str]:
        # Check each column
        for c_i in range(0, self.cols):
            # Check [0, self.rows-3) as starting point of win
            # Typically [0, 3]
            for r_i in range(0, self.rows-3):
                if self.board[r_i][c_i] == ".":
                    continue
                
                # If I did this in Numpy, it would've been easier
                # whomp whomp
                start_piece = self.board[r_i][c_i]
                is_win = True
                # Check piece below me are same for win 
                for i in range(1,4):
                    is_win = is_win and (start_piece == self.board[r_i+i][c_i])
                
                if is_win:
                    return True, start_piece
        
        return False, None
    
    def _is_diag_win(self) -> Tuple[bool, str]:
        # 1. Check descending diagonals (\)
        # We only check rows up to rows-3 and cols up to cols-3
        for r in range(self.rows - 3):
            for c in range(self.cols - 3):
                start_piece = self.board[r][c]
                if start_piece != "." and \
                   start_piece == self.board[r+1][c+1] == self.board[r+2][c+2] == self.board[r+3][c+3]:
                    return True, start_piece

        # 2. Check ascending diagonals (/)
        # We start from row 3 and up, and cols up to cols-3
        for r in range(3, self.rows):
            for c in range(self.cols - 3):
                start_piece = self.board[r][c]
                if start_piece != "." and \
                   start_piece == self.board[r-1][c+1] == self.board[r-2][c+2] == self.board[r-3][c+3]:
                    return True, start_piece

        return False, None   
            