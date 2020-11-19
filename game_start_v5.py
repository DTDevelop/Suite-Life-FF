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

char_objects[1].set_x(char_objects[1].get_x()*2)
#blit function under construction - refer create_character.py
# char_info = char.blit_character(char_objects)

"""
KEY INPUT DICT
"""
# def walk_up():
#     pass
# def walk_down():
#     pass
# def walk_left():
#     pass
# def walk_right():
#     pass
#if certain key press, calls on different char objects within list
player_one_mapping = {
'up': char_objects[0].walk_up,
'down': char_objects[0].walk_down,
'left': char_objects[0].walk_left,
'right': char_objects[0].walk_right
}
player_two_mapping = {
'up': char_objects[1].walk_up,
'down': char_objects[1].walk_down,
'left': char_objects[1].walk_left,
'right': char_objects[1].walk_right
}

"""
run game
"""
while not end:
    #end
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            end = True
    # pressed = pygame.key.get_pressed()[pygame.K_w]
    # if pressed == pygame.K_w:
    #     char_objects[1].walk_up()
    for char in char_objects:#TEMP BLIT, EXPLICIT
        gameDisplay.blit(char.get_img(),char.get_pos(),(0,0,CHR_WIDTH/8,CHR_HEIGHT/8))
    #     #has black background because of convert
    if event.type == pygame.KEYDOWN:
        pressed = pygame.key.get_pressed() #checked only if keydown event

        if pressed[pygame.K_UP]:
            player_one_mapping['up']()
        if pressed[pygame.K_DOWN]:
            player_one_mapping['down']()
        if pressed[pygame.K_LEFT]:
            player_one_mapping['left']()
        if pressed[pygame.K_RIGHT]:
            player_one_mapping['right']()

        if pressed[pygame.K_w]:
            player_two_mapping['up']()
        if pressed[pygame.K_s]:
            player_two_mapping['down']()
        if pressed[pygame.K_a]:
            player_two_mapping['left']()
        if pressed[pygame.K_d]:
            player_two_mapping['right']()



        #do for all keys

    pygame.display.update()
    clock.tick(60)
print(char_objects[1].get_pos())
pygame.quit()
quit()







































#
