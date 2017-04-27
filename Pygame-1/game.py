import sys
import pygame
from pygame.locals import *

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

pygame.init()
screen = pygame.display.set_mode((800, 800))

ball_pos = [400, 400]
ball_speed = [1, 1.5]
ball_radius = 100

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

	screen.fill(WHITE)
	pygame.draw.circle(screen, BLUE, [int(round(ball_pos[0])), int(round(ball_pos[1]))], ball_radius, 0)

	ball_pos[0] += ball_speed[0]
	ball_pos[1] += ball_speed[1]

	if ball_pos[0] + ball_radius > 800 or ball_pos[0] - ball_radius < 0:
		ball_speed[0] = -ball_speed[0]

	if ball_pos[1] + ball_radius > 800 or ball_pos[1] - ball_radius < 0:
		ball_speed[1] = -ball_speed[1] 

	pygame.display.flip()