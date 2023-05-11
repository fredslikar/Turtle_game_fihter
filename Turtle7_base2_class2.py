#random - для подбора случайного числа
import math
import turtle
import random
                

window = turtle.Screen()
window.setup(1200+10, 648 + 10)
window.bgpic("images/background2.png")
window.screensize(1300, 648)
window.tracer(n=2)

ENEMY_COUNT = 5
BASE_X, BASE_Y = 0, -300
base_health = 2000

class Missile:
    def __init__(self, x, y, color, x2, y2):
        self.x = x
        self.y = y
        self.color = color

        pen = turtle.Turtle(visible=False)
        pen.hideturtle()
        pen.speed(0)
        pen.color(color)
        pen.penup()
        pen.setpos(x = x, y = y)
        pen.pendown()
        heading = pen.towards(x2, y2)
        pen.setheading(heading)
        pen.showturtle()
        self.pen = pen
        self.state = "launched"
        self.target = x2, y2
        self.radius = 0
        

    def step (self):
        if self.state == "launched":
            self.pen.forward(4)
            if self.pen.distance(x = self.target[0], y = self.target[1]) < 20:
                self.state = "explode"
                self.pen.shape("circle")
        elif self.state == "explode":
            self.radius += 1
            if self.radius > 5:
                self.pen.clear()
                self.pen.hideturtle()
                self.state = "dead"
            else:            
                self.pen.shapesize(self.radius)
        elif self.state == "dead":
            self.pen.clear()
            self.pen.hideturtle()

    def distance(self, x, y):
        return self.pen.distance(x=x, y=y)

    def get_x(self):
        return self.pen.xcor()

    def get_y(self):
        return self.pen.ycor()



def fire_missile(x, y):
    info = Missile(color = "white", x = BASE_X,  y = BASE_Y, x2 = x, y2 = y)
    our_missiles.append(info)

def fire_enemy_missile():
    x = random.randint(-700, 700)
    y = 350
    info = Missile(color = "red", x = x,  y = y, x2 = BASE_X, y2 = BASE_Y)
    enemy_missiles.append(info)

def move_missiles(missiles):
    for missile in missiles:
        missile.step()

    dead_missiles = [missile for missile in missiles if missile.state == "dead"]
    for dead in dead_missiles:
        missiles.remove(dead)    

        
def check_enemy_count():
    if len(enemy_missiles) < ENEMY_COUNT:
        fire_enemy_missile()
        
def check_interceptions():
    for our_missile in our_missiles:
        if our_missile.state != "explode":
            continue
        for enemy_missile in enemy_missiles:
            if enemy_missile.distance(our_missile.get_x(), our_missile.get_y()) < our_missile.radius*10:
                enemy_missile.state = "dead"

def game_over():
    return base_health < 0

def check_impact():
    global base_health
    for enemy_missile in enemy_missiles:
        if enemy_missile.state != "explode":
            continue
        if enemy_missile.distance(BASE_X, BASE_Y) < enemy_missile.radius*10:
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






























