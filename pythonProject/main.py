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
    " ": "green",
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

scrabble_list = [letter for letter, count in scrabble_letters.items() for _ in range(count)]

def draw_tiles(num_tiles=7):
    global scrabble_list
    drawn_tiles = random.sample(scrabble_list, num_tiles)
    for tile in drawn_tiles:
        scrabble_list.remove(tile)
    return drawn_tiles
def fill_with_tiles(player):

    missing = sum(1 for tile in player if tile == '')

    drawn_tiles = random.sample(scrabble_list, missing)

    for tile in drawn_tiles:
        scrabble_list.remove(tile)

    for i in range(len(player)):
        if player[i] == '':
            player[i] = drawn_tiles.pop(0)


player1 = draw_tiles()
player2 = draw_tiles()
player3 = draw_tiles()
player4 = draw_tiles()

player_turn = 1
player_selected_tile = False
player_selected_letter = False

board = [[''] * 15] * 15
word = ""
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

def choose_a_tile(col, row, _letter):

    x1 = board_x_start + col * cell_size
    y1 = board_y_start + row * cell_size
    x2 = x1 + cell_size
    y2 = y1 + cell_size

    canvas.create_rectangle(x1 + 5.5, y1 + 5.5, x2 - 5.5, y2 - 5.5, fill="white", outline="black", width=line_weight - 2)

    if _letter == '_':
        canvas.create_rectangle(x1, y1, x2, y2, fill="lightblue", outline="black", width=line_weight)

    if _letter != '' and _letter != '_':
        canvas.create_text(x1 + cell_size / 2,
                           y1 + cell_size / 2,
                           text=_letter, font=("Arial Black", 14, "bold"), fill="black")

def on_click(event):

    global player_turn, player_selected_tile, player_selected_letter, word, letter, player1, player2, player3, player4, letter_id

    tile_placed = False
    player_letter_clicked = False
    player_id = 0

    #click inside the board
    if player_selected_letter and board_x_start < event.x < board_x_start + board_width and board_y_start < event.y < board_y_start + board_height:
        tile_placed = True
        player_selected_letter = False

        if player_turn == 1:

            if player1[letter_id] != '':
                word += player1[letter_id]
                letter = player1[letter_id]
                player1[letter_id] = ''
            draw_ok_player1(True)

        elif player_turn == 2:

            if player2[letter_id] != '':
                word += player2[letter_id]
                letter = player2[letter_id]
                player2[letter_id] = ''
            draw_ok_player2(True)

        elif player_turn == 3:

            if player3[letter_id] != '':
                word += player3[letter_id]
                letter = player3[letter_id]
                player3[letter_id] = ''
            draw_ok_player3(True)

        elif player_turn == 4:

            if player4[letter_id] != '':
                word += player4[letter_id]
                letter = player4[letter_id]
                player4[letter_id] = ''
            draw_ok_player4(True)

    #click into player slot

    if player_turn == 1 and board_x_start + 4 * cell_size < event.x < board_x_start +  11  * cell_size and board_y_start + board_height + cell_size < event.y < board_y_start + board_height + 2 * cell_size:
        player_id = 1
        letter_id = (event.x - board_x_start) // cell_size - 4
        if player1[letter_id] != '':
            player_letter_clicked = True
            player_selected_letter = True

    elif player_turn == 2 and  board_x_start + board_width + cell_size < event.x < board_x_start + board_width + 2 * cell_size and board_y_start + 4 * cell_size < event.y < board_y_start + 11 * cell_size:
        player_id = 2
        letter_id = (event.y - board_y_start) // cell_size - 4
        if player2[letter_id] != '':
            player_letter_clicked = True
            player_selected_letter = True

    elif  player_turn == 3 and board_x_start + 4 * cell_size < event.x < board_x_start +  11  * cell_size and board_y_start - 2 * cell_size  < event.y < board_y_start - cell_size:
        player_id = 3
        letter_id = (event.x - board_x_start) // cell_size - 4
        if player3[letter_id] != '':
            player_letter_clicked = True
            player_selected_letter = True

    elif player_turn == 4 and board_x_start - 2 * cell_size < event.x < board_x_start - cell_size and board_y_start + 4 * cell_size < event.y < board_y_start + 11 * cell_size:
        player_id = 4
        letter_id = (event.y - board_y_start) // cell_size - 4
        if player4[letter_id] != '':
            player_letter_clicked = True
            player_selected_letter = True

    selected_row = (event.x - board_x_start) // cell_size
    selected_col = (event.y - board_y_start) // cell_size



    if player_turn == 1 and board_x_start + 12 * cell_size < event.x < board_x_start +  13 * cell_size and board_y_start + board_height + cell_size < event.y < board_y_start + board_height + 2 * cell_size:
        player_turn = 2
        print(f"Player 1 a scris cuvantul: --{word}--\n")
        word=""
        draw_ok_player1(False)
        fill_with_tiles(player1)
        draw_players_board()


    elif player_turn == 2 and  board_x_start + board_width + cell_size < event.x <  board_x_start + board_width + 2 * cell_size and board_y_start + 12 * cell_size < event.y < board_y_start + 13 * cell_size:
        player_turn = 3
        print(f"Player 2 a scris cuvantul: --{word}--\n")
        word = ""
        draw_ok_player2(False)
        fill_with_tiles(player2)
        draw_players_board()


    if player_turn == 3 and board_x_start + 12 * cell_size < event.x < board_x_start +  13 * cell_size and board_y_start - 2 * cell_size < event.y < board_y_start - cell_size:
        player_turn = 4
        print(f"Player 3 a scris cuvantul: --{word}--\n")
        word = ""
        draw_ok_player3(False)
        fill_with_tiles(player3)
        draw_players_board()


    elif player_turn == 4 and  board_x_start - 2 * cell_size < event.x <  board_x_start - cell_size and board_y_start + 12 * cell_size < event.y < board_y_start + 13 * cell_size:
        player_turn = 1
        print(f"Player 4 a scris cuvantul: --{word}--\n")
        word = ""
        draw_ok_player4(False)
        fill_with_tiles(player4)
        draw_players_board()


    if tile_placed:
        choose_a_tile(selected_row, selected_col, letter)
        print("am pus o litera pe tabla de joc")

    if player_letter_clicked:
        choose_a_tile(selected_row, selected_col, '_')
        print(f"Player cu id: {player_id} a apasat pe litera {letter_id}")

