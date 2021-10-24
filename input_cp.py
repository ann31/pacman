import pygame
import random

pygame.init()


win_h = 31 * 30
win_w = 34 * 30
pelCount = 0
lives = 3

#creating pygame window
win= pygame.display.set_mode((win_w,win_h))

#pacman animation
pacLeft = [pygame.image.load('pacman/Pac1.png'),pygame.image.load('pacman/PacL.png')]
pacRight = [pygame.image.load('pacman/Pac1.png'),pygame.image.load('pacman/PacR.png')]
pacUp = [pygame.image.load('pacman/Pac1.png'),pygame.image.load('pacman/PacU.png')]
pacDown = [pygame.image.load('pacman/Pac1.png'),pygame.image.load('pacman/PacD.png')]
pacStill = pygame.image.load('pacman/Pac1.png')

ghost = [[None for x in range(5)] for x in range (4)]

#clyde animations
ghost[0][0] = [pygame.image.load('clydeL1.png'),pygame.image.load('clydeL2.png')]
ghost[0][1] = [pygame.image.load('clydeR1.png'),pygame.image.load('clydeR2.png')]
ghost[0][2] = [pygame.image.load('clydeU1.png'),pygame.image.load('clydeU2.png')]
ghost[0][3] = [pygame.image.load('clydeD1.png'),pygame.image.load('clydeD2.png')]
ghost[0][4] = [pygame.image.load('clydeL1.png')]

#inky animations
ghost[1][0] = [pygame.image.load('inkyL1.png'),pygame.image.load('inkyL2.png')] 
ghost[1][1] = [pygame.image.load('inkyR1.png'),pygame.image.load('inkyR2.png')] 
ghost[1][2] = [pygame.image.load('inkyU1.png'),pygame.image.load('inkyU2.png')] 
ghost[1][3] = [pygame.image.load('inkyD1.png'),pygame.image.load('inkyD2.png')] 
ghost[1][4] = pygame.image.load('inkyL1.png')

#pinky animations
ghost[2][0] = [pygame.image.load('pinkyL1.png'),pygame.image.load('pinkyL2.png')]
ghost[2][1] = [pygame.image.load('pinkyR1.png'),pygame.image.load('pinkyR2.png')]
ghost[2][2] = [pygame.image.load('pinkyU1.png'),pygame.image.load('pinkyU2.png')]
ghost[2][3] = [pygame.image.load('pinkyD1.png'),pygame.image.load('pinkyD2.png')]
ghost[2][4] = pygame.image.load('pinkyL1.png')

#blinky animations
ghost[3][0] = [pygame.image.load('blinkyL1.png'),pygame.image.load('blinkyL2.png')]
ghost[3][1] = [pygame.image.load('blinkyR1.png'),pygame.image.load('blinkyR2.png')]
ghost[3][2] = [pygame.image.load('blinkyU1.png'),pygame.image.load('blinkyU2.png')]
ghost[3][3] = [pygame.image.load('blinkyD1.png'),pygame.image.load('blinkyD2.png')]
ghost[3][4] = pygame.image.load('blinkyL1.png')

#images for creating maze
brick = pygame.image.load('brick.png')
pel = pygame.image.load('pellet.png')

clock = pygame.time.Clock()
random.seed()

#variables
cell_h = 30
cell_w = 30
White=(255,255,255)
start_count=0

