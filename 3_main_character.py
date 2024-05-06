import pygame

pygame.init()

#screen size
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Jun game") #game title

background = pygame.image.load("/Users/junsuplim/pyworkspace/pygame_basic/640x480-light-blue-solid-color-background.jpg")

#character

character = pygame.image.load("/Users/junsuplim/pyworkspace/pygame_basic/character.png")
character_size = character.get_rect().size # size of image
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = screen_width / 2 - character_width / 2
character_y_pos = screen_height - character_height

#event loop
running = True # is it running?
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #screen.fill((0, 0, 255))
    screen.blit(background, (0, 0)) #draw background
    screen.blit(character, (character_x_pos, character_y_pos))

    pygame.display.update() #re-drawing, necessary
# pygame quit
pygame.quit()