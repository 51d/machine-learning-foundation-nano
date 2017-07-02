#drawing a circle out of sqaures
import turtle
def draw_sqaure(a):
    for i in range(1,5):
        a.forward(100)
        a.right(90)
def draw_circle():
    window = turtle.Screen()
    window.bgcolor('red')
    b = turtle.Turtle()
    b.shape('arrow')
    b.color('blue')
    b.speed(5)
    for i in range(1,37):
        draw_sqaure(b)
        b.right(10)
    window.exitonclick()

draw_circle()
