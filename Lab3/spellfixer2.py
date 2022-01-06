import sys


def file_processor(file_name: str):
    file_values = []
    with open(file_name) as f:
        for line in f:
            file_values.append(line.strip())

    return file_values


def file_processor_for_dict(file_name: str):
    file_values = []
    with open(file_name) as f:
        for line in f:
            file_values.append(line.strip())

    keyboard_dict = dict()

    for arr in file_values:
        keyboard_dict[arr[0]] = arr.split(' ')[1:]

    return keyboard_dict


def create_dict_for_keyboard_values(arr_of_arr):
    keyboard_dict = dict()

    for arr in arr_of_arr:
        keyboard_dict[arr[0]] = arr.split(' ')[1:]

    return keyboard_dict


def adding_a_letter_to_corrected_word(to_correct_word, words_which_are_valid):
    for i in range(len(to_correct_word)):
        first_word = to_correct_word[:i+1]
        second_word = to_correct_word[i:]
        corrected_word = first_word + second_word
        if is_present_in_words(corrected_word, words_which_are_valid):
            return corrected_word

    return to_correct_word


def removing_a_letter_to_corrected_word(to_correct_word, words_which_are_valid):
    for i in range(len(to_correct_word)):
        first_word = to_correct_word[:i]
        second_word = to_correct_word[i+1:]
        corrected_word = first_word + second_word
        if is_present_in_words(corrected_word, words_which_are_valid):
            return corrected_word

    return to_correct_word


def is_present_in_words(word, words):
    return word in words


def get_replacing_word(to_correct_word, words_which_are_valid, keyboard_key_value_pair):
    for i, letter_to_correct in enumerate(to_correct_word):
        replaced_word = to_correct_word
        if letter_to_correct in keyboard_key_value_pair.keys():
            for next_letter in keyboard_key_value_pair[letter_to_correct.lower()] or []:
                temporary_list = list(replaced_word)
                temporary_list[i] = next_letter
                replacing_word = "".join(temporary_list)
                if is_present_in_words(replacing_word, words_which_are_valid):
                    return replacing_word
    return to_correct_word


def get_the_corrected_word(to_correct_word, words_which_are_valid, keyboard_key_value_pair):
    word_to_replace = to_correct_word
    if not is_present_in_words(to_correct_word, words_which_are_valid):
        word_to_replace = get_replacing_word(to_correct_word, words_which_are_valid, keyboard_key_value_pair)

    return word_to_replace


def correct_the_spelling(user_provided_string, words_which_are_valid, keyboard_key_value_pair):
    all_words_in_user_input_strip = user_provided_string.strip()
    split_words = all_words_in_user_input_strip.split(' ')
    corrected_words = []

    for index in range(len(split_words)):
        corrected_word = get_the_corrected_word(split_words[index], words_which_are_valid, keyboard_key_value_pair)
        if not is_present_in_words(corrected_word, words_which_are_valid):
            corrected_word = adding_a_letter_to_corrected_word(corrected_word, words_which_are_valid)
        if not is_present_in_words(corrected_word, words_which_are_valid):
            corrected_word = removing_a_letter_to_corrected_word(corrected_word, words_which_are_valid)

        corrected_words.append(corrected_word)

    return corrected_words


def spell_checker(words_which_are_valid, keyboard_key_value_pair):
    print("Welcome to spell checker")
    while True:
        user_provided_string = input(">")
        if user_provided_string != '!*!':
            corrected_words = correct_the_spelling(user_provided_string, words_which_are_valid, keyboard_key_value_pair)
            print(" ".join(corrected_words))
        else:
            print("Bye!")
            break


if __name__ == "__main__":
    words_file = sys.argv[1]
    keyboard_file = sys.argv[2]

    valid_words = file_processor(words_file)
    keyboard_with_key_value_pair = file_processor_for_dict(keyboard_file)

    spell_checker(valid_words, keyboard_with_key_value_pair)

