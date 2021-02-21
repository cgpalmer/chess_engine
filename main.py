position = "a1"
character = "king"

pieces = {
    'king': {
        'character': "king",
        'range': 1,
        'forwards': False,
        'backwards': True,  
        'left_right': True,
        'diagonal': True,           
        'current_position': 'A5'
        },
    'queen': {
        'character': "queen",
        'range': 8,
        'forwards': False,
        'backwards': True,
        'left_right': True,
        'diagonal': True,
        'current_position': 'E5'
    },
    'bishop': {
        'character': "bishop",
        'range': 8,
        'forwards': False,
        'backwards': False,
        'left_right': False,
        'diagonal': True,
        'current_position': 'A5'
    },
    'rook': {
        'character': "rook",
        'range': 8,
        'forwards': False,
        'backwards': True,
        'left_right': True,
        'diagonal': False,
        'current_position': 'A5'
    },
    'pawn': {
        'character': "pawn",
        'range': 1,
        'forwards': False,
        'backwards': False,
        'left_right': False,
        'diagonal': False, # For now false but in future try = cond on overtake.
        'current_position': 'A5'
    },
    'knight': {
        'character': "knight",
        'range': 1,
        'forwards': False,
        'backwards': True,
        'left_right': True,
        'diagonal': True,
        'current_position': 'A5'
    },
}


alphabet = []
for i in range(65, 91):
    alphabet.append(chr(i))


possible_moves = []


def possible_moves_right():
    c_pos = pieces[character_input]['current_position']
    letter_c_pos_index = alphabet.index(c_pos[0])
    for i in range(pieces[character_input]['range']):
        i = i + 1
        if (letter_c_pos_index + i) > 7:
            print("Can't move right")
        else:
            possible_moves.append(str(alphabet[(letter_c_pos_index+i)]) + str(c_pos[1]))


def possible_moves_left():
    c_pos = pieces[character_input]['current_position']
    letter_c_pos_index = alphabet.index(c_pos[0])
    for i in range(pieces[character_input]['range']):
        i = i + 1
        if (letter_c_pos_index - i) < 0:
            print("Can't move left")
        else:
            possible_moves.append(str(alphabet[(letter_c_pos_index - i)]) + str(c_pos[1]))


def possible_moves_forward():
    c_pos = pieces[character_input]['current_position']
    for i in range(pieces[character_input]['range']):
        i = i + 1
        if (int(c_pos[1])+i) > 8:
            print("invalid f")
        else:
            possible_moves.append(str(c_pos[0]) + str(int(c_pos[1]) + (i)))


def possible_moves_backward():
    c_pos = pieces[character_input]['current_position']
    for i in range(pieces[character_input]['range']):
        i = i + 1
        if (int(c_pos[1])-i) < 1:
            print("invalid b")
        else:
            possible_moves.append(str(c_pos[0]) + str(int(c_pos[1]) - (i)))


def possible_move_diagonal():
    c_pos = pieces[character_input]['current_position']
    letter_c_pos_index = alphabet.index(c_pos[0])
    for i in range(pieces[character_input]['range']):
        i = i + 1
        # diagonal up right
        if (int(c_pos[1])+i) > 8 or (letter_c_pos_index + i) > 7:
            print("invalid d")
        else:
            possible_moves.append(str(alphabet[(i+letter_c_pos_index)]) + str(int(c_pos[1])+i))
        # diagonal up left
        if (letter_c_pos_index - i) < 0 or (letter_c_pos_index + i) > 7:
            print("Can't move left")
        else:
            possible_moves.append(str(alphabet[(letter_c_pos_index-i)]) + str(int(c_pos[1])+i))
        # diagonal down left
        if (letter_c_pos_index - i) < 0 or (int(c_pos[1])-i) < 1:
            print("Can't move left")
        else:
            possible_moves.append(str(alphabet[(letter_c_pos_index-i)]) + str(int(c_pos[1])-i))
        # diagonal down right
        if (letter_c_pos_index + i) > 7 or (int(c_pos[1])-i) < 1:
            print("Can't move right")
        else:
            possible_moves.append(str(alphabet[(i+letter_c_pos_index)]) + str(int(c_pos[1])-i))


def find_characters_moves(character_input):
    if pieces[character_input]['backwards']:
        possible_moves_forward()
    if pieces[character_input]['backwards']:
        possible_moves_backward()
    if pieces[character_input]['left_right']:
        possible_moves_left()
        possible_moves_right()
    if pieces[character_input]['diagonal']:
        possible_move_diagonal()
    


print("Which character?")
character_input = input().lower()
print("You've chosen " + character_input)
find_characters_moves(character_input)

print(f"Piece's position is {pieces[character_input]['current_position']}. Here are the suggested moves: ")
print(possible_moves)
print("Where would you like to move the piece to?: ")
new_position = input().capitalize()
if new_position in possible_moves:
    print("this move is valid")
    pieces[character_input]['current_position'] = new_position
    print(f"Piece's new position is: {pieces[character_input]['current_position']}")
else:
    print("invalid move")
    print(f"Pieces's new position is: {pieces[character_input]['current_position']}")
