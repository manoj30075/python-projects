"""
file: spellfixer.py
description: This program is to fix the spelling errors
             This program performs 4 operations
             1- accidentally hit a key adjacent to the intended one instead of the intended one
             2- Transpose two adjacent letters
             3- Add a letter
             4- Remove a letter
language: python3
author: Manoj Kumar Reddy Palasamudram , mp6112@rit.edu
        Ashwath Sreedhar Halemane, ah7387@rit.edu
"""
import sys


def process_file(file_name: str):
    """
    Pushes all the strings into an array
    :param file_name: file name which has to be processed
    :return: returns array of strings
    """
    file_values = []
    with open(file_name) as f:
        for line in f:
            file_values.append(line.strip())

    return file_values


def create_dict_for_keyboard_values(arr_of_arr):
    """
    create a dictionary for all the adjacent keys
    :param arr_of_arr: arrays of strings
    :return: returns a dict with key as a letter and values as letters adjacent to that letter
    """
    keyboard_dict = dict()

    for arr in arr_of_arr:
        keyboard_dict[arr[0]] = arr.split(' ')[1:]

    return keyboard_dict


def transpose_letter(word, words):
    """
    swap the letters and return if its a valid word in word list
    :param word: word which has to be corrected
    :param words: valid words in an array
    :return: return correct word
    """
    for i in range(len(word) - 1):
        swap_word_1 = word[i]
        swap_word_2 = word[i+1]
        new_word = word[:i] + swap_word_2 + swap_word_1 + word[i+2:]
        if new_word in words:
            return new_word

    return word


def add_a_letter(word, words):
    """
    Add a same letter adjacent to it and check if its a valid word and return
    :param word: word to be corrected
    :param words: valid words
    :return: returns corrected word
    """
    for i in range(len(word)):
        new_word = word[:i+1] + word[i:]
        if new_word in words:
            return new_word

    return word


def remove_a_letter(word, words):
    """
    remove letter and check if its a valid word
    :param word: word that is to be corrected
    :param words: valid words
    :return: returns corrected word
    """
    for i in range(len(word)):
        new_word = word[:i] + word[i+1:]
        if new_word in words:
            return new_word

    return word


def find_correct_spelling(word, words, keyboard_dict):
    """
    replace adjacent letters of a letter in key board and return if it is valid word
    :param word: word that is to be corrected
    :param words: valid words
    :param keyboard_dict: adjacent letters key value pair dict
    :return: returns corrected word
    """
    if word not in words:
        for index, letter in enumerate(word):
            replaced_word = word
            if letter in keyboard_dict.keys():
                for next_to_letter in keyboard_dict[letter.lower()] or []:
                    temp_list = list(replaced_word)
                    temp_list[index] = next_to_letter
                    replaced_word = "".join(temp_list)
                    if replaced_word in words:
                        return replaced_word

    return word


def process_user_input(user_input, words, keyboard_dict):
    """
    correct the user input string
    :param user_input: user input string
    :param words: valid words
    :param keyboard_dict: adjacent letters key value pair dict
    :return: returns corrected string
    """
    all_words_in_user_input = user_input.strip().split(' ')
    correct_words = []

    for word in all_words_in_user_input:
        correct_spelling = find_correct_spelling(word, words, keyboard_dict)
        if correct_spelling not in words and len(word) > 1:
            correct_spelling = transpose_letter(correct_spelling, words)
        if correct_spelling not in words and len(word) > 1:
            correct_spelling = add_a_letter(correct_spelling, words)
        if correct_spelling not in words and len(word) > 1:
            correct_spelling = remove_a_letter(correct_spelling, words)

        correct_words.append(correct_spelling)

    print(" ".join(correct_words))


def start_spell_checker(words, keyboard_dict):
    """
    spell fixer initial function
    :param words: valid words
    :param keyboard_dict: adjacent letters key value pair dict
    :return: None
    """
    print("Welcome to spell checker")
    while True:
        user_input = input(">")
        if user_input == '!*!':
            print("Bye!")
            break
        process_user_input(user_input, words, keyboard_dict)


def main():
    """
    process the files and start the spell fixer program
    :return: None
    """
    file_names = sys.argv[1:]
    words_file = file_names[0]
    keyboard_file = file_names[1]

    words = process_file(words_file)
    processed_keyboard_file = process_file(keyboard_file)
    # making valid words to lower case
    lower_case_words = list(map(lambda word: word.lower(), words))
    keyboard_dict = create_dict_for_keyboard_values(processed_keyboard_file)

    start_spell_checker(lower_case_words, keyboard_dict)


if __name__ == "__main__":
    main()


def merge(left, right):
    arr = []
    right_index = 0
    left_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            arr.append(left[left_index])
            left_index += 1
        else:
            arr.append(right[right_index])
            right_index += 1

    if right_index < len(right):
        arr.extend(right)

    if left_index < len(left):
        arr.extend(left)

    return arr


def merge_sort(array):
    if len(array) == 1:
        return array
    mid = len(array)//2

    return merge(merge_sort(array[:mid]), merge_sort(array[mid+1:]))

