bird = None
deadline = 150
obstacles = []
birdRadius = 18
score = 0
has2die = False
def setup():
    global bird
    fullScreen()
    frameRate(60)
    bird = Bird()
    
def draw():
    global bird
    global score
    global birdRadius
    global has2die
    if keyPressed:
        if key==" ":
            bird.jump()
    if frameCount%60==0:
        obstacles.append(Obstacle())
    background(0x6CE3FF)
    textSize(80)
    stroke(0,0,0)
    line(0,height-deadline,width,height-deadline)
    bird.display()
    for i,obstacle in enumerate(obstacles):
        if has2die:
            obstacles.pop(i-1)
        has2die = False
        if bird.pos.x+birdRadius > obstacle.pos.x-25 and bird.pos.x-birdRadius < obstacle.pos.x+25 and bird.pos.y+birdRadius > obstacle.pos.y-25 and bird.pos.y-birdRadius < obstacle.pos.y+25:
            score += 1
            has2die = True
        if obstacle.pos.x < -100:
            has2die = True
        obstacle.display()
    text(score,width/2,50)
class Bird:
    global birdRadius
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
        ellipse(self.pos.x,self.pos.y,2*birdRadius,2*birdRadius)
       
    def jump(self):
        self.gravity = -10
        self.lastJumped = frameCount
        
class Obstacle:
    def __init__(self):
        self.pos = PVector(width,random(height-deadline-25))
    
    def display(self):
        fill(255,0,0)
        noStroke()
        rect(self.pos.x,self.pos.y,50,50)
        self.pos.x -= 7
