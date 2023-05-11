#random - для подбора случайного числа
import math
import turtle
import random
import time
             
window = turtle.Screen()
window.setup(1300+10, 648 + 10)
window.bgpic("images/background.png")
window.screensize(1300, 648)
window.tracer(n=1.5)


base2_x = random.randint(-650, 650)
base2_y = 300

def calc_heading(x1, y1, x2, y2):
    length = ((x2-x1)**2 + (y2 - y1)**2)**(0.5)
    cos_alpha = (x2-x1)/length
    alpha = math.acos(cos_alpha)
    alpha = math.degrees(alpha)
    if y2 - y1 < 0:
        alpha = - alpha
    return alpha

def calc_length(x1, y1, x2, y2):
    length2 = ((x2-x1)**2 + (y2 - y1)**2)**(0.5)
    return length2

def fire_missile(x, y):
    missile = turtle.Turtle()
    missile.hideturtle()
    missile.speed(0)
    missile.color("white")
    missile.penup()
    missile.setpos(x = base2_x, y = base2_y)
    missile.pendown()
    heading = calc_heading(x1 = base2_x, y1 = base2_y, x2 = x, y2 = y)
    missile.setheading(heading)
    missile.showturtle()
##    get_length = calc_length(x1 = base2_x, y1 = base2_y, x2 = x, y2 = y)
##    missile.forward(get_length)
##    missile.shape("circle")
##    missile.shapesize(0.1)
##    missile.shapesize(0.2)
##    missile.shapesize(0.4)
##    missile.shapesize(0.6)
##    missile.shapesize(1)
##    missile.shapesize(1.6)
##    missile.shapesize(2.6)
##    missile.shapesize(4.2)
##    missile.clear()
##    missile.hideturtle()
    info = {"missile": missile, "target": [x, y], "state": "launched", "radius": 0} 
    our_missiles.append(info)

window.onclick(fire_missile)

our_missiles = []


while True:
    window.update()

    for info in our_missiles:
        state = info["state"]
        missile = info["missile"]
        if state == "launched":
            missile.forward(4)
            target = info["target"]
            if missile.distance(x = target[0], y = target[1]) < 20:
                info["state"] = "explode"
                missile.shape("circle")
        elif state == "explode":
            info["radius"] += 1
            if info["radius"] > 5:
                missile.clear()
                missile.hideturtle()
                info["state"] = "dead"
            else:            
                missile.shapesize(info["radius"])
        elif state == "dead":
            missile.clear()
            missile.hideturtle()
    dead_missiles = [info for info in our_missiles if info["state"] == "dead"]
    for dead in dead_missiles:
        our_missiles.remove(dead)
    
            


































