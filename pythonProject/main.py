import tkinter as tk
import random
board_size = 15
cell_size = 50

line_weight = 4
click = "<Button-1>"

colors = {
    "TC": "#ff6e6e",
    "DC": "#ffff70",
    "TL": "#0373fc",
    "DL": "#d4ccff",
    " ": "#79b58f",
    "START": "#ffff70"
}
special_tiles = {
    "TC": [(0, 0), (0, 7), (0, 14), (7, 0), (7, 14), (14, 0), (14, 7), (14, 14)],
    "DC": [(1, 1), (2, 2), (3, 3), (4, 4), (10, 10), (11, 11), (12, 12), (13, 13),
           (1, 13), (2, 12), (3, 11), (4, 10), (10, 4), (11, 3), (12, 2), (13, 1)],
    "TL": [(1, 5), (1, 9), (5, 1), (5, 5), (5, 9), (5, 13),
           (9, 1), (9, 5), (9, 9), (9, 13), (13, 5), (13, 9)],
    "DL": [(0, 3), (0, 11), (2, 6), (2, 8), (3, 0), (3, 7), (3, 14),
           (6, 2), (6, 6), (6, 8), (6, 12), (7, 3), (7, 11), (8, 2), (8, 6),
           (8, 8), (8, 12), (11, 0), (11, 7), (11, 14), (12, 6), (12, 8), (14, 3), (14, 11)],
    "START": [(7,7)]
}
scrabble_letters = {
    'A': 11, 'B': 2, 'C': 2, 'D': 5, 'E': 11, 'F': 1, 'G': 2,
    'H': 1, 'I': 10, 'J': 1, 'K': 1, 'L': 4, 'M': 3, 'N': 5,
    'O': 8, 'P': 4, 'Q': 0, 'R': 5, 'S': 5, 'T': 7, 'U': 6,
    'V': 2, 'W': 0, 'X': 1, 'Y': 0, 'Z': 1
}


canvas_player_turns = [0, 0, 0, 0]


scrabble_list = [letter for letter, count in scrabble_letters.items() for _ in range(count)]

def take_tiles_from_bag_at_start(num_tiles=7):
    global scrabble_list
    drawn_tiles = random.sample(scrabble_list, num_tiles)
    for tile in drawn_tiles:
        scrabble_list.remove(tile)
    return drawn_tiles
def take_tiles_from_bag_after_word(player):

    missing = sum(1 for tile in player if tile == '')

    drawn_tiles = random.sample(scrabble_list, missing)

    for tile in drawn_tiles:
        scrabble_list.remove(tile)

    for i in range(len(player)):
        if player[i] == '':
            player[i] = drawn_tiles.pop(0)

player1 = take_tiles_from_bag_at_start()
player2 = take_tiles_from_bag_at_start()
player3 = take_tiles_from_bag_at_start()
player4 = take_tiles_from_bag_at_start()

player1_name = "BIA"
player2_name = "R\nA\nD\nU\n"
player3_name = "DARIA"
player4_name = "G\nD\nT\n"

player_turn = 1
letter_was_placed = True

board = [['' for _ in range(15)] for _ in range(15)]
word = []
letter = ""
letter_id = 0

def get_cell_type(row, col):
    for tile, positions in special_tiles.items():
        if (row, col) in positions:
            return tile
    return " "

def draw_scrabble_board():

    window.geometry(f"{screen_width}x{screen_height}")

    for row in range(board_size):
        for col in range(board_size):
            cell_type = get_cell_type(row, col)
            color = colors[cell_type]
            x1 = board_x_start + col * cell_size
            y1 = board_y_start + row * cell_size
            x2 = x1 + cell_size
            y2 = y1 + cell_size

            canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="black", width=line_weight)

            if cell_type != " ":
                canvas.create_text(x1 + cell_size / 2, y1 + cell_size / 2, text=cell_type, font=("Arial Black", 10, "bold"), fill="black")

