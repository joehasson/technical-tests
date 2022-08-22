def letters_to_points(letter):
    letter = letter.lower()
    if letter in 'eaionrtlsu':
        return 1
    elif letter in 'dg':
        return 2
    elif letter in 'bcmp':
        return 3
    elif letter in 'fhvwy':
        return 4
    elif letter == 'k':
        return 5
    elif letter in 'jx':
        return 8
    elif letter in 'qz':
        return 10
    else:
        raise BaseException()
    
def calculate_score_for_word(word):
    return sum(letter_to_points(letter) for letter in word)
