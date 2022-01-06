"""
file: auto_complete.py
description: This program does auto complete of the words when
            user inputs a letter
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


def find_last_index(string_arr, starting_index, prefix):
    """
    This function returns the last index of the prefix letter
    :param string_arr: sorted words array
    :param starting_index: starting index of the array
    :param prefix: prefix letter given by user
    :return: returns last index of the prefix word
    """
    for index in range(starting_index, len(string_arr)):
        if string_arr[index][:len(prefix)] != prefix:
            return index-1

    return starting_index


def _binary_search(data, val, left, right, starts_with_prefix):
    """
    binary searches the prefix index
    :param data: array to do binary search
    :param val: value to find the in the array with prefix
    :param left: left index of the array
    :param right: right index of the array
    :param starts_with_prefix: prefix of the word
    :return: return the index of exact match or starting prefix index
    """
    if left > right:
        if starts_with_prefix > -1:
            return starts_with_prefix
        return -1
    mid = (left + right)//2

    if data[mid][: len(val)] == val:
        if data[mid] == val:
            return mid
        return _binary_search(data, val, left, mid - 1, mid)
    if data[mid][: len(val)] >= val:
        return _binary_search(data, val, left, mid - 1, starts_with_prefix)
    else:
        return _binary_search(data, val, mid+1, right, starts_with_prefix)


def merge(left, right):
    """
    Performs merge of to arrays
    :param left: left array
    :param right: right array
    :return: returns sorted array
    """
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
        arr.extend(right[right_index:])

    if left_index < len(left):
        arr.extend(left[left_index:])

    return arr


def merge_sort(array):
    """
    Performs merge sort of the array
    :param array: array to which sort to be performed
    :return: sorted array -> ascending to descending
    """
    if len(array) == 1:
        return array
    mid = len(array)//2

    return merge(merge_sort(array[:mid]), merge_sort(array[mid:]))


def main():
    """
    Start program to perform the autofill part
    :return: None
    """
    args = sys.argv[0:]
    if len(args) < 2:
        print("Please provide words file name")
    else:
        words = process_file(args[1])
        lower_case_words = list(map(lambda word: word.lower(), words))
        sorted_words = merge_sort(lower_case_words)
        prefix_sorted_words = []
        index = 0

        while True:
            user_input = input("Enter the input")
            if user_input == '<QUIT>':
                break

            if user_input == '':
                index += 1
            else:
                index = 0
                start_index = _binary_search(sorted_words, user_input, 0, len(sorted_words), -1)
                last_index = find_last_index(sorted_words, start_index, user_input)
                prefix_sorted_words = sorted_words[start_index: last_index + 1]

            # To handle boundary case
            if index == len(prefix_sorted_words) or len(prefix_sorted_words) == 0:
                index = 0
                print(user_input)
            else:
                print(prefix_sorted_words[index])


if __name__ == '__main__':
    main()

