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

    def change_is_piece_set(self):
        print("Hello")
        # Wonwoo



class Piece:
    # Shape names reference: https://tetris.wiki/Tetromino
    def __init__(self):
        #
        cleared_row_count = 0
        dimension = [0][0]
        position = (0, 0)

    class I_shape:
        dimension = [1][4]
        position = 
        dimension[0][0] = 1 
        dimension[0][1] = 1
        dimension[0][2] = 1
        dimension[0][3] = 1

    class O_shape:
        dimension = [2][2]
        position = 
        dimension[0][0] = 1 
        dimension[0][1] = 1
        dimension[1][0] = 1
        dimension[1][1] = 1
    
    class T_shape:
        dimension = [2][3]
        position = 
        dimension[0][0] = 1 
        dimension[0][1] = 1
        dimension[1][0] = 1
        dimension[1][1] = 1
        dimension[1][0] = 1
        dimension[1][1] = 1
    
    class S_shape:
        dimension = [2][3]
        position = 
    
    class Z_shape:
        dimension = [2][3]
        position = 
    
    class J_shape:
        dimension = [2][3]
        position = 
    
    class L_shpae:
        dimension = [2][3]
        position = 

    



    def random_piece_gen(self):
        

    def rotate_piece(self):


    def change_row(self):
        row_num = row_num - cleared_row_count



class Game:
    def __init__(self):
        self.board = Board()
        self.piece = Piece()
        
        self.score = 0

    def timer(self):
        # Henry,

    def move(self):
        # Henry,

    def rotate(self):
        # Henry,

    def score(self):
        # Brian Y.
        # Just Tetris scoring please
        self.score = NotImplementedError()