def draw_players_board():

    vector_x_start = board_x_start + 4 * cell_size
    vector_y_start = board_y_start + board_height + cell_size

    # down player 1
    for i in range(7):
        x1 = vector_x_start + i * cell_size
        y1 = vector_y_start
        x2 = x1 + cell_size
        y2 = y1 + cell_size

        canvas.create_rectangle(x1, y1, x2, y2, fill="lightblue", outline="black", width=line_weight)
        if player1[i] != '':
            canvas.create_text(x1 + cell_size / 2,
                               y1 + cell_size / 2,
                               text=player1[i], font=("Arial Black", 10, "bold"), fill="black")

    vector_x_start = board_x_start + 4 * cell_size
    vector_y_start = board_y_start - cell_size - cell_size

    # up player 3
    for i in range(7):
        x1 = vector_x_start + i * cell_size
        y1 = vector_y_start
        x2 = x1 + cell_size
        y2 = y1 + cell_size

        canvas.create_rectangle(x1, y1, x2, y2, fill="lightblue", outline="black", width=line_weight)
        if player3[i] != '':
            canvas.create_text(x1 + cell_size / 2,
                               y1 + cell_size / 2,
                               text=player3[i], font=("Arial Black", 10, "bold"), fill="black")

    vector_x_start = board_x_start + board_width + cell_size
    vector_y_start = board_y_start + 4 * cell_size

    # right player 2
    for i in range(7):
        x1 = vector_x_start
        y1 = vector_y_start + i * cell_size
        x2 = x1 + cell_size
        y2 = y1 + cell_size

        canvas.create_rectangle(x1, y1, x2, y2, fill="lightblue", outline="black", width=line_weight)
        if player2[i] != '':
            canvas.create_text(x1 + cell_size / 2,
                               y1 + cell_size / 2,
                               text=player2[i], font=("Arial Black", 10, "bold"), fill="black")

    vector_x_start = board_x_start - cell_size - cell_size
    vector_y_start = board_y_start + 4 * cell_size

    # left player 4
    for i in range(7):
        x1 = vector_x_start
        y1 = vector_y_start + i * cell_size
        x2 = x1 + cell_size
        y2 = y1 + cell_size

        canvas.create_rectangle(x1, y1, x2, y2, fill="lightblue", outline="black", width=line_weight)
        if player4[i] != '':
            canvas.create_text(x1 + cell_size / 2,
                               y1 + cell_size / 2,
                               text=player4[i], font=("Arial Black", 10, "bold"), fill="black")

def clean_word_from_board(_wrd, player):

    for (l, c, r) in _wrd:
        board[c][r] = ''
        paint(r, c, "default")
        for i in range(7):
            if player[i] == '':
                player[i] = l
                break

def paint(col, row, _letter):

    x1 = board_x_start + col * cell_size
    y1 = board_y_start + row * cell_size
    x2 = x1 + cell_size
    y2 = y1 + cell_size

    canvas.create_rectangle(x1 + 5.5, y1 + 5.5, x2 - 5.5, y2 - 5.5, fill="white", outline="black", width=line_weight - 2)

    if _letter == '_':
        canvas.create_rectangle(x1, y1, x2, y2, fill="lightblue", outline="black", width=line_weight)

    if _letter != '' and _letter != '_' and _letter != 'default':
        canvas.create_text(x1 + cell_size / 2,
                           y1 + cell_size / 2,
                           text=_letter, font=("Arial Black", 14, "bold"), fill="black")

    if _letter == "default":

        cell_type = get_cell_type(row, col)
        color = colors[cell_type]

        canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="black", width=line_weight)

        canvas.create_text(x1 + cell_size / 2,
                           y1 + cell_size / 2,
                           text=get_cell_type(row, col), font=("Arial Black", 10, "bold"), fill="black")


