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

# moving coordinates
to_x = 0
to_y = 0



#event loop
running = True # is it running?
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                to_x += 5
            elif event.key == pygame.K_LEFT:
                to_x -= 5
            elif event.key == pygame.K_UP:
                to_y -= 5
            elif event.key == pygame.K_DOWN:
                to_y += 5
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_LEFT:
                to_x = 0
            elif event.key == pygame.K_UP:
                to_y = 0
            elif event.key == pygame.K_DOWN:
                to_y = 0

    character_x_pos += to_x
    character_y_pos += to_y

    #width restriction
    if character_x_pos < 0:
        character_x_pos = 0
    
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width
    #height restriction
    if character_y_pos < 0:
        character_y_pos =0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height

    #screen.fill((0, 0, 255))
    screen.blit(background, (0, 0)) #draw background
    screen.blit(character, (character_x_pos, character_y_pos))

    pygame.display.update() #re-drawing, necessary
# pygame quit
pygame.quit()