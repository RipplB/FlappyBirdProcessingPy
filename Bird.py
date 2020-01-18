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