def get_crossed_words(wrd: [(str, int, int)]):

    initial = wrd.copy()

    # #caut literelel
    # d = [(0,1), (1,0), (0,-1), (-1,0)]
    # for i in range(len(wrd)):
    #     (_, line, col) = wrd[i]
    #     for j in range(4):
    #         if  0 <= line + d[j][0] <= 15 and 0 <= col + d[j][1] <= 15 and board[line + d[j][0]][col + d[j][1]] != '':
    #             if (board[line + d[j][0]][col + d[j][1]], line + d[j][0], col + d[j][1]) not in wrd:
    #                 wrd.append((board[line + d[j][0]][col + d[j][1]], line + d[j][0], col + d[j][1]))


    board_words = []

    for i in range(15):
        new_word = []
        for j in range(15):
            if board[j][i] != '':
                new_word.append((board[j][i], j, i))
            else:
                if len(new_word) > 1:
                    board_words.append(new_word.copy())
                new_word.clear()

        if len(new_word) > 1:
            board_words.append(new_word.copy())
    for i in range(15):
        new_word = []
        for j in range(15):
            if board[i][j] != '':
                new_word.append((board[i][j], i, j))
            else:
                if len(new_word) > 1:
                    board_words.append(new_word.copy())
                new_word.clear()
        if len(new_word) > 1:
            board_words.append(new_word.copy())

    filtered_words = []
    for word in board_words:
        in_selected_letter = False
        for letter in word:
            if letter in initial:
                in_selected_letter = True
                break

        if in_selected_letter:
            filtered_words.append(word)

    print(f"Cuvinte formate: {filtered_words}")

def get_word_direction(wrd: [(str, int, int)]):
    is_line_constant = True
    is_column_constant = True

    for i in range(len(wrd) - 1):
        (_, line_old, col_old) = wrd[i]
        (_, line_new, col_new) = wrd[i + 1]

        if line_old != line_new:
            is_line_constant = False
        if col_old != col_new:
            is_column_constant = False

    if is_line_constant:
        return "H"
    elif is_column_constant:
        return "V"

    return "U" # the letters were placed wrong