def draw_ok_player1(draw):

    if draw:
        canvas.create_rectangle(board_x_start + 12 * cell_size,
                                board_y_start + board_height + 2 * cell_size,
                                board_x_start + 13 * cell_size,
                                board_y_start + board_height + cell_size,
                                fill="orange", outline="black", width=line_weight)

        canvas.create_text(board_x_start + 12 * cell_size + cell_size / 2,
                           board_y_start + board_height + cell_size + cell_size / 2,
                           text="OK?", font=("Arial Black", 10, "bold"), fill="black")
    else:
        canvas.create_rectangle(board_x_start + 12 * cell_size,
                                board_y_start + board_height + 2 * cell_size,
                                board_x_start + 13 * cell_size,
                                board_y_start + board_height + cell_size,
                                fill="lightgray", outline="lightgray", width=line_weight)
def draw_ok_player2(draw):
    if draw:
        canvas.create_rectangle(board_x_start + board_width + cell_size,
                                board_y_start + 12 * cell_size,
                                board_x_start + board_width + 2 * cell_size,
                                board_y_start + 13 * cell_size,
                                fill="orange", outline="black", width=line_weight)

        canvas.create_text(board_x_start + board_width + cell_size + cell_size / 2,
                           board_y_start + 12 * cell_size + cell_size / 2,
                           text="OK?", font=("Arial Black", 10, "bold"), fill="black")
    else:
        canvas.create_rectangle(board_x_start + board_width + cell_size,
                                board_y_start + 12 * cell_size,
                                board_x_start + board_width + 2 * cell_size,
                                board_y_start + 13 * cell_size,
                                fill="lightgray", outline="lightgray", width=line_weight)
def draw_ok_player3(draw):

    if draw:
        canvas.create_rectangle(board_x_start + 12 * cell_size,
                                board_y_start - cell_size,
                                board_x_start + 13 * cell_size,
                                board_y_start - 2 * cell_size,
                                fill="orange", outline="black", width=line_weight)

        canvas.create_text(board_x_start + 12 * cell_size + cell_size / 2, board_y_start - 2 * cell_size + cell_size / 2,
                           text="OK?", font=("Arial Black", 10, "bold"), fill="black")
    else:
        canvas.create_rectangle(board_x_start + 12 * cell_size,
                                board_y_start - cell_size,
                                board_x_start + 13 * cell_size,
                                board_y_start - 2 * cell_size,
                                fill="lightgray", outline="lightgray", width=line_weight)
def draw_ok_player4(draw):
    if draw:
        canvas.create_rectangle(board_x_start - 2 * cell_size,
                                board_y_start + 12 * cell_size,
                                board_x_start - cell_size,
                                board_y_start + 13 * cell_size,
                                fill="orange", outline="black", width=line_weight)

        canvas.create_text(board_x_start - 2 * cell_size + cell_size / 2,
                           board_y_start + 12 * cell_size + cell_size / 2,
                           text="OK?", font=("Arial Black", 10, "bold"), fill="black")
    else:
        canvas.create_rectangle(board_x_start - 2 * cell_size,
                                board_y_start + 12 * cell_size,
                                board_x_start - cell_size,
                                board_y_start + 13 * cell_size,
                                fill="lightgray", outline="lightgray", width=line_weight)

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

canvas.bind(click, on_click)
window.mainloop()