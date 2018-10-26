import numpy as np

class Board:
    def __init__(self):
        # Put the board implementation here
        # Hashmap? Array? Future of KSEA lies in your hands
        # Eugene
        self.x_size = 10
        self.y_size = 20
        self.is_piece_set = False # piece moving

    def game_over(self):
        # Brian L.
        pass

    def change_is_piece_set(self):
        print("Hello")
        # Wonwoo



class Piece:
    # Shape names reference: https://tetris.wiki/Tetromino
    def __init__(self):
        #
        self.cleared_row_count = 0
        self.dimension = np.zeros((0, 0))
        self.position = [0, 0]

    def random_piece_gen(self):
        pass

    def rotate_piece(self):
        pass

    def change_row(self):
        row_num = row_num - cleared_row_count

class I_shape(Piece):
    

    def __init__(self):
        #
        dimension = np.zeros((1, 4))
        dimension[0][0] = 1 
        dimension[0][1] = 1
        dimension[0][2] = 1
        dimension[0][3] = 1
        self.cleared_row_count = 0
        self.dimension = dimension
        self.position = [0, 0]

class O_shape(Piece):
    

    def __init__(self):
        #
        dimension = np.zeros((2, 2))
        dimension[0][0] = 1 
        dimension[0][1] = 1
        dimension[1][0] = 1
        dimension[1][1] = 1
        self.cleared_row_count = 0
        self.dimension = dimension
        self.position = [0, 0]

class T_shape(Piece):
    

    def __init__(self):
        #
        dimension = np.zeros((2, 3))
        dimension[0][0] = 1 
        dimension[0][1] = 1
        dimension[0][2] = 1
        dimension[1][0] = 0
        dimension[1][1] = 1
        dimension[1][2] = 0
        self.cleared_row_count = 0
        self.dimension = dimension
        self.position = [0, 0]

class S_shape(Piece):


    def __init__(self):
        #
        dimension = np.zeros((2, 3))
        dimension[0][0] = 1 
        dimension[0][1] = 1
        dimension[0][2] = 0
        dimension[1][0] = 0
        dimension[1][1] = 1
        dimension[1][2] = 1
        self.cleared_row_count = 0
        self.dimension = dimension
        self.position = [0, 0]

class Z_shape(Piece):
    

    def __init__(self):
        #
        dimension = np.zeros((2, 3))
        dimension[0][0] = 0 
        dimension[0][1] = 1
        dimension[0][2] = 1
        dimension[1][0] = 1
        dimension[1][1] = 1
        dimension[1][2] = 0
        self.cleared_row_count = 0
        self.dimension = dimension
        self.position = [0, 0]

class J_shape(Piece):
    

    def __init__(self):
        #
        dimension = np.zeros((2, 3))
        dimension[0][0] = 1 
        dimension[0][1] = 1
        dimension[0][2] = 1
        dimension[1][0] = 1
        dimension[1][1] = 0
        dimension[1][2] = 0
        self.cleared_row_count = 0
        self.dimension = dimension
        self.position = [0, 0]

class L_shape(Piece):
    

    def __init__(self):
        #
        dimension = np.zeros((2, 3))
        dimension[0][0] = 1 
        dimension[0][1] = 1
        dimension[0][2] = 1
        dimension[1][0] = 0
        dimension[1][1] = 0
        dimension[1][2] = 1
        self.cleared_row_count = 0
        self.dimension = dimension
        self.position = [0, 0]

class Game:
    def __init__(self):
        self.board = Board()
        self.piece = Piece()
        
        self.score = 0

    def timer(self):
        # Henry,
        pass

    def move(self):
        # Henry,
        pass

    def rotate(self):
        # Henry,
        pass

    def score(self):
        # Brian Y.
        # Just Tetris scoring please
        self.score = NotImplementedError()
