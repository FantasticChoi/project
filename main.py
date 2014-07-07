import pygame
from classes import *

pygame.init()

size = (1280, 700)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("scroller")
clock = pygame.time.Clock()

done = False
colours = {"white":(255, 255, 255), "green":(0, 255, 0), "blue":(0, 0, 255), "red":(255, 0, 0), "cyan":(0, 255, 255)}
groundx = 0
chardirec = "right"
y_vel = 0.0
char_y = 490

char = pygame.image.load("CharDesign1.png").convert_alpha()
charl = pygame.transform.flip(char, True, False)

while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
	
	
	
	keys = pygame.key.get_pressed()
	
	if keys[pygame.K_a] == True:
		groundxvel = 5
		chardirec = "left"
	elif keys[pygame.K_d] == True:
		groundxvel = -5
		chardirec = "right"
	else:
		groundxvel = 0
	
	groundx += groundxvel
	
	if keys[pygame.K_SPACE] == True and (groundcollide.colliderect(ground) or groundcollide.colliderect(ground2)):
		y_vel = 17.0
	
	char_y -= y_vel
	
	ground = pygame.Rect(0 + groundx, 640, 1280, 60)
	ground2 = pygame.Rect(1280 + groundx, 560, 1280, 60)
	groundcollide = pygame.Rect(622, (char_y + 77 - y_vel), 63, 1)
	
	if groundcollide.colliderect(ground):
		y_vel = 0.0
		char_y = ground.y - 77
	elif groundcollide.colliderect(ground2):
		y_vel = 0.0
		char_y = ground2.y - 77
	elif y_vel > -20:
		y_vel -= 1
	
	screen.fill(colours["cyan"])
	
	pygame.draw.rect(screen, colours["green"], ground, 0)
	pygame.draw.rect(screen, colours["green"], ground2, 0)
	#pygame.draw.rect(screen, colours["red"], groundcollide, 0)
	
	if chardirec == "right":
		screen.blit(char, (620, char_y))
	else:
		screen.blit(charl, (620, char_y))
	
	pygame.display.flip()
	
	clock.tick(60)

pygame.quit()