class Balls(object):
    def __init__(self):
        self.ballsize = random(1,width/10)
        self.xpos = random(self.ballsize, width-self.ballsize)
        self.ypos = random(self.ballsize, height-self.ballsize)
        #self.ypos = self.ballsize
        self.xvelo = 3
        self.yvelo = 2.8
        self.color_fill = color(255,255,255)
        self.color_stroke = color(0)
        self.strokeW = 1

    def move(self):    
        #global xpos, ypos, xvelo, yvelo
        self.xpos += self.xvelo
        self.ypos += self.yvelo
        
    def bounce(self):
        #global xvelo, yvelo
        if self.xpos - self.ballsize/2 < 0 or self.xpos + self.ballsize/2 > width:
            self.xvelo *= -1
            self.color_stroke = color(random(255))
            self.strokeW = random(0.1,8)
        if  self.ypos - self.ballsize/2 < 0 or self.ypos + self.ballsize/2> height:
            self.yvelo *= -1
            self.color_fill = color(random(255))
            
    def display(self):
        fill(self.color_fill, random(255))
        stroke(self.color_stroke)
        strokeWeight(self.strokeW)
        ellipse(self.xpos, self.ypos, self.ballsize, self.ballsize)
