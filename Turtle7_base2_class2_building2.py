import turtle
import random
import time

ENEMY_COUNT = 1
BASE_X, BASE_Y = 0, -270
BUILDING_INFOS = {
    "satelit_left": [BASE_X - 500, BASE_Y],
    "dron_left": [BASE_X - 250, BASE_Y],
    "fighter": [BASE_X, BASE_Y],
    "dron_right": [BASE_X + 250, BASE_Y],
    "satelit_right": [BASE_X + 500, BASE_Y]
}


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
        pen.setpos(x=x, y=y)
        pen.pendown()
        heading = pen.towards(x2, y2)
        pen.setheading(heading)
        pen.showturtle()
        self.pen = pen
        self.state = "launched"
        self.target = x2, y2
        self.radius = 0

    def step(self):
        if self.state == "launched":
            self.pen.forward(4)
            if self.pen.distance(x=self.target[0], y=self.target[1]) < 20:
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


class Building:
    INITIAL_HEALTH = 10000

    def __init__(self, x, y, name):
        self.name = name
        self.x = x
        self.y = y
        self.health = self.INITIAL_HEALTH

        pen = turtle.Turtle()
        pen.hideturtle()
        pen.speed(0)
        pen.penup()
        pen.setpos(x=self.x, y=self.y)
        pic_path = "images/" + self.get_pic_name()
        print(pic_path)
        window.register_shape(pic_path)
        pen.shape(pic_path)
        pen.showturtle()
        self.pen = pen

        title = turtle.Turtle(visible=False)
        title.speed(0)
        title.penup()
        title.setpos(x=self.x, y=self.y - 50)
        title.write(str(self.health), align="center", font=["Arial", 14, "bold"])
        self.title = title
        self.title_health = self.health

    def get_pic_name(self):
        if self.health < self.INITIAL_HEALTH * 0.2:
            return self.name + "3.gif"
        if self.health < self.INITIAL_HEALTH * 0.5:
            return self.name + "2.gif"
        if self.health < self.INITIAL_HEALTH * 0.8:
            return self.name + "1.gif"
        return self.name + ".gif"

    def draw(self):
        pic_name = self.get_pic_name()
        pic_path = "images/" + pic_name
        if self.pen.shape() != pic_path:
            window.register_shape(pic_path)
            self.pen.shape(pic_path)
        if self.health != self.title_health:
            self.title_health = self.health
            self.title.clear()
            self.title.write(str(self.title_health), align="center", font=["Arial", 14, "bold"])

    def is_alive(self):
        return self.health >= 0


def fire_missile(x, y):
    info = Missile(color="white", x=BASE_X, y=BASE_Y, x2=x, y2=y)
    our_missiles.append(info)


def fire_enemy_missile():
    x = random.randint(-700, 700)
    y = 350
    alive_buildings = [b for b in buildings if b.is_alive()]
    if alive_buildings:
        target = random.choice(alive_buildings)
        info = Missile(color="red", x=x, y=y, x2=target.x, y2=target.y)
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
            if enemy_missile.distance(our_missile.get_x(), our_missile.get_y()) < our_missile.radius * 10:
                enemy_missile.state = "dead"


def game_over():
    for building in buildings:
        if building.health <= 0:
            return building.health < 0


def check_impact():
    for enemy_missile in enemy_missiles:
        if enemy_missile.state != "explode":
            continue
        for building in buildings:
            if enemy_missile.distance(building.x, building.y) < enemy_missile.radius * 10:
                building.health -= 100
            print(str(building.name), ' - ', str(building.health))


def draw_buildings():
    for building in buildings:
        building.draw()


window = turtle.Screen()
window.setup(1200 + 10, 648 + 10)
window.bgpic("images/background2.png")
window.screensize(1300, 648)


def game():
    global our_missiles, enemy_missiles, buildings

    window.clear()
    window.bgpic("images/background2.png")
    window.tracer(n=4)
    window.onclick(fire_missile)

    our_missiles = []
    enemy_missiles = []
    buildings = []

    for name, position in BUILDING_INFOS.items():
        base = Building(x=position[0], y=position[1], name=name)
        buildings.append(base)

    while True:
        window.update()
        if game_over():
            break
        draw_buildings()
        check_impact()
        check_enemy_count()
        check_interceptions()
        move_missiles(missiles=our_missiles)
        move_missiles(missiles=enemy_missiles)
        time.sleep(.01)

    pen = turtle.Turtle(visible=False)
    pen.speed(0)
    pen.penup()
    pen.color("red")
    pen.write("Game over", align="center", font=["Arial", 80, "bold"])


while True:
    game()
    answer = window.textinput(title="Hi!", prompt="Do you want to try yet? Y/N")
    if answer.lower() not in ("yes", "y", "da", "да", "так", "д", "т"):
        break
