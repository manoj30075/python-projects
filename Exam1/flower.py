import turtle as t
import sys

colors = ["pink", "green"]
t.speed(0)

def draw_circle(radius, color):
    t.color(color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()


def draw_petal(radius, petal_color, main_color):
    t.color(main_color)
    t.forward(radius*3)
    t.left(90)
    t.color(petal_color)
    draw_circle(radius/3, petal_color)
    t.right(90)
    t.color(main_color)
    t.back(radius*3)


def draw_flower(radius):
    draw_circle(radius, "pink")
    t.left(90)
    t.forward(radius)
    t.right(90)

    for i in range(6):
        draw_petal(radius, "green", "pink")
        t.left(360/6)

def draw_nested_flower(radius, depth):
    sum = radius * 2
    if depth == 1:
        draw_circle(radius, colors[depth%2])
        sum = radius*2
    else:
        draw_circle(radius, colors[depth%2])
        t.left(90)
        t.forward(radius)
        t.right(90)
        for i in range(6):
            t.color(colors[depth%2])
            t.forward(radius * 3)
            t.left(90)
            t.color(colors[depth%2])
            sum += draw_nested_flower(radius/3, depth-1)
            t.right(90)
            t.color(colors[depth%2])
            t.back(radius * 3)
            t.left(360/6)
    return sum

def main():
    inputs = sys.argv[1:]
    depth = int(inputs[0])
    radius = int(inputs[1])
    print("Total diameter:" + str(draw_nested_flower(radius, depth)))

if __name__ == "__main__":
    main()
    t.mainloop()