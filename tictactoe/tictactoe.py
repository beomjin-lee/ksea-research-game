def vertical_check(board):
    # TODO:
    # if x of key(x,y) is 0 or 1 or 2 -> vertical
    # (0, 0) (0, 1) (0, 2) check
    # (1, 0) (1, 1) (1, 2) check
    # (2, 0) (2, 1) (2, 2) check
    first_column = (board[(0, 0)] and board[(0, 1)] and board[(0, 2)] == 1)
    second_column = (board[(1, 0)] and board[(1, 1)] and board[(1, 2)] == 1)
    third_column = (board[(2, 0)] and board[(2, 1)] and board[(2, 2)] == 1)
    if first_column or second_column or third_column:
        return True
    else:
        return False 

def horizontal_check(board):
    # TODO:


def diagonal_check(board):
    # TODO:


def draw_check(board):
    # TODO:


def main():
    board = {
        (0, 0) : 0,
        (0, 1) : 0,
        (0, 2) : 0,
        (1, 0) : 0,
        (1, 1) : 0,
        (1, 2) : 0,
        (2, 0) : 0,
        (2, 1) : 0,
        (2, 2) : 0
    }

    step = 0




if __name__ == "__main__":
    main()
