# cd OneDrive\Desktop\PYTH_CARGAME

import pygame
import time
import random
pygame.init()
display_width = 800
display_height = 600
gray = (120, 120, 120)
black = (0, 0, 0)
red = (255, 0, 0)
bright_red = (255, 40, 20)
green = (125, 235, 52)
bright_green = (132, 255, 0)
blue = (20, 118, 255)
bright_blue = (20, 185, 255)
gamedisplays = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("CAR GAME")
clock = pygame.time.Clock()
carimage = pygame.image.load('car1.png')
backgroundpic = pygame.image.load('grass.jpg')
yellow_strip = pygame.image.load('yellow.png')
strip = pygame.image.load('white line.png')
intro_background = pygame.image.load('intro.jpg')
#instruction_background = pygame.image.load('intro.jpg')
car_width = 125

def obstacle(obs_startx,obs_starty,obs):
	if obs==0:
		obs_pic = pygame.image.load('car1.png')
	elif obs==1:
		obs_pic = pygame.image.load('car1.png')
	elif obs==2:
		obs_pic = pygame.image.load('car1.png')
	elif obs==3:
		obs_pic = pygame.image.load('car1.png')
	elif obs==4:
		obs_pic = pygame.image.load('car1.png')
	elif obs==5:
		obs_pic = pygame.image.load('car1.png')


	gamedisplays.blit(obs_pic,(obs_startx,obs_starty))

def score_system(passed,score):
	font = pygame.font.SysFont(None,25)
	text = font.render("Passed :"+str(passed),True,black)
	score = font.render("Score :"+str(score),True,red)
	gamedisplays.blit(text,(0,50))
	gamedisplays.blit(score,(0,30))

def text_objects(text,font):
	textsurface = font.render(text,True,black)
	return textsurface,textsurface.get_rect()

def message_display(text):
	largetext = pygame.font.Font("freesansbold.ttf",80)
	textsurf,testrect = text_objects(text,largetext)
	testrect.center = ((display_width/2),(display_height/2))
	gamedisplays.blit(textsurf,testrect)
	pygame.display.update()
	time.sleep(3)
	game_loop()

def crash():
	message_display("YOU CRASHED")

def background():
	gamedisplays.blit(backgroundpic,(0,0))
	gamedisplays.blit(backgroundpic,(0,200))
	gamedisplays.blit(backgroundpic,(0,400))
	gamedisplays.blit(backgroundpic,(700,0))
	gamedisplays.blit(backgroundpic,(700,200))
	gamedisplays.blit(backgroundpic,(700,400))
	gamedisplays.blit(yellow_strip,(350,0))
	gamedisplays.blit(yellow_strip,(350,140))
	gamedisplays.blit(yellow_strip,(350,280))
	gamedisplays.blit(yellow_strip,(350,420))
	gamedisplays.blit(yellow_strip,(350,560))
	gamedisplays.blit(yellow_strip,(350,700))
	gamedisplays.blit(strip,(80,0))
	gamedisplays.blit(strip,(80,400))
	gamedisplays.blit(strip,(80,800))
	gamedisplays.blit(strip,(620,0))
	gamedisplays.blit(strip,(620,400))
	gamedisplays.blit(strip,(620,800))
	


def car(x,y):
	gamedisplays.blit(carimage,(x,y))

def game_loop():
	x = (display_width*0.45)
	y = (display_height*0.8 )
	x_change = 0
	obstacle_speed = 9
	obs = 0
	y_change = 0
	obs_startx = random.randrange(200,(display_width)-200)
	obs_starty = -750
	obs_width = 60
	obs_height = 115
	passed = 0
	level = 0
	score = 0

	bumped=False
	while not bumped:
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				pygame.quit()
				quit()

			if event.type==pygame.KEYDOWN:
				if event.key==pygame.K_LEFT:
					x_change = -5

				if event.key==pygame.K_RIGHT:
					x_change = 5

				if event.key==pygame.K_a:
					obstacle_speed += 2

				if event.key == pygame.K_b:
					obstacle_speed -= 2

			if event.type==pygame.KEYUP:
				if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
					x_change = 0

		x+=x_change
				
		gamedisplays.fill(gray)
		background()
		obs_starty-=(obstacle_speed/4)
		obstacle(obs_startx,obs_starty,obs)
		obs_starty+=obstacle_speed
		car(x,y)
		score_system(passed,score)
		#Dimensions are not that equal due to images
		if x > 700 - car_width or x<90:
			crash()

		if obs_starty>display_height:
			obs_starty = 0 - obs_height
			obs_startx = random.randrange(100,(display_width-210))
			obs = random.randrange(0,6)
			passed = passed + 1
			score = passed*10
			if int(passed)%10==0:
				level = level+1
				obstacle_speed = obstacle_speed + 2
				largetext = pygame.font.Font("freesansbold.ttf",80)
				textsurf,testrect = text_objects("Level :"+str(level),largetext)
				testrect.center = ((display_width/2),(display_height/2))
				gamedisplays.blit(textsurf,testrect)
				pygame.display.update()
				time.sleep(3)


		if y < obs_starty + obs_height:#couldnt identify the bug
			if x > obs_startx and x < obs_startx + obs_width or x + car_width > obs_startx and x + car_width < obs_startx + obs_width:
				crash()

		pygame.display.update()
		clock.tick(60)

game_loop()
pygame.quit()
quit()
