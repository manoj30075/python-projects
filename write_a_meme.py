"""
file: write_a_meme.py
description: Prints meme "TOM HELLO" on the screen using turtle library
language: python3
author: Manoj Kumar Reddy Palasamudram , mp6112@rit.edu
"""

from math import sqrt
import turtle

turtle.speed(3)
turtle.shape('arrow')
turtle.setup(1250, 900, 0, 0)
turtle.setworldcoordinates(0, -300, 1000, 255)


def draw_letter_t() -> None:
    """
    This function prints letter T
    :pre: starts (x,y+50), directed towards east, pen up
    :post: ends (x+75, y+50), directed towards east, pen up
    :return: None
    """
    turtle.pendown()
    turtle.forward(50)
    turtle.backward(25)
    turtle.right(90)
    turtle.forward(50)
    turtle.penup()
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.right(90)


def draw_letter_o() -> None:
    """
    This function prints letter O
    :pre: starts (x,y+50), directed towards east, pen up
    :post: ends (x+75, y+50), directed towards east, pen up
    :return: None
    """
    turtle.pendown()
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.penup()
    turtle.forward(75)


def draw_letter_m() -> None:
    """
    This function prints letter M
    :pre: starts (x,y+50), directed towards east, pen up
    :post: ends (x+75, y+50), directed towards east, pen up
    :return: None
    """
    turtle.up()
    hypotenuse = sqrt(50**2 + 25**2)
    turtle.right(90)
    turtle.forward(50)
    turtle.pendown()
    turtle.backward(50)
    turtle.left(30)
    turtle.forward(hypotenuse)
    turtle.left(120)
    turtle.forward(hypotenuse)
    turtle.right(150)
    turtle.forward(50)
    turtle.penup()
    turtle.left(90)
    turtle.forward(25)
    turtle.left(90)
    turtle.forward(50)
    turtle.right(90)


def draw_letter_l() -> None:
    """
    This function prints letter L
    :pre: starts (x,y+50), directed towards east, pen up
    :post: ends (x+75, y+50), directed towards east, pen up
    :return: None
    """
    turtle.pendown()
    turtle.right(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.penup()
    turtle.forward(25)
    turtle.left(90)
    turtle.forward(50)
    turtle.right(90)


def draw_letter_e() -> None:
    """
    This function prints letter E
    :pre: starts (x,y+50), directed towards east, pen up
    :post: ends (x+75, y+50), directed towards east, pen up
    :return: None
    """
    turtle.penup()
    turtle.forward(50)
    turtle.pendown()
    turtle.backward(50)
    turtle.right(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.penup()
    turtle.backward(50)
    turtle.right(90)
    turtle.backward(25)
    turtle.left(90)
    turtle.pendown()
    turtle.forward(50)
    turtle.penup()
    turtle.forward(25)
    turtle.left(90)
    turtle.forward(25)
    turtle.right(90)


def draw_letter_h() -> None:
    """
    This function prints letter H
    :pre: starts (x,y+50), directed towards east, pen up
    :post: ends (x+75, y+50), directed towards east, pen up
    :return: None
    """
    turtle.right(90)
    turtle.down()
    turtle.forward(50)
    turtle.left(180)
    turtle.forward(25)
    turtle.right(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(25)
    turtle.left(180)
    turtle.forward(50)
    turtle.left(90)
    turtle.up()
    turtle.forward(25)
    turtle.left(90)
    turtle.forward(50)
    turtle.right(90)


if __name__ == '__main__':
    """
    Prints the word 'TOM HELLO'
    """
    draw_letter_t()
    draw_letter_o()
    draw_letter_m()
    # gives space of 25 to the next letter
    turtle.forward(25)
    draw_letter_h()
    draw_letter_e()
    draw_letter_l()
    draw_letter_l()
    draw_letter_o()
    turtle.dot()
    turtle.down()
    side = 100

    for i in range(0, 4):
        for j in range(0, 4):
            turtle.forward(side)
            turtle.left(90)
        turtle.forward(side)
        side = side/2


turtle.done()
