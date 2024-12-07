import tkinter as tk
import random
board_size = 15
cell_size = 50 #50 monitor 42 laptop
letter_font_size = 14 #14 monitor 12 laptop
digit_font_size = 10 #10 monitor 8 laptop
num_of_tiles_at_start = 7
num_of_players = 4

line_weight = 4
click = "<Button-1>"
tile_fill = "#fae4c3"
padding = 4

colors = {
    "TC": "#ff6e6e",
    "DC": "#ffff70",
    "TL": "#0373fc",
    "DL": "#d4ccff",
    " ": "#79b58f",
    "GO": "#ffff70"
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
    "GO": [(7,7)]
}
scrabble_letters = {
    'A': 11, 'B': 2, 'C': 2, 'D': 5, 'E': 11, 'F': 1, 'G': 2,
    'H': 1, 'I': 10, 'J': 1, 'K': 1, 'L': 4, 'M': 3, 'N': 5,
    'O': 8, 'P': 4, 'Q': 0, 'R': 5, 'S': 5, 'T': 7, 'U': 6,
    'V': 2, 'W': 0, 'X': 1, 'Y': 0, 'Z': 1
}

# scrabble_letters = {
#     'A': 5, 'B': 1, 'C': 1, 'D': 2, 'E': 5, 'F': 0, 'G': 1,
#     'H': 0, 'I': 5, 'J': 0, 'K': 0, 'L': 2, 'M': 1, 'N': 2,
#     'O': 4, 'P': 2, 'Q': 0, 'R': 2, 'S': 2, 'T': 3, 'U': 3,
#     'V': 1, 'W': 0, 'X': 0, 'Y': 0, 'Z': 0
# }
scrabble_points = {
    'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 2,
    'H': 4, 'I': 1, 'J': 8, 'K': 5, 'L': 1, 'M': 3, 'N': 1,
    'O': 1, 'P': 3, 'Q': 10, 'R': 1, 'S': 1, 'T': 1, 'U': 1,
    'V': 4, 'W': 4, 'X': 8, 'Y': 4, 'Z': 10
}


canvas_player_turns = [0, 0, 0, 0]

scrabble_list = [letter for letter, count in scrabble_letters.items() for _ in range(count)]

def take_tiles_from_bag_at_start(num_tiles=num_of_tiles_at_start):
    global scrabble_list
    drawn_tiles = random.sample(scrabble_list, min(num_tiles, len(scrabble_list)))
    for tile in drawn_tiles:
        scrabble_list.remove(tile)
    return drawn_tiles

def take_tiles_from_bag_after_word(player):

    missing = sum(1 for tile in player if tile == '')

    drawn_tiles = random.sample(scrabble_list,  min(missing, len(scrabble_list)))

    for tile in drawn_tiles:
        scrabble_list.remove(tile)

    for i in range(len(player)):
        if player[i] == '' and len(drawn_tiles) > 0:
            player[i] = drawn_tiles.pop(0)

def check_player_bag_empty(player):
    has_at_least_one = False
    for letter in player:
        if letter != '':
            has_at_least_one = True

    if has_at_least_one:
        print("mai are piese")

    return (not has_at_least_one) and (len(scrabble_list) == 0)