def on_click(event):

    global player_turn, letter_was_placed, word, letter, player1, player2, player3, player4, letter_id, board

    player_placed_tile_on_board = False
    player_chose_tile_from_rack = False
    player_id = 0

    selected_row = (event.x - board_x_start) // cell_size
    selected_col = (event.y - board_y_start) // cell_size

    #player placed a letter onto the board
    if not letter_was_placed and board_x_start < event.x < board_x_start + board_width and board_y_start < event.y < board_y_start + board_height:

        if board[selected_col][selected_row] == '': #board tile was empty
            board[selected_col][selected_row] = letter
            player_placed_tile_on_board = True
            letter_was_placed = True

        if player_turn == 1:

            if player1[letter_id] != '':
                word.append((player1[letter_id], selected_col, selected_row))
                letter = player1[letter_id]
                player1[letter_id] = ''
            show_finish_option_player1(True)

        elif player_turn == 2:

            if player2[letter_id] != '':
                word.append((player2[letter_id], selected_col, selected_row))
                letter = player2[letter_id]
                player2[letter_id] = ''
            show_finish_option_player2(True)

        elif player_turn == 3:

            if player3[letter_id] != '':
                word.append((player3[letter_id], selected_col, selected_row))
                letter = player3[letter_id]
                player3[letter_id] = ''
            show_finish_option_player3(True)

        elif player_turn == 4:

            if player4[letter_id] != '':
                word.append((player4[letter_id], selected_col, selected_row))
                letter = player4[letter_id]
                player4[letter_id] = ''
            show_finish_option_player4(True)


    #player selected a letter from his rack
    if   player_turn == 1 and board_x_start + 4 * cell_size < event.x < board_x_start +  11  * cell_size and board_y_start + board_height + cell_size < event.y < board_y_start + board_height + 2 * cell_size:
        player_id = 1
        letter_id = (event.x - board_x_start) // cell_size - 4
        if player1[letter_id] != '':
            player_chose_tile_from_rack = True
            letter_was_placed = False

    elif player_turn == 2 and  board_x_start + board_width + cell_size < event.x < board_x_start + board_width + 2 * cell_size and board_y_start + 4 * cell_size < event.y < board_y_start + 11 * cell_size:
        player_id = 2
        letter_id = (event.y - board_y_start) // cell_size - 4
        if player2[letter_id] != '':
            player_chose_tile_from_rack = True
            letter_was_placed = False

    elif player_turn == 3 and board_x_start + 4 * cell_size < event.x < board_x_start +  11  * cell_size and board_y_start - 2 * cell_size  < event.y < board_y_start - cell_size:
        player_id = 3
        letter_id = (event.x - board_x_start) // cell_size - 4
        if player3[letter_id] != '':
            player_chose_tile_from_rack = True
            letter_was_placed = False

    elif player_turn == 4 and board_x_start - 2 * cell_size < event.x < board_x_start - cell_size and board_y_start + 4 * cell_size < event.y < board_y_start + 11 * cell_size:
        player_id = 4
        letter_id = (event.y - board_y_start) // cell_size - 4
        if player4[letter_id] != '':
            player_chose_tile_from_rack = True
            letter_was_placed = False


    #player pressed check my word
    if   player_turn == 1 and board_x_start + 12 * cell_size < event.x < board_x_start +  13 * cell_size and board_y_start + board_height + cell_size < event.y < board_y_start + board_height + 2 * cell_size:
        player_turn = 2
        show_finish_option_player1(False)
        take_tiles_from_bag_after_word(player1)
        draw_players_board()

        get_word_direction(word)
        word = sorted(word, key=lambda e: [e[1], e[2]])
        get_crossed_words(word)
        word.clear()
        show_turn_player2()

    elif player_turn == 2 and board_x_start + board_width + cell_size < event.x <  board_x_start + board_width + 2 * cell_size and board_y_start + 12 * cell_size < event.y < board_y_start + 13 * cell_size:
        player_turn = 3
        show_finish_option_player2(False)
        take_tiles_from_bag_after_word(player2)
        draw_players_board()

        get_word_direction(word)
        word = sorted(word, key=lambda e: [e[1], e[2]])
        get_crossed_words(word)
        word.clear()
        show_turn_player3()

    elif player_turn == 3 and board_x_start + 12 * cell_size < event.x < board_x_start +  13 * cell_size and board_y_start - 2 * cell_size < event.y < board_y_start - cell_size:
        player_turn = 4
        show_finish_option_player3(False)
        take_tiles_from_bag_after_word(player3)
        draw_players_board()

        get_word_direction(word)
        word = sorted(word, key=lambda e: [e[1], e[2]])
        get_crossed_words(word)
        word.clear()
        show_turn_player4()

    elif player_turn == 4 and board_x_start - 2 * cell_size < event.x <  board_x_start - cell_size and board_y_start + 12 * cell_size < event.y < board_y_start + 13 * cell_size:
        player_turn = 1
        show_finish_option_player4(False)
        take_tiles_from_bag_after_word(player4)
        draw_players_board()

        get_word_direction(word)
        word = sorted(word, key=lambda e: [e[1], e[2]])
        get_crossed_words(word)
        word.clear()
        show_turn_player1()

    #player pressed reset my word
    if   player_turn == 1 and board_x_start + 14 * cell_size < event.x < board_x_start +  15 * cell_size and board_y_start + board_height + cell_size < event.y < board_y_start + board_height + 2 * cell_size:
        clean_word_from_board(word, player1)
        draw_players_board()
        word.clear()

    elif player_turn == 2 and board_x_start + board_width + cell_size < event.x <  board_x_start + board_width + 2 * cell_size and board_y_start + 14 * cell_size < event.y < board_y_start + 15 * cell_size:
        clean_word_from_board(word, player2)
        draw_players_board()
        word.clear()

    elif player_turn == 3 and board_x_start + 14 * cell_size < event.x < board_x_start +  15 * cell_size and board_y_start - 2 * cell_size < event.y < board_y_start - cell_size:
        clean_word_from_board(word, player3)
        draw_players_board()
        word.clear()

    elif player_turn == 4 and board_x_start - 2 * cell_size < event.x <  board_x_start - cell_size and board_y_start + 14 * cell_size < event.y < board_y_start + 15 * cell_size:
        clean_word_from_board(word, player4)
        draw_players_board()
        word.clear()


    #player placed a letter on board -> draw his decision
    if player_placed_tile_on_board:
        paint(selected_row, selected_col, letter)
        board[selected_col][selected_row] = letter

    #player selected a letter from rack -> draw his decision
    if player_chose_tile_from_rack:
        paint(selected_row, selected_col, '_')

