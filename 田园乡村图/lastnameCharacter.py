'''
#!/usr/bin/env python3
- * - coding=utf-8 - * -
@author     :  makerchen
@time       :  2019-5-8
@IDE        :  PyCharm/Sublime Text
@微信公众号 ：小鸿星空科技
- * - coding=utf-8 - * -
'''

# Imports
import pygame
import random
import math

# Initialize game engine
pygame.init()

# Window
SIZE = (1000, 600)
TITLE = "My Awesome Picture"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)

# Timer
clock = pygame.time.Clock()
refresh_rate = 60

# Colors
r = (255, 0, 0) #Red
lr = (255, 150, 150) #Light Red
dr = (150,0,0) #Dark Red
w = (255, 255, 255) #White
ns = (10, 25, 75) #Night Sky
b = (0, 0, 0) #Black
y = (255, 255, 0) #Yellow
g = (90, 90, 90) #Gray
lg = (225, 225, 225) #Light Gray
gg = (0, 180, 0) #Grass Green

screen.fill(ns)

#Pixels for Umbreon
UMB0 = [b,b,ns,ns,ns,ns,ns,ns,ns,ns,ns,ns,ns,ns,ns,ns,ns,ns,ns,ns,ns]
UMB1 = [b,g,b,ns,ns,ns,ns,ns,ns,ns,ns,b,b,b,ns,ns,ns,ns,ns,ns,ns]
UMB2 = [b,y,y,b,ns,ns,ns,ns,ns,b,b,g,g,b,ns,ns,ns,ns,b,b,b]
UMB3 = [b,y,g,g,b,ns,ns,ns,b,y,y,g,g,b,ns,ns,ns,b,g,g,b]
UMB4 = [b,y,g,g,b,b,b,b,g,g,y,y,b,ns,ns,ns,b,y,y,g,b]
UMB5 = [ns,b,g,g,y,y,g,b,g,g,y,b,ns,ns,ns,b,y,y,y,y,b]
UMB6 = [ns,ns,b,g,g,y,g,g,g,g,b,ns,ns,ns,ns,b,g,g,y,b,ns]
UMB7 = [ns,b,g,g,y,g,g,g,b,b,ns,ns,ns,b,b,g,g,g,b,ns,ns]
UMB8 = [ns,b,y,y,g,g,w,b,g,b,b,b,b,g,g,g,b,b,ns,ns,ns]
UMB9 = [ns,b,g,g,g,w,r,b,g,b,b,g,g,g,g,b,ns,ns,ns,ns,ns]
UMB10 = [ns,b,g,g,g,r,b,g,g,b,g,g,g,g,y,g,b,ns,ns,ns,ns]
UMB11 = [ns,ns,b,g,g,g,g,b,b,g,g,g,g,g,y,g,b,ns,ns,ns,ns]
UMB12 = [ns,ns,ns,b,b,b,b,g,g,g,g,g,g,b,g,y,g,b,ns,ns,ns]
UMB13 = [ns,ns,ns,ns,ns,b,g,g,g,g,g,g,g,b,g,b,g,b,ns,ns,ns]
UMB14 = [ns,ns,ns,ns,ns,b,g,g,b,g,g,b,g,b,b,g,g,b,ns,ns,ns]
UMB15 = [ns,ns,ns,ns,b,g,g,b,b,g,y,b,b,ns,ns,b,g,b,ns,ns,ns]
UMB16 = [ns,ns,ns,b,g,g,b,ns,ns,b,y,b,ns,ns,ns,b,g,b,ns,ns,ns]
UMB17 = [ns,ns,ns,b,b,b,ns,ns,ns,b,g,b,ns,ns,ns,b,b,ns,ns,ns,ns]
UMB18 = [ns,ns,ns,ns,ns,ns,ns,ns,ns,b,g,b,ns,ns,ns,ns,ns,ns,ns,ns,ns]
UMB19 = [ns,ns,ns,ns,ns,ns,ns,ns,ns,b,b,ns,ns,ns,ns,ns,ns,ns,ns,ns,ns]
#Pixels for Pokeball
PKM0 = [ns,ns,ns,ns,b,b,b,b,ns,ns,ns,ns]
PKM1 = [ns,ns,b,b,r,dr,dr,dr,b,b,ns,ns]
PKM2 = [ns,b,r,r,lr,r,dr,dr,dr,dr,b,ns]
PKM3 = [ns,b,r,lr,w,lr,r,r,dr,dr,b,ns] #<<<
PKM4 = [b,r,r,r,lr,r,r,r,dr,dr,dr,b]
PKM5 = [b,r,r,r,r,b,b,dr,dr,dr,dr,b]
PKM6 = [b,b,r,r,b,w,lg,b,dr,dr,b,b]
PKM7 = [b,w,b,b,b,lg,lg,b,b,b,lg,b]
PKM8 = [ns,b,w,w,w,b,b,lg,lg,lg,b,ns]
PKM9 = [ns,b,w,w,w,w,w,lg,lg,lg,b,ns,ns]
PKM10 = [ns,ns,b,b,lg,lg,lg,lg,b,b,ns,ns]
PKM11 = [ns,ns,ns,ns,b,b,b,b,ns,ns,ns,ns]

