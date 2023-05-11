#random - для подбора случайного числа
import math
import turtle
import random
                

window = turtle.Screen()
window.setup(1300+10, 648 + 10)
window.bgpic("images/background.png")
window.screensize(1300, 648)
window.tracer(n=2)

ENEMY_COUNT = 4
BASE_X, BASE_Y = 0, -300



def fire_missile(x, y):
    missile = turtle.Turtle()
    missile.hideturtle()
    missile.speed(0)
    missile.color("white")
    missile.penup()
    missile.setpos(x = BASE_X, y = BASE_Y)
    missile.pendown()
    heading = missile.towards(x, y)
    missile.setheading(heading)
    missile.showturtle()
    info = {"missile": missile, "target": [x, y], "state": "launched", "radius": 0} 
    our_missiles.append(info)

def fire_enemy_missile():
    missile = turtle.Turtle()
    missile.hideturtle()
    missile.speed(0)
    missile.color("red")
    missile.penup()
    x = random.randint(-700, 700)
    y = 350
    missile.setpos(x = x, y = y)
    missile.pendown()
    heading = missile.towards(BASE_X, BASE_Y)
    missile.setheading(heading)
    missile.showturtle()
    info = {"missile": missile, "target": [BASE_X, BASE_Y], "state": "launched", "radius": 0} 
    enemy_missiles.append(info)

def move_missiles(missiles):
    for info in missiles:
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
    dead_missiles = [info for info in missiles if info["state"] == "dead"]
    for dead in dead_missiles:
        missiles.remove(dead)    
    
window.onclick(fire_missile)

our_missiles = []
enemy_missiles = []


while True:
    window.update()


    if len(enemy_missiles) < ENEMY_COUNT:
        fire_enemy_missile()
        
    move_missiles(missiles = our_missiles)
    move_missiles(missiles = enemy_missiles) 






























