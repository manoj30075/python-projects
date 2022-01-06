"""
file: pigdice.py
description: This program is replicate the pig dice game using turtle
language: python3
author: Manoj Kumar Reddy Palasamudram , mp6112@rit.edu
        Ashwath Sreedhar Halemane, ah7387@rit.edu
"""

import turtle
import random
from score import Keeper

is_game_completed = False

player_score = Keeper()
colors = ['green', 'red']

# dice side length
SIDE = 100
sc = turtle.Screen()
sc.setup(800, 600)
sc.register_shape('hold_turtle_button', ((30, 30), (75, 30), (75, 170), (30, 170)))

# turtle to print the player score
player_score_track = turtle.Turtle()

# turtle to print the hold button
hold_turtle = turtle.Turtle()


# turtle to draw the dice
drawing_turtle = turtle.Turtle()
drawing_turtle.up()
drawing_turtle.back(50)
drawing_turtle.speed(0)

# turtle to print the dice turn total
turn_total_turtle = turtle.Turtle()
turn_total_turtle.hideturtle()
turn_total_turtle.up()
turn_total_turtle.speed(0)


def hold_turtle_initialisation() -> None:
    """
    function to initialise the hold_turtle
    :return: None
    """
    hold_turtle.speed(0)
    hold_turtle.up()
    hold_turtle.hideturtle()
    hold_turtle.right(90)
    hold_turtle.forward(100)
    hold_turtle.left(90)
    hold_turtle.left(90)
    hold_turtle.forward(100)
    hold_turtle.right(180)
    hold_turtle.forward(100)
    hold_turtle.down()
    hold_turtle.pencolor('blue')
    style_hold = ('Arial', 25, 'bold')
    hold_turtle.write("Hold", font=style_hold, align='center')
    hold_turtle.up()
    hold_turtle.left(90)
    hold_turtle.down()
    hold_turtle.forward(40)
    hold_turtle.left(90)
    hold_turtle.forward(30)
    hold_turtle.left(90)
    hold_turtle.forward(80)
    hold_turtle.left(90)
    hold_turtle.forward(30)
    hold_turtle.left(90)
    hold_turtle.forward(40)
    hold_turtle.up()


def update_score() -> None:
    """
    This function updates the players scores
    :return: None
    """
    player_score_track.clear()
    style = ('Arial', 20, 'bold')
    player_score_track.speed(0)
    player_score_track.hideturtle()
    player_score_track.up()
    player_score_track.left(90)
    player_score_track.forward(250)
    player_score_track.right(90)
    player_score_track.back(300)
    player_score_track.color(colors[player_score.player])
    player_1_text = 'Player 1'
    if player_score.player == 0:
        player_1_text = player_1_text + ' *'
    player_score_track.write(player_1_text, font=style, align='center')
    player_score_track.right(90)
    player_score_track.forward(50)
    player_score_track.left(90)
    player_score_track.write(player_score.score[0], font=style, align='center')
    player_score_track.right(90)
    player_score_track.backward(50)
    player_score_track.left(90)
    player_score_track.forward(600)
    player_score_track.color(colors[1 - player_score.player])
    player_2_text = 'Player 2'
    if player_score.player == 1:
        player_2_text = player_2_text + ' *'
    player_score_track.write(player_2_text, font=style, align='center')
    player_score_track.right(90)
    player_score_track.forward(50)
    player_score_track.left(90)
    player_score_track.write(player_score.score[1], font=style, align='center')
    player_score_track.right(90)
    player_score_track.backward(50)
    player_score_track.left(90)
    player_score_track.back(300)
    player_score_track.right(90)
    player_score_track.forward(250)
    player_score_track.left(90)


def draw_dot_at_center() -> None:
    """
    This function is used to print the dot at center of dice
    :return: None
    """
    drawing_turtle.forward(SIDE/2)
    drawing_turtle.left(90)
    drawing_turtle.forward(SIDE/2)
    drawing_turtle.dot(10)
    drawing_turtle.left(180)
    drawing_turtle.forward(SIDE/2)
    drawing_turtle.right(90)
    drawing_turtle.forward(SIDE/2)
    drawing_turtle.left(180)


def draw_two() -> None:
    """
    This function is used to print the two of dice
    :return: None
    """
    drawing_turtle.back(SIDE/4)
    drawing_turtle.left(90)
    drawing_turtle.forward(SIDE/4)
    drawing_turtle.right(90)
    draw_dot_at_center()
    drawing_turtle.right(90)
    drawing_turtle.forward(SIDE/4)
    drawing_turtle.left(90)
    drawing_turtle.forward(SIDE/2)
    drawing_turtle.right(90)
    drawing_turtle.forward(SIDE/4)
    drawing_turtle.left(90)
    draw_dot_at_center()
    drawing_turtle.left(90)
    drawing_turtle.forward(SIDE/4)
    drawing_turtle.right(90)
    drawing_turtle.back(SIDE/4)


