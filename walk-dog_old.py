# Import and initialize the pygame library
import pygame
from pygame.locals import *
pygame.init()

# Import Sprite class and function to show a grid
from ucc_sprite import Sprite
from pygame_grid import make_grid

# Create and open a pygame screen with the given size
screen = pygame.display.set_mode((640, 360))
grid = make_grid()

# Set the title of the pygame screen
pygame.display.set_caption("Puppy Dog")

# Create a clock to keep track of time
clock = pygame.time.Clock()

# Load the image of a dog
dog_image = pygame.image.load("dog.png")

# Create the sprite
dog = Sprite(dog_image, (0, 100))

# Main Loop
while True:
    # Set the frame rate to 60 frames per second
    clock.tick(60)

    # Clear the screen by redrawing the background
    screen.fill("white")

    # Add the dog image to the screen
    

    # Uncomment the next line to show a grid
    # screen.blit(grid, (0,0))

    # Flip the changes to the screen to the computer display
    pygame.display.flip()
