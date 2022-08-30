import pygame,sys,time,math,random
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((1100,800))
clock = pygame.time.Clock()
BLACK=(255,255,255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 128)
smallfont = pygame.font.SysFont('Corbel',35)
text = smallfont.render('Start' , True , BLACK)
text5 = smallfont.render('Game Over', True, GREEN, BLUE)
background=pygame.image.load('monkeytree.png')
Q=3
images=['arrow.png','balloon.png','balloon1.png']
x,y=[150,500,500],[100,50,50]
img=[0]*Q
rect=[0]*Q
a,angle=0,0
score=0
push0,counter,counter1=0,0,0
X0,Y0=800,100# button location!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
Point1=(X0,Y0)  #circle center coordinates 500/100
Point2=(x[0],y[0]) #monkey position 150/100
X,Y=800,500# start_stop button position
delta=0
Y1=0
k=0
a1=0

crash_sound = pygame.mixer.Sound("pop.wav")

def time_record():
    global counter
    global counter1
    if push0==1:
        counter += 1
        counter1=round(counter/60)
        text3 = smallfont.render(str(counter1), True, (0, 128, 0))
        text4 = smallfont.render('Time in sec:',True, (0, 128, 0))
        screen.blit(text3,(680,648))
        screen.blit(text4, (480, 648))
        
def scores():
    score1=str(score)
    pygame.draw.rect(screen,'green', (X, Y+60,180,50))
    text1=smallfont.render('Score=' , True , BLACK)
    screen.blit(text1,(X+10,Y+65))
    text2=smallfont.render(score1 , True , BLACK)
    screen.blit(text2,(X+120,Y+65))
    
def base(i,scalex,scaley,angle):
    img[i]=pygame.image.load(images[i])
    img[i]=pygame.transform.scale(img[i],(scalex,scaley))
    img[i]=pygame.transform.rotate(img[i],angle)
    rect[i]=img[i].get_rect(center=(x[i],y[i]))
    screen.blit(img[i],rect[i])
    
def position():
    x[0]=150+350*(1-math.cos(angle*3.14/180))
    y[0]=100+350*(1+angle/180)*math.sin(angle*3.14/180)

img[1]=pygame.image.load(images[1])

while True:
    delta=delta+5
    y[1]=50+delta
    y[2]=50+delta
        
    if y[1]>700:
        delta=0
        k=0
        x[1]=random.randint(200,800)
        x[2]=x[1]
            
    screen.blit(background,(0,10))
    scores()
    if a!=2:
        pygame.draw.rect(screen,'orange', (X, Y,100,50))
        screen.blit(text,(X+10,Y+5))
    pygame.draw.line(screen,'brown',Point1,Point2,6)
        
    base(0,70,70,angle)#  ball on the screen
    base(1,100,100,0)#balloon on the screen

    mouse=pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if abs(mouse[0] - X)<50 and abs(mouse[1] - Y) <50:
                a=1
    button=pygame.key.get_pressed()
    if a==1:
        push0=1
        if button[pygame.K_LEFT]:
            angle=angle-1
            position()
        if button[pygame.K_RIGHT]:
            angle=angle+1
            position()
        pygame.draw.rect(screen,(183,168,249), (X, Y,100,50))
        Point2=(x[0],y[0])
        pygame.draw.line(screen,'brown',Point1,Point2,6)
       
        base(0,70,70,angle)
        base(1,100,100,0)
        scores()
        time_record()
        #print('counter1=',counter1)
        if counter1==120:
            screen.blit(text5, (850,650))
            a=2
        if k==1 and y[2]<700:
            base(2,200,200,0)
    if abs(x[0]-x[1])+abs(y[0]-y[1])<40:
        x[1]=2000
        k=1
        score=score+1
        pygame.mixer.Sound.play(crash_sound)
    if a==2:
        screen.blit(text5, (850,650))
        delta=0
    clock.tick(100)
    pygame.display.update()
    

    