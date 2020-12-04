def setup():
    global rot, x, y, cubesize, b
    b = 50
    size(200,200)
    background(15)
    colorMode(HSB,width)
    rot = 0
    x = 0
    y = 0
    cubesize = width/10

def draw():
    global rot, x, y, cubesize, b
    fill(color(x,y,b))
    translate(x, y)
    rotate(rot)
    rect(0, 0, cubesize, cubesize)
    rot += random(0,15)
    x += 1
    b += 1
    if b > 1000:
        b=50
    if x > width:
        x=0
        y+= cubesize*2
    if y > height:
        y = 0
