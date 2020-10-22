board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7],
]


def print_board(board_arr):
    for i in range(len(board_arr)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - -")

        for j in range(len(board_arr[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(board_arr[i][j])
            else:
                print(str(board_arr[i][j]) + " ", end="")


def find_empty_square(board_arr):
    """
    :param board_arr: board

    :return: empty square position (row, col) if any or None
    """
    for row in range(len(board_arr)):
        for col in range(len(board_arr[0])):
            if board_arr[row][col] == 0:
                return row, col

    return None


def is_valid_entry_at_pos(board_arr, entry, pos):
    """
    :param board_arr: board
    :param entry: number to be entered at given position
    :param pos: position (row, col)

    :return: if entry at given position is possible or not (bool)
    """

    x_pos = pos[0]
    y_pos = pos[1]

    # Box position:
    x_box = x_pos // 3  # floor(x_pos/3)
    y_box = y_pos // 3  # floor(y_pos/3)

    # check row:
    for col in range(len(board_arr[0])):
        if board_arr[x_pos][col] == entry and y_pos != col:
            return False

    # check col:
    for row in range(len(board_arr[0])):
        if board_arr[row][y_pos] == entry and x_pos != row:
            return False

    # check 3 X 3 cube corresponding to given pos:
    for box_row in range(x_box * 3, x_box * 3 + 3):
        for box_col in range(y_box * 3, y_box * 3 + 3):
            if board_arr[box_row][box_col] == entry and (box_row, box_col) != pos:
                return False

    return True


def solve_board(board_arr):
    empty_square_pos = find_empty_square(board_arr)

    if not empty_square_pos:
        return True  # solved

    else:
        empty_row, empty_col = empty_square_pos

        # check for each possible entry from 1 to 9 at (empty_row, empty_col)
        for possible_entry in range(1, 10):
            is_valid = is_valid_entry_at_pos(board_arr=board_arr, entry=possible_entry, pos=(empty_row, empty_col))

            if is_valid:
                # change empty_square to possible_entry
                board_arr[empty_row][empty_col] = possible_entry

                # solve with this updated board
                sol = solve_board(board_arr)

                if sol:
                    return True
                else:
                    # empty square
                    board_arr[empty_row][empty_col] = 0

                    # again find another possible_entry after current possible_entry and try to solve i.e.
                    # continue for loop
                    continue

        # if no possible_entry i.e. 1 to 9 fits in empty_square, backtrack
        return False


print_board(board_arr=board)
solve_board(board_arr=board)
print("___________________________")
print_board(board_arr=board)
