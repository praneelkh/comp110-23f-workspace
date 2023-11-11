"""EX05 - A peaceful drawing of a house with a forest and a lake with a boat."""
 
__author__ = "730663941"


from turtle import Turtle, done
import random


def draw_rectangle(t1: Turtle, x: float, y: float, width: float, height: float, fill_color: str, line_color: str) -> None:
    """Draws a rectangle using a turtle object.
    
    param t: The turtle object.
    param x, y: Coordinates to start drawing.
    param width: Width of the rectangle.
    param height: Height of the rectangle.
    param fill_color: Fill color of the rectangle.
    param line_color: Line color of the rectangle.
    """
    t1.penup()
    t1.goto(x, y)
    t1.pendown()
    t1.color(line_color, fill_color)
    t1.begin_fill()
    for _ in range(2):
        t1.forward(width)
        t1.left(90)
        t1.forward(height)
        t1.left(90)
    t1.end_fill()


def draw_triangle(t2: Turtle, x: float, y: float, size: float, fill_color: str, line_color: str) -> None:
    """Draws a triangle using a turtle object.
    
    param t: The turtle object.
    param x, y: Coordinates to start drawing.
    param size: Size of the equilateral triangle's side.
    param fill_color: Fill color of the triangle.
    param line_color: Line color of the triangle.
    """
    t2.penup()
    t2.goto(x, y)
    t2.pendown()
    t2.color(line_color, fill_color)
    t2.begin_fill()
    for _ in range(3):
        t2.forward(size)
        t2.left(120)
    t2.end_fill()


def draw_tree(t3: Turtle, x: float, y: float) -> None:
    """Draws a tree using a turtle object.

    param t: The turtle object.
    param x, y: Coordinates to start drawing.
    """
    draw_rectangle(t3, x, y, 20, 40, "saddlebrown", "black")  # tree trunk
    draw_triangle(t3, x - 30, y + 40, 80, "green", "black")      # tree foliage


def draw_path(t4: Turtle, x: float, y: float, width: float, height: float) -> None:
    """Draws a path leading to the house.

    param t: The turtle object.
    param x, y: Coordinates to start drawing.
    param width: Width of the path.
    param height: Height of the path.
    """
    draw_rectangle(t4, x, y, width, height, "tan", "tan")


def draw_circle(t5: Turtle, x: float, y: float, radius: float, fill_color: str, line_color: str) -> None:
    """Draws a circle using a turtle object.
    
    param t: The turtle object.
    param x, y: Coordinates to start drawing.
    param radius: Radius of the circle.
    param fill_color: Fill color of the circle.
    param line_color: Line color of the circle.
    """
    t5.penup()
    t5.goto(x, y - radius)
    t5.pendown()
    t5.color(line_color, fill_color)
    t5.begin_fill()
    t5.circle(radius)
    t5.end_fill()


def main() -> None:
    """The main function that creates the scene."""
    Turtle().getscreen().bgcolor("skyblue")
    t: Turtle = Turtle()
    t.speed(10)   # Increase speed for faster drawing
    # Draw sun in the sky
    draw_circle(t, -200, 150, 40, "yellow", "yellow")
    # Draw house base
    draw_rectangle(t, -75, -100, 150, 100, "yellow", "black")
    # Draw house roof
    draw_triangle(t, -75, 0, 150, "red", "black")
    # Draw door in the house
    draw_rectangle(t, -25, -100, 50, 60, "brown", "black")
    # Draw windows using a loop
    for x, y in [(-60, -50), (10, -50)]:
        draw_rectangle(t, x, y, 40, 40, "blue", "black")
    # Draw path leading to the house
    draw_path(t, -25, -140, 50, 40)
    # Draw trees around the house 
    draw_tree(t, -150, -70)
    draw_tree(t, 120, -70)
    # Draw a lake to the side
    draw_circle(t, 220, -130, 70, "blue", "blue")
    # Draw a boat on the lake
    draw_rectangle(t, 180, -130, 40, 10, "brown", "black")
    draw_triangle(t, 220, -130, 40, "brown", "black")
    # Drawing multiple random trees in the scene, but ensuring they don't cover the house
    for _ in range(10):
        x = random.randint(-300, -200)
        draw_tree(t, x, -70)
    t.hideturtle()  # Hide turtle after drawing
    done()


if __name__ == "__main__":
    main()