def game_over():

    global score, canvas_score

    final_scores = [(player1_name, player1_score), (player2_name, player2_score),
                    (player3_name, player3_score), (player4_name, player4_score)]

    final_scores = sorted(final_scores, key=lambda s : s[1], reverse=True)

    score = "🎉 🎉 GAME OVER 🎉 🎉\n\n"

    place = 1
    for f_score in final_scores:
        score += "🏆" * place + " "
        score += f_score[0].replace('\n','') + " 👉 " + str(f_score[1]) + "\n\n"
        place += 1

    if canvas_score:
        canvas.delete(canvas_score)

    if canvas_words:
        canvas.delete(canvas_words)

    canvas_score = canvas.create_text(screen_width - 250, screen_height // 2 , text = score, font=("Arial Black", digit_font_size + 8, ""), fill="black")

    print("gata jocul !!!!")

player1 = take_tiles_from_bag_at_start()
player2 = take_tiles_from_bag_at_start()
if num_of_players > 2:
    player3 = take_tiles_from_bag_at_start()
if num_of_players > 3:
    player4 = take_tiles_from_bag_at_start()

player1_name = "BIA"
player2_name = "R\nA\nD\nU\n"
player3_name = "DARIA"
player4_name = "G\nD\nT\n"

player1_score = 0
player2_score = 0
player3_score = 0
player4_score = 0

score = player1_name + ": " + str(player1_score) + " puncte\n" + player2_name.replace("\n","") + ": " + str(player2_score) + " puncte\n"
if num_of_players > 2:
    score += player3_name.replace("\n","") + ": " + str(player3_score) + " puncte\n"

if num_of_players > 3:
    score +=player4_name.replace("\n","") + ": " + str(player4_score) + " puncte\n"

legend = "Aici apar cuvintele formate\nsi scorul acestora!"

player_turn = 1
letter_was_placed = True

board = [['' for _ in range(15)] for _ in range(15)]
word = []
letter = ""
letter_id = 0

permitted_words = []
try:

    with open("words.txt", 'r') as file:
        for line in file:
            permitted_words.append(line.replace('\n',''))

except FileNotFoundError:
    print("MISSING WORDS LIST")


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
                canvas.create_text(x1 + cell_size / 2, y1 + cell_size / 2, text=cell_type, font=("Arial Black", digit_font_size, "bold"), fill="black")

def draw_players_board():

    vector_x_start = board_x_start + 4 * cell_size
    vector_y_start = board_y_start + board_height + cell_size

    # down player 1
    for i in range(num_of_tiles_at_start):
        x1 = vector_x_start + i * cell_size
        y1 = vector_y_start
        x2 = x1 + cell_size
        y2 = y1 + cell_size

        canvas.create_rectangle(x1, y1, x2, y2, fill="lightblue", outline="black", width=line_weight)
        canvas.create_rectangle(x1+padding, y1+padding, x2-padding, y2-padding, fill=tile_fill, outline="black", width=line_weight - 2)

        if player1[i] != '':
            canvas.create_text(x1 + cell_size / 2,
                               y1 + cell_size / 2,
                               text=player1[i], font=("Arial Black", letter_font_size, "bold"), fill="black")

            canvas.create_text(x2 - 12.5,
                               y2 - 12.5,
                               text=scrabble_points[player1[i]], font=("Arial Black", digit_font_size, "bold"), fill="black")
        else:
            canvas.create_rectangle(x1, y1, x2, y2, fill="lightblue", outline="black", width=line_weight)

    vector_x_start = board_x_start + 4 * cell_size
    vector_y_start = board_y_start - cell_size - cell_size

    # up player 3
    if num_of_players > 2:
        for i in range(num_of_tiles_at_start):
            x1 = vector_x_start + i * cell_size
            y1 = vector_y_start
            x2 = x1 + cell_size
            y2 = y1 + cell_size

            canvas.create_rectangle(x1, y1, x2, y2, fill="lightblue", outline="black", width=line_weight)
            canvas.create_rectangle(x1+padding, y1+padding, x2-padding, y2-padding, fill=tile_fill, outline="black", width=line_weight - 2)

            if player3[i] != '':
                canvas.create_text(x1 + cell_size / 2,
                                   y1 + cell_size / 2,
                                   text=player3[i], font=("Arial Black", letter_font_size, "bold"), fill="black")

                canvas.create_text(x2 - 12.5,
                                   y2 - 12.5,
                                   text=scrabble_points[player3[i]], font=("Arial Black", digit_font_size, "bold"), fill="black")
            else:
                canvas.create_rectangle(x1, y1, x2, y2, fill="lightblue", outline="black", width=line_weight)

    vector_x_start = board_x_start + board_width + cell_size
    vector_y_start = board_y_start + 4 * cell_size

    # right player 2
    for i in range(num_of_tiles_at_start):
        x1 = vector_x_start
        y1 = vector_y_start + i * cell_size
        x2 = x1 + cell_size
        y2 = y1 + cell_size

        canvas.create_rectangle(x1, y1, x2, y2, fill="lightblue", outline="black", width=line_weight)
        canvas.create_rectangle(x1+padding, y1+padding, x2-padding, y2-padding, fill=tile_fill, outline="black", width=line_weight - 2)

        if player2[i] != '':
            canvas.create_text(x1 + cell_size / 2,
                               y1 + cell_size / 2,
                               text=player2[i], font=("Arial Black", letter_font_size, "bold"), fill="black")

            canvas.create_text(x2 - 12.5,
                               y2 - 12.5,
                               text=scrabble_points[player2[i]], font=("Arial Black", digit_font_size, "bold"), fill="black")
        else:
            canvas.create_rectangle(x1, y1, x2, y2, fill="lightblue", outline="black", width=line_weight)

    vector_x_start = board_x_start - cell_size - cell_size
    vector_y_start = board_y_start + 4 * cell_size

    # left player 4
    if num_of_players > 3:
        for i in range(num_of_tiles_at_start):
            x1 = vector_x_start
            y1 = vector_y_start + i * cell_size
            x2 = x1 + cell_size
            y2 = y1 + cell_size

            canvas.create_rectangle(x1, y1, x2, y2, fill="lightblue", outline="black", width=line_weight)
            canvas.create_rectangle(x1+padding, y1+padding, x2-padding, y2-padding, fill=tile_fill, outline="black", width=line_weight - 2)

            if player4[i] != '':
                canvas.create_text(x1 + cell_size / 2,
                                   y1 + cell_size / 2,
                                   text=player4[i], font=("Arial Black", letter_font_size, "bold"), fill="black")

                canvas.create_text(x2 - 12.5,
                                   y2 - 12.5,
                                   text=scrabble_points[player4[i]], font=("Arial Black", digit_font_size, "bold"), fill="black")

            else:
                canvas.create_rectangle(x1, y1, x2, y2, fill="lightblue", outline="black", width=line_weight)

def paint_score():

    global score, canvas_score
    p1n = player1_name.replace("\n", "")
    p2n = player2_name.replace("\n", "")
    p3n = player3_name.replace("\n", "")
    p4n = player4_name.replace("\n", "")

    score = ""

    score += p1n + " : " + str(player1_score) + " puncte\n"
    score += p2n + " : " + str(player2_score) + " puncte\n"
    if num_of_players > 2:
        score += p3n + " : " + str(player3_score) + " puncte\n"
    if num_of_players > 3:
        score += p4n + " : " + str( player4_score) + " puncte\n"

    if canvas_score:
        canvas.delete(canvas_score)
    canvas_score = canvas.create_text(screen_width - 200, 100, text = score, font=("Arial Black", digit_font_size + 8, ""), fill="black")

def clean_word_from_board(_wrd, player):

    for (l, c, r) in _wrd:
        board[c][r] = ''
        paint(r, c, "default")
        for i in range(num_of_tiles_at_start):
            if player[i] == '':
                player[i] = l
                break

def paint(col, row, _letter):

    x1 = board_x_start + col * cell_size
    y1 = board_y_start + row * cell_size
    x2 = x1 + cell_size
    y2 = y1 + cell_size

    canvas.create_rectangle(x1 + padding, y1 + padding, x2 - padding, y2 - padding, fill=tile_fill, outline="black", width=line_weight - 2)

    if _letter == '_':
        canvas.create_rectangle(x1, y1, x2, y2, fill="lightblue", outline="black", width=line_weight)

    if _letter != '' and _letter != '_' and _letter != 'default':
        canvas.create_text(x1 + cell_size / 2,
                           y1 + cell_size / 2,
                           text=_letter, font=("Arial Black", letter_font_size, "bold"), fill="black")

        canvas.create_text(x2 - 12.5,
                           y2 - 12.5,
                           text=scrabble_points[_letter], font=("Arial Black", digit_font_size, "bold"), fill="black")

    if _letter == "default":

        cell_type = get_cell_type(row, col)
        color = colors[cell_type]

        canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="black", width=line_weight)

        canvas.create_text(x1 + cell_size / 2,
                           y1 + cell_size / 2,
                           text=get_cell_type(row, col), font=("Arial Black", digit_font_size, "bold"), fill="black")