def draw_four() -> None:
    """
    This function is used to print the four of dice
    :return: None
    """
    draw_two()
    drawing_turtle.forward(SIDE)
    drawing_turtle.left(90)
    draw_two()
    drawing_turtle.right(90)
    drawing_turtle.back(SIDE)


def draw_five() -> None:
    """
    This function is used to print the five of dice
    :return: None
    """
    draw_four()
    draw_dot_at_center()


def draw_three() -> None:
    """
    This function is used to print the three of dice
    :return: None
    """
    draw_dot_at_center()
    draw_two()


def draw_six() -> None:
    """
    This function is used to print the six of dice
    :return: None
    """
    draw_four()
    drawing_turtle.left(90)
    drawing_turtle.forward(SIDE/4)
    drawing_turtle.right(90)
    draw_dot_at_center()
    drawing_turtle.right(90)
    drawing_turtle.forward(SIDE/2)
    drawing_turtle.left(90)
    draw_dot_at_center()
    drawing_turtle.left(90)
    drawing_turtle.forward(SIDE/4)
    drawing_turtle.right(90)


def draw_square() -> None:
    """
    This function is used to draw dice square
    :return: None
    """
    drawing_turtle.down()
    for i in range(0, 4):
        drawing_turtle.forward(SIDE)
        drawing_turtle.left(90)
    drawing_turtle.up()


def draw_dice(dice_digit) -> None:
    """
    This function is used to draw dice digit
    :param dice_digit: dice digit to print
    :return: None
    """
    draw_square()
    if dice_digit == 2:
        draw_two()
    elif dice_digit == 3:
        draw_three()
    elif dice_digit == 4:
        draw_four()
    elif dice_digit == 5:
        draw_five()
    elif dice_digit == 6:
        draw_six()
    else:
        draw_dot_at_center()


def player_score_draw() -> None:
    """
    This function which is used to update the score of the players when the player clicks on HOLD and also print
    the player ID when game is over
    :return: None
    """
    global is_game_completed
    player_score.score[player_score.player] = player_score.score[player_score.player] + player_score.points
    if player_score.score[player_score.player] >= 10:
        is_game_completed = True
        update_score()
        print_player_won(player_score.player + 1)
    else:
        player_score.points = 0
        player_score.switch_player()
        update_score()


def start_the_game(x, y) -> None:
    """
    This function is used to start the game with random integers of dice
    :param x: x-coordinate
    :param y: y-coordinate
    :return: None
    """
    if not is_game_completed:
        if -54 < x < 75 and -6 < y < 111:
            drawing_turtle.clear()
            drawing_turtle.up()
            random_integer = random.randint(1, 6)
            if random_integer == 1:
                player_score.points = 0
                player_score.switch_player()
                turn_total()
                update_score()
            else:
                player_score.add_points(random_integer)
                turn_total()

            draw_dice(random_integer)
        elif -45 < x < 45 and -99 < y < -68:
            player_score_draw()


def turn_total() -> None:
    """
    This function is used to print the turn total
    :return: None
    """
    turn_total_turtle.clear()
    turn_total_turtle.left(90)
    turn_total_turtle.forward(100)
    turn_total_turtle.right(90)
    style = ('Arial', 20)
    turn_total_turtle.write("Turn Total: " + str(player_score.points), font=style, align='center')
    turn_total_turtle.right(90)
    turn_total_turtle.forward(100)
    turn_total_turtle.left(90)


def print_player_won(player_won) -> None:
    """
    This function is used to print the player who has won the game
    :param player_won: player id who won
    :return: None
    """
    style = ('Arial', 20, 'bold')
    player_won_turtle = turtle.Turtle()
    player_won_turtle.up()
    player_won_turtle.hideturtle()
    player_won_turtle.speed(0)
    player_won_turtle.right(90)
    player_won_turtle.forward(250)
    player_won_turtle.left(90)
    player_won_turtle.write("Player " + str(player_won) + " won", font=style, align='center')


sc = turtle.Screen()
sc.setup(800, 600)
if __name__ == '__main__':
    """
    main function to initialise the game
    """
    hold_turtle_initialisation()
    turtle.onscreenclick(start_the_game)
    turn_total()
    draw_square()
    update_score()
    turtle.mainloop()
    sc.mainloop()

