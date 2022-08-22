import random

with open('dictionary.txt') as f:
    DICTIONARY_CONTENTS = f.readlines()

class Bag:
    def __init__(self):
        self.letters = ((['e'] * 12) + (['a', 'i'] * 9) + (['o'] * 8) +
            (['n','r','t'] * 6) + (['l','s','u','d'] * 4) + (['g'] * 3)
            + (['b','c','m','p','f','h','v','w','y'] * 2) + ['k','j','x','w','z'])
        random.shuffle(self.letters)

    def draw(self):
        return self.letters.pop()
    
class Player:
    def __init__(self, bag):
        self.rack = [bag.draw() for i in range(7)]


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
    return sum(letters_to_points(letter) for letter in word)

# def find_valid_word(letters):
#     for permutation in permute(letters):

#def bisect_search_dict()