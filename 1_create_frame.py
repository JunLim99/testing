import pygame

pygame.init()

#screen size
screen_width = 480
screen_height = 640
pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Jun game") #game title

#event loop
running = True # is it running?
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# pygame quit
pygame.quit()