from random import randint

LETTER_SCORES = {
    "A": 1,
    "E": 1,
    "I": 1,
    "O": 1,
    "U": 1,
    "L": 1,
    "N": 1,
    "R": 1,
    "S": 1,
    "T": 1,

    "D": 2,
    "G": 2,

    "B": 3,
    "C": 3,
    "M": 3,
    "P": 3,

    "F": 4,
    "H": 4,
    "V": 4,
    "W": 4,
    "Y": 4,

    "K": 5,

    "J": 8,
    "X": 8,

    "Q": 10,
    "Z": 10
}

LETTER_POOL = {
    'A': 9,
    'B': 2,
    'C': 2,
    'D': 4,
    'E': 12,
    'F': 2,
    'G': 3,
    'H': 2,
    'I': 9,
    'J': 1,
    'K': 1,
    'L': 4,
    'M': 2,
    'N': 6,
    'O': 8,
    'P': 2,
    'Q': 1,
    'R': 6,
    'S': 4,
    'T': 6,
    'U': 4,
    'V': 2,
    'W': 2,
    'X': 1,
    'Y': 2,
    'Z': 1
}

ALPHABET = list(LETTER_POOL.keys())

def draw_letters():
    letters = []   # create an empty list
    copia = LETTER_POOL.copy() # make a copy of the pool
    while len(letters) < 10: # while I wont fullfil all the letters
        position = randint(0, 25) # sort a position
        letter = ALPHABET[position]   # obtains the letter according with the sorted position
        if copia[letter] > 0: #first we verify if the letter is avaliable then if is avaliable we add in the it on the list with append
                letters.append(letter)
                copia[letter] -=1 
    return letters
    

def uses_available_letters(word, letter_bank): 
    word= word.upper()#convert all leters in a string uppercase 
    frequences = {} # create a frequency dictionary
    for letter in letter_bank:
        if letter in frequences:
                frequences[letter] +=1
        else:
                frequences[letter] =1

    # verify if there is the letter and if it respects the frequency
    for letter in word:
        print("dicionario de frequencias: ", frequences)
        if letter in frequences:
            if frequences[letter] >0:
                frequences[letter] -=1
            else:
                return False
        else:
                return False
        
    return True


def score_word(word):
    word= word.upper()#convert all leters in a string uppercase 
    score= 0
    for letter in word:
        if letter in LETTER_SCORES:#if the letter is in LETTER_SCORES, add its score
            score += LETTER_SCORES[letter]
    if len(word) >= 7 and len(word) <= 10:# Check if the word has between 7 and 10 letters
        score +=8
    return score


def get_highest_word_score(word_list):
    winning_word= ""
    winning_score= 0
    for word in word_list:# Check each word in the list
        if score_word(word) >  winning_score:
            winning_score = score_word(word)
            winning_word = word
            
        elif score_word (word)== winning_score:
            if len(word) == 10 and len(winning_word)!= 10:# Prefer a 10 letter word when the scores are the same
                winning_word = word # Update the winning word
            elif len(word) < len(winning_word) and len(winning_word)!= 10:
                winning_word = word

    return (winning_word,winning_score)