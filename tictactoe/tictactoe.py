def vertical_check(board):
    # TODO:
    first_column = board[(0, 0)] == board[(0, 1)] and board[(0, 1)] == board[(0, 2)] and board[(0, 0)] ! = ' '
    second_column = board[(1, 0)] == board[(1, 1)] and board[(1, 1)] == board[(1, 2)] and board[(1, 0)] ! = ' '
    third_column = board[(2, 0)] == board[(2, 1)] and board[(2, 1)] == board[(2, 2)] and board[(2, 0)] ! = ' '
    if first_column or second_column or third_column:
        return True
    else:
        return False

def horizontal_check(board):
    # TODO:
    if (board[(0, 0)] == board[(1, 0)] and  board[(1, 0)] == board[(2, 0)] and board[(0, 0)] ! = ' '):
        return True
    elif (board[(0, 1)] == board[(1, 1)] and  board[(1, 1)] == board[(2, 1)] and board[(0, 1)] ! = ' '):
        return True
    elif (board[(0, 2)] == board[(1, 2)] and  board[(1, 2)] == board[(2, 2)] and board[(0, 2)] ! = ' '):
        return True
    else:
        return False


def diagonal_check(board):

    # TODO:
    if board[(0, 0)] == board[(1, 1)] and board[(1, 1)] == board[(2, 2)] and board[(0, 0)] ! = ' ':
        return True
    elif board[(0, 2)] == board[(1, 1)] and board[(1, 1)] == board[(2, 0)] and board[(0, 2)] ! = ' ':
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

def game_print(board):
    print("   |   |   ")
    print(" " + board[(0, 2)] + " | " + board[(1, 2)] + " | " + board[(2, 2)] + " ")
    print("   |   |   ")
    print("---|---|---")
    print("   |   |   ")
    print(" " + board[(0, 1)] + " | " + board[(1, 1)] + " | " + board[(2, 1)] + " ")
    print("   |   |   ")
    print("---|---|---")
    print("   |   |   ")
    print(" " + board[(0, 0)] + " | " + board[(1, 0)] + " | " + board[(2, 0)] + " ")
    print("   |   |   ")


def change_player(player):
    player = 1 - player

def number_to_coord(number):
    if number > 9:
        print("Invalid number")
        break

    horizontal = (number - 1) % 3
    vertical = (number - 1) // 3
    return (horizontal, vertical)

def play(board, player):
    if player == 0:
        player_piece = 'X'
    else:
        player_piece = 'O'



def main():
    board = {
        (0, 0) : ' ',
        (0, 1) : ' ',
        (0, 2) : ' ',
        (1, 0) : ' ',
        (1, 1) : ' ',
        (1, 2) : ' ',
        (2, 0) : ' ',
        (2, 1) : ' ',
        (2, 2) : ' '
    }

    step = 0
    player = 0

    while step < 9:





if __name__ == "__main__":
    main()
