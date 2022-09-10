WORD = "Jan Kowalski"

temp_WORD_list = list(WORD)
letter_position = temp_WORD_list('a')
temp_WORD_list[letter_position] = 'S'
WORD = "".join(temp_WORD_list)

print(WORD)