def get_crossed_words(wrd: [(str, int, int)]):

    initial = wrd.copy()

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
    for board_word in board_words:
        in_selected_letter = False
        for letter in board_word:
            if letter in initial:
                in_selected_letter = True
                break

        if in_selected_letter:
            filtered_words.append(board_word)

    print(f"Cuvinte formate: {filtered_words}")
    return filtered_words

def get_score(word_list):

    global legend, canvas_words

    legend = "CUVINTE FORMATE\n"
    canvas.delete(canvas_words)
    fs = 0
    double_w = False
    triple_w = False

    for _word in word_list:
        s = 0
        chained_letters = ""
        for l, r, c in _word:

            cell_type = get_cell_type(r,c)
            letter_score = scrabble_points[l]

            if cell_type == "DL":
                letter_score *= 2
            elif cell_type == "TL":
                letter_score *= 3

            elif cell_type == "DC":
                double_w = True
            elif cell_type == "TC":
                triple_w = True

            s += letter_score
            chained_letters += l.lower()

        if chained_letters not in permitted_words:
            legend = "Cuvantul \"" +  chained_letters.upper() + "\" NU\neste in dictionar!\nFii mai atent!\nTrecem la urmatorul jucator!"
            fs = 0
            break

        if double_w:
            s *= 2
        elif triple_w:
            s *= 3

        fs += s
        legend += " ● " + chained_letters.upper() + " : " + str(s) + "\n"


    canvas_words = canvas.create_text(screen_width - 200, screen_height - 200, text=legend, font=("Arial Black", digit_font_size + 8, ""), fill="black")
    return fs


