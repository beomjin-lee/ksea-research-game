def vertical_check(board):
    ## TODO:

def horizontal_check(board):
    ## # TODO:

def diagonal_check(board):
    if board[(0, 0)] == board[(1, 1)] and board[(1, 1)] == board[(2, 2)]:
        return True

    elif board[(0, 2)] == board[(1, 1)] and board[(1, 1)] == board[(2, 0)]:
        return True

    else:
        return False

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
