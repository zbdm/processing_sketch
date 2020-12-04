def setup():
    size(400,400, P3D)
    stroke(155)
    strokeWeight(1)
    frameRate(1)
    background(55)
    f = loadFont("Algerian-48.vlw")
    textFont(f,30)
    textAlign(CENTER)
    
def draw():
    v1 = PVector(width/2 - random(0, width/2), height/2 - random(0, height/2)) 
    v2 = PVector(width/2 + random(0, width/2), height/2 + random(0, height/2))
                
    fill(0,0,255)
    text("LIBERTE", v1.x, v1.y)
    #ellipse(v1.x, v1.y, 12, 12)
    fill(255,0,0)
    #ellipse(v2.x, v2.y, 12, 12)
    text("FRATERNITE", v2.x, v2.y)
    if random(0,100) > 50:
        v2 += v1 # v2 += v1
    else:
        v2 -= v1
    fill(255)
    text("EGALITE", v2.x, v2.y)
    #ellipse(v2.x, v2.y, 24, 24)