def on_click(event):

    global player_turn, letter_was_placed, word, letter, player1, player2, player3, player4, letter_id, board, player1_score, player2_score, player3_score, player4_score

    player_placed_tile_on_board = False
    player_chose_tile_from_rack = False

    selected_row = (event.x - board_x_start) // cell_size
    selected_col = (event.y - board_y_start) // cell_size

    #player placed a letter onto the board
    if not letter_was_placed and board_x_start < event.x < board_x_start + board_width and board_y_start < event.y < board_y_start + board_height:

        if board[selected_col][selected_row] == '': #board tile was empty
            board[selected_col][selected_row] = letter
            player_placed_tile_on_board = True
            letter_was_placed = True

        if player_turn == 1 and player_placed_tile_on_board:

            if player1[letter_id] != '':
                word.append((player1[letter_id], selected_col, selected_row))
                letter = player1[letter_id]
                player1[letter_id] = ''
            show_finish_option_player1(True)

        elif player_turn == 2 and player_placed_tile_on_board:

            if player2[letter_id] != '':
                word.append((player2[letter_id], selected_col, selected_row))
                letter = player2[letter_id]
                player2[letter_id] = ''
            show_finish_option_player2(True)

        elif player_turn == 3 and player_placed_tile_on_board:

            if player3[letter_id] != '':
                word.append((player3[letter_id], selected_col, selected_row))
                letter = player3[letter_id]
                player3[letter_id] = ''
            show_finish_option_player3(True)

        elif player_turn == 4 and player_placed_tile_on_board:

            if player4[letter_id] != '':
                word.append((player4[letter_id], selected_col, selected_row))
                letter = player4[letter_id]
                player4[letter_id] = ''
            show_finish_option_player4(True)


    #player selected a letter from his rack
    if   player_turn == 1 and board_x_start + 4 * cell_size < event.x < board_x_start +  11  * cell_size and board_y_start + board_height + cell_size < event.y < board_y_start + board_height + 2 * cell_size:
        letter_id = (event.x - board_x_start) // cell_size - 4
        if player1[letter_id] != '':
            player_chose_tile_from_rack = True
            letter_was_placed = False

    elif player_turn == 2 and  board_x_start + board_width + cell_size < event.x < board_x_start + board_width + 2 * cell_size and board_y_start + 4 * cell_size < event.y < board_y_start + 11 * cell_size:
        letter_id = (event.y - board_y_start) // cell_size - 4
        if player2[letter_id] != '':
            player_chose_tile_from_rack = True
            letter_was_placed = False

    elif player_turn == 3 and board_x_start + 4 * cell_size < event.x < board_x_start +  11  * cell_size and board_y_start - 2 * cell_size  < event.y < board_y_start - cell_size:
        letter_id = (event.x - board_x_start) // cell_size - 4
        if player3[letter_id] != '':
            player_chose_tile_from_rack = True
            letter_was_placed = False

    elif player_turn == 4 and board_x_start - 2 * cell_size < event.x < board_x_start - cell_size and board_y_start + 4 * cell_size < event.y < board_y_start + 11 * cell_size:
        letter_id = (event.y - board_y_start) // cell_size - 4
        if player4[letter_id] != '':
            player_chose_tile_from_rack = True
            letter_was_placed = False


    #player pressed check my word
    if   player_turn == 1 and board_x_start + 12 * cell_size < event.x < board_x_start +  13 * cell_size and board_y_start + board_height + cell_size < event.y < board_y_start + board_height + 2 * cell_size:
        player_turn = 1 + player_turn % num_of_players
        show_finish_option_player1(False)

        word = sorted(word, key=lambda e: [e[1], e[2]])
        sc = get_score(get_crossed_words(word))
        if sc != 0:
            take_tiles_from_bag_after_word(player1)
            player1_score += sc
        else:
            clean_word_from_board(word, player1)

        if check_player_bag_empty(player1):
            game_over()
            return

        word.clear()
        draw_players_board()
        show_turn_player2()

    elif player_turn == 2 and board_x_start + board_width + cell_size < event.x <  board_x_start + board_width + 2 * cell_size and board_y_start + 12 * cell_size < event.y < board_y_start + 13 * cell_size:
        player_turn = 1 + player_turn % num_of_players
        show_finish_option_player2(False)

        word = sorted(word, key=lambda e: [e[1], e[2]])
        sc = get_score(get_crossed_words(word))
        if sc != 0:
            take_tiles_from_bag_after_word(player2)
            player2_score += sc
        else:
            clean_word_from_board(word, player2)

        if check_player_bag_empty(player2):
            game_over()
            return

        word.clear()
        draw_players_board()
        if num_of_players > 2:
            show_turn_player3()
        else:
            show_turn_player1()

    elif player_turn == 3 and board_x_start + 12 * cell_size < event.x < board_x_start +  13 * cell_size and board_y_start - 2 * cell_size < event.y < board_y_start - cell_size:
        player_turn = 1 + player_turn % num_of_players
        show_finish_option_player3(False)

        word = sorted(word, key=lambda e: [e[1], e[2]])
        sc = get_score(get_crossed_words(word))
        if sc != 0:
            take_tiles_from_bag_after_word(player3)
            player3_score += sc
        else:
            clean_word_from_board(word, player3)

        if check_player_bag_empty(player3):
            game_over()
            return

        word.clear()
        draw_players_board()
        if num_of_players > 3:
            show_turn_player4()
        else:
            show_turn_player1()

    elif player_turn == 4 and board_x_start - 2 * cell_size < event.x <  board_x_start - cell_size and board_y_start + 12 * cell_size < event.y < board_y_start + 13 * cell_size:
        player_turn = 1 + player_turn % num_of_players
        show_finish_option_player4(False)

        word = sorted(word, key=lambda e: [e[1], e[2]])
        sc = get_score(get_crossed_words(word))
        if sc != 0:
            take_tiles_from_bag_after_word(player4)
            player4_score += sc
        else:
            clean_word_from_board(word, player4)

        if check_player_bag_empty(player4):
            game_over()
            return

        word.clear()
        draw_players_board()
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

    paint_score()

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

    if num_of_players == 4 and canvas_player_turns[3]:
        canvas.delete(canvas_player_turns[3])
    elif num_of_players == 3 and canvas_player_turns[2]:
        canvas.delete(canvas_player_turns[2])
    elif num_of_players == 2 and canvas_player_turns[1]:
        canvas.delete(canvas_player_turns[1])

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
window.state("zoomed")
window.title("Radu's Scrabble")

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
board_width = board_size * cell_size
board_height = board_size * cell_size
board_x_start = (screen_width - board_width) // 2
board_y_start = (screen_height - board_height) // 2

canvas = tk.Canvas(window, width=screen_width, height=screen_height, bg="lightgray")
canvas.pack()
canvas_score = canvas.create_text(screen_width - 200, 100, text = score, font=("Arial Black", digit_font_size + 8, ""), fill="black")
canvas_words = canvas.create_text(screen_width - 200, screen_height - 200, text = legend, font=("Arial Black", digit_font_size + 8, ""), fill="black")


draw_scrabble_board()
draw_players_board()
show_turn_player1()

canvas.bind(click, on_click)
window.mainloop()