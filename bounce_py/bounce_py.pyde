from balls import *
nb_balls = 2
balls_list = []


def setup():
    size(200,200, P2D)
    frameRate(60)
    global balls_list
    #a = Balls()
    for i in range(0,nb_balls):
        balls_list.append(Balls())
    
def draw():
    global balls_list
    background(15)
    for i in range(0, nb_balls):
        balls_list[i].move()
        balls_list[i].bounce()
        balls_list[i].display()    
    
