def col(x,y,w,h,x2,y2,w2,h2):
   if (x + w >= x2) and (x <= x2 + w2) and (y + h >= y2) and (y <= y2 + h2):
       return True
   else:
       return False
y = 900
x = 475
DecX = 0
DecY = 0
PlatX = 0
PlatY = 0
ysp = 0
dop = 0
grav = 0.08
jump = False
pr = -6
i = 0
a = [100]
count = 0
def setup():
    size(1000,1000)
    def draw():
    global x,y,DecX,DecY,PlatX,PlatY,ysp,grav,jump,pr,dop,a, count
    #deco
    rect(x,y,50,50)
    fill(75,56,4)
    rect(0,900,1000,100)
    ellipse(DecX,DecY,50,50)
    if count <= 100:
        PlatX = random(0,900)
        PlatY += 200
        rect(PlatX,PlatY,100,10)
    fill(255)
    rect(x,y,50,50)
    ysp += grav
    y += ysp
    dop = PlatY - y
    PlatY - dop
    if y > height - 25:
        y = height - 25
        ysp = 0
        jump = False
    if jump == False:
        ysp = pr
        jump = True
    if keyPressed == True:
        if key == 'D' or key == 'd':
            x += 15
        if key == 'A' or key == 'a':
            x -= 15
