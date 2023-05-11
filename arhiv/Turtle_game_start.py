#random - для подбора случайного числа
import turtle
import random
                

window = turtle.Screen()
window.setup(1300+10, 648 + 10)
window.bgcolor("skyblue")
window.screensize(1300, 648)


def airplane (y):
    pen = turtle.Turtle()
    if y > 0:
        pen.color("white")
    else:
        pen.color("red")
    pen.shape("turtle")
    for current_x in [-200, 0, 200]:
        pen.penup()
        pen.setposition(current_x, y)
        pen.pendown()
        pen.circle(radius = 50)
        pen.forward(100)
        pen.circle(radius = random.randint(2, 100))

airplane (10)
airplane (-100)
window.mainloop()





