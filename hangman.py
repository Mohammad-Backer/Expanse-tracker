import json
import random


def get_words():
    with open('words_dictionary.json') as f:
        words = json.load(f)
        f.close()

    actual_words = list(words.keys())
    return actual_words

def random_word(list_words):
    word =  random.choice(list_words)
    while '-' in word or ' ' in word:
        word = random.choice(list_words)
    return word

def print_stars(word):
    word_length = len(word)
    s = ''
    for i in range(word_length):
        s += '-'
    return s

def replacer(s, newstring, index):
    return s[:index] + newstring + s[index + 1:]

def display_placement(letter, word, state):
    for i in range(len(word)):
        if letter == word[i]:
            state = replacer(state,letter,i)
    return state

if __name__ == "__main__":
    list_words = get_words()
    guessee = random_word(list_words)
    attempts = 10
    word_state = print_stars(guessee)
    print("The computer chose a word! Try guessing it!")
    print("Start by guessing a letter! you have 10 attempts.")
    print(f"This is the word: {print_stars(guessee)}")
    while attempts>0:
        guessed_letter = input("You letter is: ")
        if len(guessed_letter)>1:
            print("Type only one letter!")
        elif not guessed_letter.isalpha():
            print("It should be a letter!")
        else:
            if guessed_letter in guessee:
                word_state = display_placement(guessed_letter, guessee, word_state)
                if word_state == guessee:
                    print("You won!")
                    break
            else:
                attempts -= 1
        print(f"You still have {attempts} attempts")
        print(word_state)
    print(guessee)


