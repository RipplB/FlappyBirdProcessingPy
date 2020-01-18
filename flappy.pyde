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
    
