# Programer: Jacob Mark-Synard
# Discription: Making a dog move.

# Import and initialize the pygame library
import pygame
from pygame.locals import *
pygame.init()

# Import functions for drawing gridlines and using sprites
from pygame_grid import *
from ucc_sprite import Sprite

# Create and open a pygame screen with the given size
screen = pygame.display.set_mode((960, 540))
grid = make_grid()

# Set the title of the pygame screen
pygame.display.set_caption("My Game")

# Create a clock to keep track of time
clock = pygame.time.Clock()

# Group to hold all of the active sprites
all_sprites = pygame.sprite.Group()

### SET UP YOUR GAME HERE

# Load images
background_image = pygame.image.load("park.png")
dog_image = pygame.image.load("dog.png")

# Create sprites
dog = Sprite(dog_image)
dog.postion = (300, 100)
dog.direction = 300
dog.rotates = True
dog.speed = 2
dog.add(all_sprites)

dog2 = Sprite(dog_image)
dog2.postion = (100, 200)
dog2.direction = 500
dog2.rotates = False 
dog2.speed = 2
dog2.add(all_sprites)

# Main Loop
while True:
    # Set the frame rate to 60 frames per second
    clock.tick(60)

    ### MANAGE IN-GAME EVENTS AND ANIMATIONS HERE



    # Redraw the background
    screen.blit(background_image, (0, 0))

    # Update the sprites' locations
    all_sprites.update()

    # Redraw the sprites
    all_sprites.draw(screen)

    # Uncomment the next line to show a grid
    # screen.blit(grid, (0,0))

    # Flip the changes to the screen to the computer display
    pygame.display.flip()