import pygame
import sys
import random
import base64

# Decoded base64 images
bird_img_data = """
<base64_encoded_bird_image_data>
"""

pipe_img_data = """
<base64_encoded_pipe_image_data>
"""

bird_img = pygame.image.load(pygame.image.fromstring(base64.b64decode(bird_img_data), (BIRD_WIDTH, BIRD_HEIGHT), "RGBA"))
pipe_img = pygame.image.load(pygame.image.fromstring(base64.b64decode(pipe_img_data), (PIPE_WIDTH, PIPE_HEIGHT), "RGBA"))