#draws stars
def stars(color, position, size):
		pygame.draw.circle(screen, color, position, size)
for x in range(0,25):
	stars(w, (random.randint(0,900), random.randint(0,600)),3)

#draws triangular stars
def stars2(color):
		x1 = random.randint(0,1000)
		y1 = random.randint(0,1000)
		pygame.draw.polygon(screen, color, ((x1,y1), (x1+1,y1+1), (x1+2,y1)))
for x in range(0,25):
		stars2(w)

#draws the moon
def moon(color, position, size):
	pygame.draw.circle(screen, color, position, size)
moon(y,(900, 100), 80)

#draws the Pokeball
for y in range(0,12):
	PKM_List = [PKM0,PKM1,PKM2,PKM3,PKM4,PKM5,PKM6,PKM7,PKM8,PKM9,PKM10,PKM11]
	PKM = PKM_List[y]
	
	for x in range(0,12):
		pygame.draw.rect(screen, PKM[x], (x*10+800, y*10+395, 10, 10))
		
#draws the Umbreon
for y in range(0,20):
	UMBreon_List = [UMB0,UMB1,UMB2,UMB3,UMB4,UMB5,UMB6,UMB7,UMB8,UMB9,UMB10,UMB11,UMB12,UMB13,UMB14,UMB15,UMB16,UMB17,UMB18,UMB19]
	UMB = UMBreon_List[y]
	
	for x in range(0,21):
		pygame.draw.rect(screen, UMB[x], (x*10+500, y*10+315, 10, 10))

def draw_house(x,y):
	#pink house
	pygame.draw.rect(screen,(255,171,244),(x,y-180,200,180))
	#brown door
	pygame.draw.rect(screen,(89,71,0),(x+80,y-60,40,60))
	#yellow door knob
	pygame.draw.rect(screen,(128,64,0),(380,270,20,60))
	pygame.draw.circle(screen,(255,204,0),(x+112,y-30),4)
	#triangle roof
	pygame.draw.polygon(screen, (125,125,125), ( (x,y-180),(x+100,y-250),(x+200,y-180) ) )
	draw_window(x+20,y-90)
	draw_window(x+130,y-90)
	draw_window(x+80,y-180)

def draw_window(x,y):
	#glass
	pygame.draw.rect(screen,(207,229,255),(x,y-50,45,45))
	#frame
	pygame.draw.rect(screen,(0,0,0),(x,y-50,45,45),3)
	pygame.draw.rect(screen,(0,0,0),(x+23,y-50,3,45))
	pygame.draw.rect(screen,(0,0,0),(x,y-27,45,5))

draw_house(225,520)

def draw_cloud(x,y,size):
	pygame.draw.circle(screen,(255,255,255),(x,y),int(size*.5))
	pygame.draw.circle(screen,(255,255,255),(int(x+size*.5),y),int(size*.6))
	pygame.draw.circle(screen,(255,255,255),(x+size,int(y-size*.1)),int(size*.4))
draw_cloud(60,80,60)
draw_cloud(220,50,40)
draw_cloud(550,100,100)

def draw_bubble(x,y,size):
	pygame.draw.circle(screen,(0,0,0),(x,y),int(size*.5))
	pygame.draw.circle(screen,(0,0,0),(int(x+size*.5),y),int(size*.6))
	pygame.draw.circle(screen,(0,0,0),(x+size,int(y-size*.1)),int(size*.4))
draw_bubble(410,250,20)
draw_bubble(450,240,15)

def draw_small_tree(x,y):
	#small_tree(50 wide and 100 tall)
	pygame.draw.rect(screen,(117,90,0),(x,y-100,50,100))
	#leaves are a circle
	pygame.draw.circle(screen,(27,117,0),(x+25,y-120),50)