#maze matrix b-brick, p - pellets, np- no pellets, l-line
pac_grid = [['b','b','b','b','b','b','b','b','b','b','b','b','b','b','b','b','b','b','b','b','b','b','b','b','b','b','b','b'],
            ['b','p','p','p','p','p','p','p','p','p','p','p','p','b','b','p','p','p','p','p','p','p','p','p','p','p','p','b'],
            ['b','p','b','b','b','b','p','b','b','b','b','b','p','b','b','p','b','b','b','b','b','p','b','b','b','b','p','b'],
            ['b','p','b','n','n','b','p','b','n','n','n','b','p','b','b','p','b','n','n','n','b','p','b','n','n','b','p','b'],
            ['b','p','b','b','b','b','p','b','b','b','b','b','p','b','b','p','b','b','b','b','b','p','b','b','b','b','p','b'],
            ['b','p','p','p','p','p','p','p','p','p','p','p','p','p','p','p','p','p','p','p','p','p','p','p','p','p','p','b'],
            ['b','p','b','b','b','b','p','b','b','p','b','b','b','b','b','b','b','b','p','b','b','p','b','b','b','b','p','b'],
            ['b','p','b','b','b','b','p','b','b','p','b','b','b','b','b','b','b','b','p','b','b','p','b','b','b','b','p','b'],
            ['b','p','p','p','p','p','p','b','b','p','p','p','p','b','b','p','p','p','p','b','b','p','p','p','p','p','p','b'],
            ['b','b','b','b','b','b','p','b','b','b','b','b','p','b','b','p','b','b','b','b','b','p','b','b','b','b','b','b'],
            ['n','n','n','n','n','b','p','b','b','b','b','b','p','b','b','p','b','b','b','b','b','p','b','n','n','n','n','n'],
            ['n','n','n','n','n','b','p','b','b','p','p','p','p','p','p','p','p','p','p','b','b','p','b','n','n','n','n','n'],
            ['n','n','n','n','n','b','p','b','b','p','b','l','b','b','b','b','l','b','p','b','b','p','b','n','n','n','n','n'],
            ['n','n','n','n','n','b','p','b','b','p','b','n','n','n','n','n','n','b','p','b','b','p','b','n','n','n','n','n'],
            ['n','n','n','n','n','b','p','p','p','p','b','n','n','n','n','n','n','b','p','p','p','p','b','n','n','n','n','n'],
            ['n','n','n','n','n','b','p','b','b','p','b','n','n','n','n','n','n','b','p','b','b','p','b','n','n','n','n','n'],
            ['n','n','n','n','n','b','p','b','b','p','b','b','b','b','b','b','b','b','p','b','b','p','b','n','n','n','n','n'],
            ['n','n','n','n','n','b','p','b','b','p','p','p','p','p','p','p','p','p','p','b','b','p','b','n','n','n','n','n'],
            ['n','n','n','n','n','b','p','b','b','p','b','b','b','b','b','b','b','b','p','b','b','p','b','n','n','n','n','n'],
            ['b','b','b','b','b','b','p','b','b','p','b','b','b','b','b','b','b','b','p','b','b','p','b','b','b','b','b','b'],
            ['b','p','p','p','p','p','p','p','p','p','p','p','p','b','b','p','p','p','p','p','p','p','p','p','p','p','p','b'],
            ['b','p','b','b','b','b','p','b','b','b','b','b','p','b','b','p','b','b','b','b','b','p','b','b','b','b','p','b'],
            ['b','p','b','b','b','b','p','b','b','b','b','b','p','b','b','p','b','b','b','b','b','p','b','b','b','b','p','b'],
            ['b','p','p','p','b','b','p','p','p','p','p','p','p','p','p','p','p','p','p','p','p','p','b','b','p','p','p','b'],
            ['b','b','b','p','b','b','p','b','b','p','b','b','b','b','b','b','b','b','p','b','b','p','b','b','p','b','b','b'],
            ['b','b','b','p','b','b','p','b','b','p','b','b','b','b','b','b','b','b','p','b','b','p','b','b','p','b','b','b'],
            ['b','p','p','p','p','p','p','b','b','p','p','p','p','b','b','p','p','p','p','b','b','p','p','p','p','p','p','b'],
            ['b','p','b','b','b','b','b','b','b','b','b','b','p','b','b','p','b','b','b','b','b','b','b','b','b','b','p','b'],
            ['b','p','b','b','b','b','b','b','b','b','b','b','p','b','b','p','b','b','b','b','b','b','b','b','b','b','p','b'],
            ['b','p','p','p','p','p','p','p','p','p','p','p','p','p','p','p','p','p','p','p','p','p','p','p','p','p','p','b'], 
            ['b','b','b','b','b','b','b','b','b','b','b','b','b','b','b','b','b','b','b','b','b','b','b','b','b','b','b','b']]


