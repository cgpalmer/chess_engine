position = "a1"
character = "king"

king = {
    'character': "king",
    'range': 1,
    'backwards': 'yes',
    'left_right': 'yes',
    'diagonal': 'yes',
    'current_position': 'E3'
    }

alphabet = []
for i in range(65, 91):
    alphabet.append(chr(i))
# print(alphabet[1])


possible_moves = []
def possible_moves_right():
    c_pos = king['current_position']
    letter_c_pos_index = alphabet.index(c_pos[0])
    for i in range(king['range']):
        i = i + 1
        possible_moves.append(str(alphabet[(i+letter_c_pos_index)]) + str(c_pos[1]))


def possible_moves_left():
    c_pos = king['current_position']
    letter_c_pos_index = alphabet.index(c_pos[0])
    for i in range(king['range']):
        i = i + 1
        possible_moves.append(str(alphabet[(letter_c_pos_index - i)]) + str(c_pos[1]))


def possible_moves_forward():
    c_pos = king['current_position']
    for i in range(king['range']):
        i = i + 1
        possible_moves.append(str(c_pos[0]) + str(int(c_pos[1]) + (i)))

def possible_moves_backward():
    c_pos = king['current_position']
    for i in range(king['range']):
        i = i + 1
        possible_moves.append(str(c_pos[0]) + str(int(c_pos[1]) - (i)))

possible_moves_left()
possible_moves_right()
possible_moves_forward()
possible_moves_backward()


print(f"King's position is {king['current_position']}. Here are the suggested moves: ")
print(possible_moves)
print("Where would you like to move the king to?: ")
new_position = input()
king['current_position'] = new_position.capitalize()
print(f"Kings's new position is: {king['current_position']}")