draw_small_tree(60,520)


def draw_big_tree():
	'''
	for循环：树干，树支，花朵绘制的步骤及移动顺序
	'''
	tree_x = 250
	tree_y = 530
	tree_size = 50

	for tree in range(200):
		tree_y = tree_y - 1
		tree_x = tree_x - 0.2
		tree_size = tree_size - 0.1
		my_tree = pygame.draw.rect(screen,(134,78,2),(tree_x,tree_y,tree_size,tree_size),0)#画出主树干

	tree_size = 30
	for tree in range(180):
		tree_y = tree_y - 1
		tree_x = tree_x + 0.5
		tree_size = tree_size - 0.15
		my_tree = pygame.draw.rect(screen,(134,78,2),(tree_x,tree_y,tree_size,tree_size),0)#剩下的画出不同的树枝

	branch_x = 210
	branch_y = 330
	branch_size = 15
	for tree in range(180):
		branch_y = branch_y - 1
		branch_x = branch_x - 0.4
		branch_size = branch_size - 0.05
		my_tree = pygame.draw.rect(screen,(134,78,2),(branch_x,branch_y,branch_size,branch_size),0)

	branch_x = 200
	branch_y = 180
	branch_size = 10
	for tree in range(50):
		branch_y = branch_y - 1
		branch_x = branch_x + 1.5
		branch_size = branch_size - 0.05
		my_tree = pygame.draw.rect(screen,(134,78,2),(branch_x,branch_y,branch_size,branch_size),0)

	branch_x = 210
	branch_y = 310
	branch_size = 15
	for tree in range(150):
		branch_y = branch_y - 1
		branch_x = branch_x - 1
		branch_size = branch_size - 0.05
		my_tree = pygame.draw.rect(screen,(134,78,2),(branch_x,branch_y,branch_size,branch_size),0)

	branch_x = 110
	branch_y = 210
	branch_size = 10
	for tree in range(50):
		branch_y = branch_y + 0.3
		branch_x = branch_x - 1
		branch_size = branch_size - 0.05
		my_tree = pygame.draw.rect(screen,(134,78,2),(branch_x,branch_y,branch_size,branch_size),0)

	branch_x = 170
	branch_y = 230
	branch_size = 12
	for tree in range(80):
		branch_y = branch_y - 1.5
		branch_x = branch_x + 1
		branch_size = branch_size - 0.1
		my_tree = pygame.draw.rect(screen,(134,78,2),(branch_x,branch_y,branch_size,branch_size),0)

	f_x = 0
	f_y = 0
	for flower in range(250):#画出花朵
		f_x = random.randint(180,280)
		f_y = random.randint(100,300)
		my_flower = pygame.draw.circle(screen,(0,random.randint(150,255),0),(f_x,f_y),5,1)

	for flower in range(130):
		f_x = random.randint(280,380)
		f_y = random.randint(130,250)
		my_flower = pygame.draw.circle(screen,(0,random.randint(150,255),0),(f_x,f_y),5,1)


	for flower in range(130):
		f_x = random.randint(80,180)
		f_y = random.randint(130,250)
		my_flower = pygame.draw.circle(screen,(0,random.randint(150,255),0),(f_x,f_y),5,1)
		   
	for flower in range(80):
		f_x = random.randint(130,180)
		f_y = random.randint(200,300)
		my_flower = pygame.draw.circle(screen,(0,random.randint(150,255),0),(f_x,f_y),5,1)

	for flower in range(80):
		f_x = random.randint(330,430)
		f_y = random.randint(100,200)
		my_flower = pygame.draw.circle(screen,(0,random.randint(150,255),0),(f_x,f_y),5,1)

	for flower in range(80):
		f_x = random.randint(30,130)
		f_y = random.randint(150,250)
		my_flower = pygame.draw.circle(screen,(0,random.randint(150,255),0),(f_x,f_y),5,1)
		#此部分使用那么多的for循环是为了增强花朵排列的自然感
draw_big_tree()

#draws grass
def grass(color, position):
	pygame.draw.rect(screen, color, position)
	
grass(gg,(0,515,1000,85))

# Game loop
done = False

if __name__ == '__main__':
	while not done:
		clock.tick(refresh_rate)
		# Event processing
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				done = True
		pygame.display.flip()
	# Close window and quit
	pygame.quit()