#drawing the grid on the game window
def grid():
    win.fill((0,0,0))
    for i in range(31):
        for j in range (28):
            if pac_grid[i][j]=='b':
                win.blit(brick,(j*cell_w,i*cell_h))
            elif pac_grid[i][j]=='p':
                win.blit(pel,(j*cell_w,i*cell_h))

#first person player object
class player:
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 10
        self.i = 0
        self.j = 0
        self.border = 20
        self.L = False
        self.R = False
        self.U = False
        self.D = False
        self.count = 0
        self.hitbox = (self.x , self.y , 25 , 25)

    #check if pacman is aloowed to move in the given direction
    def check(self,c,s):
        global pelCount

        #creating a padding around the animation
        if s == '+':
            self.border = +20
        else:
            self.border = -10
        
        #finding the position of pacman on the maze grid
        if c =='x':
            self.i = (self.x+self.border)//cell_w
            self.j = (self.y)//cell_h
        else:
            self.i = (self.x)//cell_w
            self.j = (self.y+self.border)//cell_h
        
        #restrictions
        if pac_grid[self.j][self.i]=='b' or  pac_grid[self.j][self.i]=='l':
            return 0
            
        elif pac_grid[self.j][self.i]=='p':
            pac_grid[self.j][self.i] = 'n'
            pelCount += 1
            return 1
        else:
            return 1

    #drawing pacman animation
    def draw(self,win):
        if  self.count + 1 >= 12:
            self.count = 0
    
        if self.L :
            win.blit(pacLeft[self.count % 2], (self.x , self.y))
            self.count += 1
        elif self.R :
            win.blit(pacRight[self.count % 2], (self.x , self.y))
            self.count += 1
        elif self.U :
            win.blit(pacUp[self.count % 2], (self.x , self.y))
            self.count += 1
        elif self.D :
            win.blit(pacDown[self.count % 2], (self.x , self.y))
            self.count += 1
        else:
            win.blit(pacStill, (self.x , self.y))
            self.count += 1
        
        self.hitbox = (self.x , self.y  , 25 , 25)

    #define pacman behaviour when collision occurs
    def hit(self):
        global lives
        self.walkcount = 0
        lives -= 1
        font1 = pygame.font.SysFont('comicsans',20)
        text = font1.render('-10',1,(255,0,0))
        win.blit(text,(self.x,self.y))
        self.x= 30
        self.y= 30
        k=0
        while k < 100:
            pygame.time.delay(10)
            k += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    k  = 301
                    pygame.quit()

