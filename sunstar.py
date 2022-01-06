"""
file: sunstar.py
description: This program is draw sequence diagrams
language: python3
author: Manoj Kumar Reddy Palasamudram , mp6112@rit.edu
        Ashwath Sreedhar Halemane, ah7387@rit.edu
"""

import turtle
import math
import re

PATTERN = r"[0-9]+"

def draw_line(n):
    """
    This function is used to draw forward line
    :param n: int length of the side
    :return: None
    """
    turtle.forward(n)


def draw_side(side, level, angle):
    """
    This function is used to draw a side of the sequence using user input
    :param side: length of the side
    :param level: level of the side
    :param angle: deflection angle
    :return: int total length
    """
    total_length = 0
    if level == 1:
        draw_line(side)
        total_length = side
    else:
        draw_line(side / 4)
        turtle.left(angle)
        total_length += side / 4
        total_length += draw_side((side / 4) / math.cos(math.radians(angle)), level - 1, angle)
        turtle.right(2 * angle)
        total_length += draw_side((side / 4) / math.cos(math.radians(angle)), level - 1, angle)
        turtle.left(angle)
        draw_line(side / 4)
        total_length += side / 4
    return total_length


def draw_sequence(no_of_sequence, side, level, angle, total_length, temp_sequence_var):
    """
    This function is used to draw the whole sequence
    :param no_of_sequence: no of sequences to be drawn
    :param side: length of side
    :param level: level of side
    :param angle: deflection angle
    :param total_length: total length to be calculated
    :param temp_sequence_var: temporary variable to store the no of sequence
    :return: int returns total length
    """
    if no_of_sequence == 0:
        pass
    else:
        total_length += draw_side(side, level, angle)
        turtle.right(360 / temp_sequence_var)
        total_length = draw_sequence(no_of_sequence - 1, side, level, angle, total_length, temp_sequence_var)

    return total_length


def user_input():
    """
    This function used to capture user inputs
    :return: None
    """
    u_input = 0
    angle_int = 0

    while True:
        try:
            u_input = input("Number of sides")
            sides_int = int(u_input)
            break
        except ValueError:
            print("Value must be an integer. You entered: " + str(type(u_input)))

    while True:
        try:
            u_input = input("Length of sides")
            length_int = int(u_input)
            break
        except ValueError:
            print("Value must be an integer. You entered: " + str(type(u_input)))

    while True:
        try:
            u_input = input("Number of levels")
            levels_int = int(u_input)
            break
        except ValueError:
            print("Value must be an integer. You entered: " + str(type(u_input)))

    if levels_int > 1:
        while True:
            try:
                u_input = input("Deflection angle")
                angle_int = int(u_input)
                break
            except ValueError:
                print("Value must be an integer. You entered: " + str(type(u_input)))

    total_length = 0

    total_length = draw_sequence(sides_int, length_int, levels_int, angle_int, total_length, sides_int)
    print("Total length is: " + str(total_length))


if __name__ == '__main__':
    turtle.speed(0)
    user_input()
    turtle.mainloop()
