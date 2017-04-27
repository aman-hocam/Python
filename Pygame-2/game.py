import sys
import pygame
import random
from pygame.locals import *

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

width = 1000
height = 600

pygame.init()
screen = pygame.display.set_mode((width, height))

ball_pos = [400, 400]
ball_speed = [0.5, 0]
ball_radius = 30

paddle_width = 10
paddle_height = 150
paddle_speed = 1

paddle_1_pos_x = 0
paddle_1_pos_y = 350

paddle_2_pos_x = width - paddle_width
paddle_2_pos_y = 350

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

	screen.fill(BLACK)

	# Orta saha cizgisi
	pygame.draw.line(screen, WHITE, (width/2, 0), (width/2, height), 5)

	# Kale cizgileri
	pygame.draw.line(screen, WHITE, (paddle_width, 0), (paddle_width, height), 2)
	pygame.draw.line(screen, WHITE, (width - paddle_width, 0), (width - paddle_width, height), 2)

	pygame.draw.circle(screen, WHITE, [int(round(ball_pos[0])), int(round(ball_pos[1]))], ball_radius, 0)

	# First paddle
	pygame.draw.polygon(screen, WHITE, [[paddle_1_pos_x 			  , paddle_1_pos_y], # Sol ust
										[paddle_1_pos_x 			  , paddle_1_pos_y + paddle_height], # Sol alt
										[paddle_1_pos_x + paddle_width, paddle_1_pos_y + paddle_height], # Sag alt
										[paddle_1_pos_x + paddle_width, paddle_1_pos_y]], 0) # Sag ust

	# Second paddle
	pygame.draw.polygon(screen, WHITE, [[paddle_2_pos_x 			  , paddle_2_pos_y], # Sol ust
										[paddle_2_pos_x 			  , paddle_2_pos_y + paddle_height], # Sol alt
										[paddle_2_pos_x + paddle_width, paddle_2_pos_y + paddle_height], # Sag alt
										[paddle_2_pos_x + paddle_width, paddle_2_pos_y]], 0) # Sag ust

	keys=pygame.key.get_pressed()
	if keys[K_w]:
		paddle_1_pos_y -= paddle_speed
	if keys[K_s]:
		paddle_1_pos_y += paddle_speed

	if keys[K_UP]:
		paddle_2_pos_y -= paddle_speed
	if keys[K_DOWN]:
		paddle_2_pos_y += paddle_speed

	ball_pos[0] += ball_speed[0]
	ball_pos[1] += ball_speed[1]

	# X collision
	if ball_pos[0] + ball_radius > width - paddle_width and \
	   paddle_2_pos_y <= ball_pos[1] <= paddle_2_pos_y + paddle_height:
		ball_speed[0] = -ball_speed[0]

	elif ball_pos[0] + ball_radius > width - paddle_width:
		ball_pos = [width/2, height/2]
		ball_speed = [random.uniform(-1.0, 1.0), random.uniform(-0.5, 0.5)]

	if ball_pos[0] - ball_radius < paddle_width and \
	   paddle_1_pos_y <= ball_pos[1] <= paddle_1_pos_y + paddle_height:
		ball_speed[0] = -ball_speed[0]

	elif ball_pos[0] - ball_radius < paddle_width:
		ball_pos = [width/2, height/2]
		ball_speed = [random.uniform(-1.0, 1.0), random.uniform(-0.5, 0.5)]

	# Y collision
	if ball_pos[1] + ball_radius > height or ball_pos[1] - ball_radius < 0:
		ball_speed[1] = -ball_speed[1] 

	# Paddle limit
	if paddle_1_pos_y <= 0:
		paddle_1_pos_y = 0
	elif paddle_1_pos_y + paddle_height > height:
		paddle_1_pos_y = height - paddle_height

	if paddle_2_pos_y <= 0:
		paddle_2_pos_y = 0
	elif paddle_2_pos_y + paddle_height > height:
		paddle_2_pos_y = height - paddle_height

	pygame.display.flip()