#class for the ghosts
class ghosts:
    def __init__(self,x,y,width,height,name):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.name = name
        self.count = 0
        self.vel = 10
        self.i = 0
        self.j = 0
        self.border = 20
        self.ret = 0
        self.dir = ['L','R','D','U']
        self.d = self.dir[random.randrange(4)]
        self.hitbox = (self.x , self.y , 25 , 25)
    
    #checking if the ghost is allowed to move in the given direction
    def check(self,c,s):
        if s == '+':
            self.border = +30
        else:
            self.border = -15


        if c =='x':
            self.i = (self.x + self.border)//cell_w
            self.j = (self.y)//cell_h
        else:
            self.i = (self.x)//cell_w
            self.j = (self.y + self.border)//cell_h
         
        if pac_grid[self.j][self.i]=='b':
            return 0
        else : 
            return 1

    #to find which direction the ghost is allowed to move in
    def gen_dir(self):
        self.ret = 0
        #loop runs till it finds a direction in which the ghost is allowed to move
        while self.ret == 0 :
                self.d = self.dir[random.randrange(4)]
                if self.d == 'L':
                    s = '-'
                    c = 'x'
                elif self.d == 'R':
                    s = '+'
                    c = 'x'
                elif self.d == 'U':
                    s = '+'
                    c = 'y'
                elif self.d == 'D':
                    s = '-'
                    c = 'y'

                self.ret = self.check(c,s)
     
    #drawing the ghost animation 
    def draw (self, win):
        
        self.move()

        if  self.count + 1 >= 12:
            self.count = 0

        if self.d == 'L' :
            win.blit(ghost[self.name][0][self.count % 2], (self.x,self.y))
            self.count += 1
        
        elif self.d == 'R' :
            win.blit(ghost[self.name][1][self.count % 2], (self.x,self.y))
            self.count += 1
        
        elif self.d == 'U' :
            win.blit(ghost[self.name][2][self.count % 2], (self.x,self.y))
            self.count += 1
        
        elif self.d == 'D' :
            win.blit(ghost[self.name][3][self.count % 2], (self.x,self.y))
            self.count += 1
        
        else:
            win.blit(ghost[self.name][4], (self.x,self.y))
            self.count += 1
        self.hitbox = (self.x , self.y  , 25 , 25)
        
    #moving the ghost around the map
    def move (self):
        if self.d == 'L' :
            if self.check('x','-'):
                self.x -=self.vel
            else:
                self.gen_dir()
                if self.d == 'R':
                    self.x += self.vel
                elif self.d == 'U':
                    self.y += self.vel
                elif self.d == 'D':
                    self.y -= self.vel

                self.count = 0

        elif self.d == 'R' :
            if self.check('x','+'):
                self.x +=self.vel
            else:
                self.gen_dir()
                if self.d == 'L':
                    self.x -= self.vel
                elif self.d == 'U':
                    self.y += self.vel
                elif self.d == 'D':
                    self.y -= self.vel
                self.count = 0

        elif self.d == 'U' :
            if self.check('y','+'):
                self.y +=self.vel
            else:
                self.gen_dir()
                if self.d == 'D':
                    self.y -= self.vel
                elif self.d == 'R':
                    self.x += self.vel
                elif self.d == 'L':
                    self.x -= self.vel
                
                self.count = 0

        elif self.d == 'D' :
            if self.check('y','-'):
                self.y -=self.vel
            else:
                self.count = 0
                self.gen_dir()
                if self.d == 'U':
                    self.y += self.vel
                elif self.d == 'R':
                    self.x += self.vel
                elif self.d == 'L':
                    self.x -= self.vel
    
    #behaviour of ghost when collision occurs
    def hit(self):
        if self.d == 'L' :
            self.gen_dir()
            if self.d == 'R':
                self.x += 2
            elif self.d == 'U':
                self.y += 2
            elif self.d == 'D':
                self.y -= 2
            self.count = 0

        elif self.d == 'R' :
            self.gen_dir()
            if self.d == 'L':
                self.x -= 2
            elif self.d == 'U':
                self.y += 2
            elif self.d == 'D':
                self.y -= 2
            self.count = 0

        elif self.d == 'U' :
            self.gen_dir()
            if self.d == 'D':
                self.y -= 2
            elif self.d == 'R':
                self.x += 2
            elif self.d == 'L':
                self.x -= 2
            self.count = 0

        elif self.d == 'D':
            self.count = 0
            self.gen_dir()
            if self.d == 'U':
                self.y += 2
            elif self.d == 'R':
                self.x += 2
            elif self.d == 'L':
                self.x -= 2
            self.count = 0

