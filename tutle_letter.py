import turtle

def drawLetterM() -> None:
    """
    Draw letter M
    :pre: pos (25,0), heading east, up
    :post: pos (25,0), heading east, up
    :return: None
    """

    turtle.down()
    turtle.left(90)
    turtle.forward(40)
    turtle.right(135)
    turtle.forward(56.5)
    turtle.left(90)
    turtle.forward(56.5)
    turtle.right(135)
    turtle.forward(40)
    turtle.up()
    turtle.right(90)
    turtle.forward(80)
    turtle.left(180)

def drawLetterT() -> None:
    turtle.left(90)
    turtle.forward(40)
    turtle.right(90)
    turtle.down()
    turtle.forward(50)
    turtle.left(180)
    turtle.forward(25)
    turtle.left(90)
    turtle.forward(40)
    turtle.up()
    turtle.right(90)
    turtle.forward(25)
    turtle.left(180)

def drawLetterO() -> None:
    turtle.down()
    turtle.forward(30)
    turtle.left(90)
    turtle.forward(40)
    turtle.left(90)
    turtle.forward(30)
    turtle.left(90)
    turtle.forward(40)
    turtle.up()
    turtle.left(90)

def drawLetterH() -> None:
    turtle.right(90)
    turtle.down()
    turtle.forward(100)
    turtle.left(180)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(180)
    turtle.forward(100)
    turtle.left(90)
    turtle.up()
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(100)
    turtle.right(90)

if __name__ == '__main__':
    """
    """
    turtle.up()
    drawLetterH()
    turtle.mainloop()