message = "CrashServer"
nbr_line = 1500
line_list = []

def setup():
    global f, nbr_line, message
    size(400,400)
    f = createFont("Arial", 20, True)
    frameRate(30)
    for i in range(nbr_line):
        line_list.append(Phrase(message, random(0,width), random(0,height)))

def draw():
    global f, line_list
    background(15)
    fill(255)
    textFont(f)
    for i in line_list:
        i.display()
        i.move()
    
class Phrase(object):
    def __init__(self, msg, x, y):
        self.msg = msg
        self.x = x
        self.y = y
        self.index = 0
        
    def display(self):
        textSize(random(16,32))
        fill(random(50,255))
        text(self.msg[self.index%len(self.msg)], self.x, self.y)
    
    def move(self):
        self.x += textWidth(self.msg[self.index%len(self.msg)])
        self.index += 1
        if self.x > width:
            self.x = 0
        