def score():
    global pelCount
    score = pelCount*10
    font=pygame.font.SysFont('Pokemon GB.ttf',30)
    text=font.render("SCORE :",True,White,(0,0,0))
    text1=font.render(str(score),True,White,(0,0,0))
    win.blit(text,[850,150])
    win.blit(text1,[945,190])
    
pygame.display.update()

def live():
    global lives
    font=pygame.font.SysFont('Pokemon GB.ttf',30)
    text=pygame.image.load('pacman/PacR.png',":")
    text1=text1=font.render(str(lives),True,White,(0,0,0))
    win.blit(text,[850,650])
    win.blit(text1,[900,650])
    
pygame.display.update()
#drawing on the main window
def winDraw():
    global count 
    grid()
    score()
    live()
    pac.draw(win)
    clyde.draw(win)
    inky.draw(win)
    pinky.draw(win)
    blinky.draw(win)

    pygame.display.update()

#to find when a collision is occuring between pacman and a ghost
def collide_p ( pac , ghost_obj ):
    if pac.hitbox[1] < ghost_obj.hitbox[1] + ghost_obj.hitbox[3] and pac.hitbox[1] + pac.hitbox[3] > ghost_obj.hitbox[1]:
        if pac.hitbox[0] < ghost_obj.hitbox[0] + ghost_obj.hitbox[2] and pac.hitbox[0] + pac.hitbox[2] > ghost_obj.hitbox[0]:
            pac.hit()
            ghost_obj.hit()

#to find when a collision happens between two ghosts
def collide_g ( ghost_obj1 , ghost_obj2 ):
    if ghost_obj1.hitbox[1] < ghost_obj2.hitbox[1] + ghost_obj2.hitbox[3] and ghost_obj1.hitbox[1] + ghost_obj1.hitbox[3] > ghost_obj2.hitbox[1]:
        if ghost_obj1.hitbox[0] < ghost_obj2.hitbox[0] + ghost_obj2.hitbox[2] and ghost_obj1.hitbox[0] + ghost_obj1.hitbox[2] > ghost_obj2.hitbox[0]:
            ghost_obj1.hit()
            ghost_obj2.hit()    

#initialising all characters
pac = player(30,30,25,25)
clyde = ghosts(420,420,25,25,0)
inky = ghosts(420,450,25,25,1)
pinky = ghosts(420,390,25,25,2)
blinky = ghosts(480,450,25,25,3)


run= True

#main loop
while run:
    clock.tick(12)

    #checking for collision of pac with a ghost
    collide_p(pac , clyde)
    collide_p(pac , inky)
    collide_p(pac , pinky)
    collide_p(pac , blinky)
    
    #checking for collisions between ghosts
    collide_g(clyde , inky)
    collide_g(clyde , pinky)
    collide_g(clyde , blinky)
    collide_g(inky , clyde)
    collide_g(inky , pinky)
    collide_g(inky , blinky)
    collide_g(pinky , clyde)
    collide_g(pinky , inky)
    collide_g(pinky , blinky)
    collide_g(blinky , clyde)
    collide_g(blinky , inky)
    collide_g(blinky , pinky)

    #exiting the window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run= False

    #detecting player movements
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and pac.check('x','-'):
        pac.x -= pac.vel
        pac.R = False
        pac.L = True
        pac.U = False
        pac.D = False
    elif keys[pygame.K_RIGHT] and pac.check('x','+'):
        pac.x += pac.vel
        pac.R = True
        pac.L = False
        pac.U = False
        pac.D = False
    elif keys[pygame.K_UP] and  pac.check('y','-'):
        pac.y -= pac.vel
        pac.R = False
        pac.L = False
        pac.U = True
        pac.D = False
    elif keys[pygame.K_DOWN] and pac.check('y','+'):
        pac.y += pac.vel
        pac.R = False
        pac.L = False
        pac.U = False
        pac.D = True
    else:
        pac.R = False
        pac.L = False
        pac.U = False
        pac.D = False
        pac.count = 0
    winDraw()
    

pygame.quit()

