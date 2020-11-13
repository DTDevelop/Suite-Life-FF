"""
v5 implementation, test game start
"""
import pygame
import sprite_class as spr
import create_character as char

pygame.init()

"""
global access variables, immutable
"""
DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600

gameDisplay =  pygame.display.set_mode((DISPLAY_WIDTH,DISPLAY_HEIGHT))
pygame.display.set_caption("Friction Collision")

clock = pygame.time.Clock()
end = False

"""
create objects #create_character.py
"""
char_objects = char.create_characters(char.scale_char_imgs(
               char.load_assets("relative_directory.txt")),DISPLAY_WIDTH,DISPLAY_HEIGHT)
CHR_WIDTH = char_objects[0].get_img().get_width()
CHR_HEIGHT = char_objects[0].get_img().get_height()
#blit function under construction - refer create_character.py
# char_info = char.blit_character(char_objects)

"""
KEY INPUT DICT
"""
#if certain key press, calls on different char objects within list
key_press_one = {
pygame.K_UP: walk_up,
pygame.K_DOWN: walk_down,
pygame.K_LEFT: walk_left,
pygame.K_RIGHT: walk_right
}

key_press_two = {
pygame.K_w: walk_up,
pygame.K_s: walk_down,
pygame.K_a: walk_left,
pygame.K_d: walk_right
}

"""
run game
"""
while not end:
    #end
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            end = True

    gameDisplay.fill((102,204,0))
    for char in char_objects:#TEMP BLIT, EXPLICIT
        gameDisplay.blit(char.get_img(),char.get_pos(),(0,0,CHR_WIDTH/8,CHR_HEIGHT/8))

    pressed = pygame.key.get_pressed()
    if key_press in key_press_one:
        char_objects[0].key_press_one[key_press]()
    if key_press in key_press_two:
        char_objects[1].key_press_two[key_press]()

    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()







































#
