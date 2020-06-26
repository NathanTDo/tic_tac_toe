def check_if_number(input):
    try:
        number = int(input)
    except ValueError:
        return False, None
    return True, number

while True:
    dimensions = (input("X * X dimensions: "))
    is_int, dimensions = check_if_number(dimensions)
    if is_int == True:
        break
    else:
        print("Try putting a number")

game = []

for x in range(dimensions):
    game.append(['-'] * dimensions)

turn_count = 1

def print_board():
    col_number  = "  "
    global turn_count
    if turn_count < 10:
        turn_display = (" TURN: %s" + "\n") % (turn_count)
        print (turn_display)
    for i in range(dimensions):
        col_number += (str(i) + ' ')
    print(col_number)
    #print(range(dim))
    # print("  0 1 2")
    for count, row in enumerate(game):
        print(str(count) + " " + " ".join(row))

def set_coordinates(x, y, shape):
    game[x][y] = shape

def draw_condition():
    print("Game IS A DRAW!")

def check_win_condition(last_x, last_y):
    #x = 0
    #y = 0
    win_hor = True
    win_vert = True
    win_left_diag = True
    win_right_diag = True

    # vertical checker 2.0
    for x in range(dimensions):
        if (game[x][last_y] != game[last_x][last_y]):
            win_vert = False
    
    # horizontal checker
    for y in range(dimensions):
        if (game[last_x][y] != game[last_x][last_y]):
            win_hor = False

    # left diaganol check
    if last_x == last_y:
        for diag in range(dimensions):
            if game[diag][diag] != game[last_x][last_y]:
                win_left_diag = False
    else:
        win_left_diag = False
    
    #right diaganol check:
    if (last_x + last_y) == dimensions: # to-do: make 2 a variable and argument of range variable + 1
        for diag in range(dimensions):
            if game[2 - diag][diag] != game[last_x][last_y]:
                win_right_diag = False
    else:
        win_right_diag = False

    return win_hor or win_vert or win_left_diag or win_right_diag

def validate_input(input):
    if not is_in_boundary(input):
        print("That is not in the boundary")
        print_board()
        return False
    return True

def is_in_boundary(input):
    global dimensions
    return (input >= 0 and input <= dimensions)

def get_player_input(player_name, shape):
    while True:
        #Prompt player 1 for row choice and column choice
        guess_row = (input("\n" +  "%s\'s Row Choice: " % (player_name)))
        is_number, guess_row = check_if_number(guess_row)
        if is_number == False:
            print_board()
            continue
        if validate_input(guess_row) == False:
            continue
        guess_col = (input("%s\'s Column Choice: " % (player_name)))
        is_number, guess_col = check_if_number(guess_col)
        if is_number == False:
            print_board()
            continue
        if validate_input(guess_col) == False:
            continue
        print(" ")

        #Reprint the game board with updated state
        if game[guess_row][guess_col] == '-':
            set_coordinates(guess_row, guess_col, shape)
            return (guess_row, guess_col)
        else:
            print("\n" + "Oops, that spot was boonked already, please enter another answer \n")
            print_board()

def exec_turn(player_name, shape):
    global turn_count
    guess_row, guess_col = get_player_input(player_name, shape)
    turn_count += 1
    print_board()

    #Check for win condition
    if check_win_condition(guess_row, guess_col) == True:
        print("YOU WIN!")
        return True
    if turn_count == 10:
        draw_condition()
        return True
    return False


# #Ask for name of player 1
print("Please Enter Your Name")
name_P1 = input("Player 1: ")

#Ask for name of player 2
name_P2 = input("Player 2: ")
print(" ")

#Print game board
print_board()

P1_turn_flag = True
while True:
    if P1_turn_flag == True:
        name = name_P1
        shape = "X"
    else:
        name = name_P2
        shape = "O"
    
    game_finish = exec_turn(name, shape)
    if game_finish:
        break
    P1_turn_flag = not P1_turn_flag































