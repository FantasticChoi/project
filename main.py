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

y_vel = 0.0

char_y = 490

while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
	
	
	
	keys = pygame.key.get_pressed()
	
	if keys[pygame.K_a] == True:
		groundx += 4
		chardirec = "left"
	elif keys[pygame.K_d] == True:
		groundx -= 4
		chardirec = "right"
	
	if keys[pygame.K_SPACE] == True:
		y_vel = 10.0
	
	char_y -= y_vel
	
	ground = pygame.Rect(0 + groundx, 640, 1280, 60)
	groundcollide = pygame.Rect(624, (char_y + 150), 104, 2)
	
	if groundcollide.colliderect(ground):
		y_vel = 0.0
	else:
		y_vel -= 1.0
	
	screen.fill(colours["cyan"])
	
	pygame.draw.rect(screen, colours["green"], ground, 0)
	pygame.draw.rect(screen, colours["red"], groundcollide, 0)
	
	if chardirec == "right":
		screen.blit(char, (620, char_y))
	else:
		screen.blit(charl, (620, char_y))
	
	pygame.display.flip()
	
	clock.tick(60)

print(ground)
print
pygame.quit()