def show_finish_option_player1(draw):

    if draw:
        canvas.create_rectangle(board_x_start + 12 * cell_size,
                                board_y_start + board_height + 2 * cell_size,
                                board_x_start + 13 * cell_size,
                                board_y_start + board_height + cell_size,
                                fill="orange", outline="black", width=line_weight)

        canvas.create_text(board_x_start + 12 * cell_size + cell_size / 2,
                           board_y_start + board_height + cell_size + cell_size / 2,
                           text="✔", font=("Arial Black", 20, "bold"), fill="black")
    else:
        canvas.create_rectangle(board_x_start + 12 * cell_size,
                                board_y_start + board_height + 2 * cell_size,
                                board_x_start + 13 * cell_size,
                                board_y_start + board_height + cell_size,
                                fill="lightgray", outline="lightgray", width=line_weight)

    if draw:
        canvas.create_rectangle(board_x_start + 14 * cell_size,
                                board_y_start + board_height + 2 * cell_size,
                                board_x_start + 15 * cell_size,
                                board_y_start + board_height + cell_size,
                                fill="orange", outline="black", width=line_weight)

        canvas.create_text(board_x_start + 14 * cell_size + cell_size / 2,
                           board_y_start + board_height + cell_size + cell_size / 2,
                           text="↺", font=("Arial Black", 25, "bold"), fill="black")
    else:
        canvas.create_rectangle(board_x_start + 14 * cell_size,
                                board_y_start + board_height + 2 * cell_size,
                                board_x_start + 15 * cell_size,
                                board_y_start + board_height + cell_size,
                                fill="lightgray", outline="lightgray", width=line_weight)
def show_finish_option_player2(draw):
    if draw:
        canvas.create_rectangle(board_x_start + board_width + cell_size,
                                board_y_start + 12 * cell_size,
                                board_x_start + board_width + 2 * cell_size,
                                board_y_start + 13 * cell_size,
                                fill="orange", outline="black", width=line_weight)

        canvas.create_text(board_x_start + board_width + cell_size + cell_size / 2,
                           board_y_start + 12 * cell_size + cell_size / 2,
                           text="✔", font=("Arial Black", 20, "bold"), fill="black")
    else:
        canvas.create_rectangle(board_x_start + board_width + cell_size,
                                board_y_start + 12 * cell_size,
                                board_x_start + board_width + 2 * cell_size,
                                board_y_start + 13 * cell_size,
                                fill="lightgray", outline="lightgray", width=line_weight)

    if draw:
        canvas.create_rectangle(board_x_start + board_width + cell_size,
                                board_y_start + 14 * cell_size,
                                board_x_start + board_width + 2 * cell_size,
                                board_y_start + 15 * cell_size,
                                fill="orange", outline="black", width=line_weight)

        canvas.create_text(board_x_start + board_width + cell_size + cell_size / 2,
                           board_y_start + 14 * cell_size + cell_size / 2,
                           text="↺", font=("Arial Black", 25, "bold"), fill="black")
    else:
        canvas.create_rectangle(board_x_start + board_width + cell_size,
                                board_y_start + 14 * cell_size,
                                board_x_start + board_width + 2 * cell_size,
                                board_y_start + 15 * cell_size,
                                fill="lightgray", outline="lightgray", width=line_weight)
def show_finish_option_player3(draw):

    if draw:
        canvas.create_rectangle(board_x_start + 12 * cell_size,
                                board_y_start - cell_size,
                                board_x_start + 13 * cell_size,
                                board_y_start - 2 * cell_size,
                                fill="orange", outline="black", width=line_weight)

        canvas.create_text(board_x_start + 12 * cell_size + cell_size / 2, board_y_start - 2 * cell_size + cell_size / 2,
                           text="✔", font=("Arial Black", 20, "bold"), fill="black")
    else:
        canvas.create_rectangle(board_x_start + 12 * cell_size,
                                board_y_start - cell_size,
                                board_x_start + 13 * cell_size,
                                board_y_start - 2 * cell_size,
                                fill="lightgray", outline="lightgray", width=line_weight)

    if draw:
        canvas.create_rectangle(board_x_start + 14 * cell_size,
                                board_y_start - cell_size,
                                board_x_start + 15 * cell_size,
                                board_y_start - 2 * cell_size,
                                fill="orange", outline="black", width=line_weight)

        canvas.create_text(board_x_start + 14 * cell_size + cell_size / 2, board_y_start - 2 * cell_size + cell_size / 2,
                           text="↺", font=("Arial Black", 25, "bold"), fill="black")
    else:
        canvas.create_rectangle(board_x_start + 14 * cell_size,
                                board_y_start - cell_size,
                                board_x_start + 15 * cell_size,
                                board_y_start - 2 * cell_size,
                                fill="lightgray", outline="lightgray", width=line_weight)
