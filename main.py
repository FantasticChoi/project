import pygame
from math import sin, cos

pygame.init()

size = (1280, 700)

screen = pygame.display.set_mode(size)

pygame.display.set_caption("scroller")

done = False

clock = pygame.time.Clock()

colours = {"white":(255, 255, 255), "green":(0, 255, 0), "blue":(0, 0, 255), "red":(255, 0, 0), "cyan":(0, 255, 255)}

groundx = 0

char = pygame.image.load("char.png").convert_alpha()
charl = pygame.transform.flip(char, True, False)

chardirec = "right"

while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
	
	
	
	keys = pygame.key.get_pressed()
	
	if keys[pygame.K_a] == True:
		groundx += 2
		chardirec = "left"
	elif keys[pygame.K_d] == True:
		groundx -= 2
		chardirec = "right"
	
	screen.fill(colours["cyan"])
	
	pygame.draw.rect(screen, colours["green"], (100 + groundx, 640, 1080, 60), 0)
	
	if chardirec == "right":
		screen.blit(char, (620 ,490))
	else:
		screen.blit(charl, (620 ,490))
	
	pygame.display.flip()
	
	clock.tick(60)

pygame.quit()