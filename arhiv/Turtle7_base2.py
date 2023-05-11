#random - для подбора случайного числа
import math
import turtle
import random
                

window = turtle.Screen()
window.setup(1200+10, 648 + 10)
window.bgpic("images/background.png")
window.screensize(1300, 648)
window.tracer(n=2)

ENEMY_COUNT = 5
BASE_X, BASE_Y = 0, -300
base_health = 2000

def create_missile(color, x, y, x2, y2):
    missile = turtle.Turtle(visible=False)
    missile.hideturtle()
    missile.speed(0)
    missile.color(color)
    missile.penup()
    missile.setpos(x = x, y = y)
    missile.pendown()
    heading = missile.towards(x2, y2)
    missile.setheading(heading)
    missile.showturtle()
    info = {"missile": missile, "target": [x2, y2], "state": "launched", "radius": 0} 
    return(info)



def fire_missile(x, y):
    info = create_missile(color = "white", x = BASE_X,  y = BASE_Y, x2 = x, y2 = y)
    our_missiles.append(info)

def fire_enemy_missile():
    x = random.randint(-700, 700)
    y = 350
    info = create_missile(color = "red", x = x,  y = y, x2 = BASE_X, y2 = BASE_Y)
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

def check_enemy_count():
    if len(enemy_missiles) < ENEMY_COUNT:
        fire_enemy_missile()
        
def check_interceptions():
    for our_info in our_missiles:
        if our_info["state"] != "explode":
            continue
        our_missile = our_info["missile"]
        for enemy_info in enemy_missiles:
            enemy_missile = enemy_info["missile"]
            if enemy_missile.distance(our_missile.xcor(), our_missile.ycor()) < our_info["radius"]*5:
                enemy_info["state"] = "dead"
def game_over():
    return base_health < 0

def check_impact():
    global base_health
    for enemy_info in enemy_missiles:
        if enemy_info["state"] != "explode":
            continue
        enemy_missile = enemy_info["missile"]
        if enemy_missile.distance(BASE_X, BASE_Y) < enemy_info["radius"]*10:
            base_health -= 10
                

window.onclick(fire_missile)

base = turtle.Turtle()
base.hideturtle()
base.speed(0)
base.penup()
base.setpos(x = BASE_X, y = BASE_Y+30)
pic_path = "images/base_fly4.gif"
window.register_shape(pic_path)
base.shape(pic_path)
base.showturtle()





our_missiles = []
enemy_missiles = []


while True:
    window.update()
    if game_over():
        continue
    check_impact()
    check_enemy_count()
    check_interceptions()
    move_missiles(missiles = our_missiles)
    move_missiles(missiles = enemy_missiles) 






