def show_finish_option_player4(draw):
    if draw:
        canvas.create_rectangle(board_x_start - 2 * cell_size,
                                board_y_start + 12 * cell_size,
                                board_x_start - cell_size,
                                board_y_start + 13 * cell_size,
                                fill="orange", outline="black", width=line_weight)

        canvas.create_text(board_x_start - 2 * cell_size + cell_size / 2,
                           board_y_start + 12 * cell_size + cell_size / 2,
                           text="✔", font=("Arial Black", 20, "bold"), fill="black")
    else:
        canvas.create_rectangle(board_x_start - 2 * cell_size,
                                board_y_start + 12 * cell_size,
                                board_x_start - cell_size,
                                board_y_start + 13 * cell_size,
                                fill="lightgray", outline="lightgray", width=line_weight)

    if draw:
        canvas.create_rectangle(board_x_start - 2 * cell_size,
                                board_y_start + 14 * cell_size,
                                board_x_start - cell_size,
                                board_y_start + 15 * cell_size,
                                fill="orange", outline="black", width=line_weight)

        canvas.create_text(board_x_start - 2 * cell_size + cell_size / 2,
                           board_y_start + 14 * cell_size + cell_size / 2,
                           text="↺", font=("Arial Black", 25, "bold"), fill="black")
    else:
        canvas.create_rectangle(board_x_start - 2 * cell_size,
                                board_y_start + 14 * cell_size,
                                board_x_start - cell_size,
                                board_y_start + 15 * cell_size,
                                fill="lightgray", outline="lightgray", width=line_weight)


def show_turn_player1():
    vector_x_start = board_x_start + 4 * cell_size + 7 * cell_size // 2
    vector_y_start = board_y_start + board_height + cell_size

    if canvas_player_turns[3]:
        canvas.delete(canvas_player_turns[3])

    canvas_player_turns[0] = canvas.create_text(vector_x_start, vector_y_start - cell_size//3, text="🢃 " + player1_name + " 🢃" ,  font=("Arial Black", 15, "bold"), fill="black")
def show_turn_player2():
    vector_x_start = board_x_start + board_width + 2.5 * cell_size
    vector_y_start = board_y_start + 4 * cell_size

    if canvas_player_turns[0]:
        canvas.delete(canvas_player_turns[0])

    canvas_player_turns[1] = canvas.create_text(vector_x_start, vector_y_start + 3.5 * cell_size, text="🢀\n" + player2_name + "🢀" ,  font=("Arial Black", 15, "bold"),  fill="black")
def show_turn_player3():
    vector_x_start = board_x_start + 4 * cell_size + 7 * cell_size // 2
    vector_y_start = board_y_start - 2 * cell_size

    if canvas_player_turns[1]:
        canvas.delete(canvas_player_turns[1])
    canvas_player_turns[2] = canvas.create_text(vector_x_start, vector_y_start - cell_size // 3, text="🢃 " + player3_name + " 🢃", font=("Arial Black", 15, "bold"), fill="black")
def show_turn_player4():
    vector_x_start = board_x_start - 2.5 * cell_size
    vector_y_start = board_y_start + 4 * cell_size

    if canvas_player_turns[2]:
        canvas.delete(canvas_player_turns[2])

    canvas_player_turns[3] = canvas.create_text(vector_x_start, vector_y_start + 3.5 * cell_size, text="🢂\n" + player4_name + "🢂", font=("Arial Black", 15, "bold"), fill="black")

window = tk.Tk()
window.title("Radu's Scrabble")

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
board_width = board_size * cell_size
board_height = board_size * cell_size
board_x_start = (screen_width - board_width) // 2
board_y_start = (screen_height - board_height) // 2

canvas = tk.Canvas(window, width=screen_width, height=screen_height, bg="lightgray")
canvas.pack()

draw_scrabble_board()
draw_players_board()
show_turn_player1()


canvas.bind(click, on_click)
window.mainloop()