from array import array

# cool way
from random import random

board = [['_'] * 3 for i in range(3)]
board[1][2] = 'O'
print(board)

# bad way
weird_board = [['_'] * 3] * 3
weird_board[1][2] = 'O'
print(weird_board)

ar1 = array('d', (1 for e in range(100)))
with open('file1.txt', 'wb') as f:
    ar1.tofile(f)
