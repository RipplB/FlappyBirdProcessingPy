bird = None
deadline = 150

def setup():
    global bird
    fullScreen()
    frameRate(60)
    bird = Bird()
    
def draw():
    global bird
    if keyPressed:
        if key==" ":
            bird.jump()
    background(0x6CE3FF)
    line(0,height-deadline,width,height-deadline)
    bird.display()
    
class Bird:
    def __init__(self):
        self.pos = PVector(400,height/2)
        self.gravity = 10
        self.lastJumped = -100
        
    def display(self):
        if self.pos.y > height-deadline:
            noLoop()
        if frameCount-self.lastJumped > 20:
            self.gravity = 10
        self.pos.y += self.gravity
        fill(149,134,75)
        ellipse(self.pos.x,self.pos.y,40,30)
       
    def jump(self):
        self.gravity = -10
        self.lastJumped = frameCount
