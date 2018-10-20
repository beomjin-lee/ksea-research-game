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
        # Wonwoo
 


class Piece:
    def __init__(self):
        #

    def random_piece_gen(self):
        #


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
