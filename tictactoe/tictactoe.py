def vertical_check(board):
    # TODO:
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
    if board[(0, 0)] == board[(1, 1)] and board[(1, 1)] == board[(2, 2)]:
        return True
    elif board[(0, 2)] == board[(1, 1)] and board[(1, 1)] == board[(2, 0)]:
        return True
    else:
        return False


def draw_check(board):
    vertical = vertical_check(board)
    horizontal = horizontal_check(board)
    diagonal = diagonal_check(board)

    if not vertical or not horizontal or not diagonal:
        print('Draw!')
        return True


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

    while step < 9:





if __name__ == "__main__":
    main()
