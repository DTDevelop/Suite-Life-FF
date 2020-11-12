"""
Using character class, creation of characters
"""

import pygame
import sprite_class as spr

"""
load asset file(s)
"""
def load_char_files():
    """
    helper function for create_characters
    returns loaded/scaled character sheets
    """
    knight_1 = pygame.image.load("Assets\Knight_Character_Pack\knight_1.png")
    knight_2 = pygame.image.load("Assets\Knight_Character_Pack\knight_3.png")

    CHR_WIDTH = characterImg.get_width() *2#width 8, height 5
    CHR_HEIGHT = characterImg.get_height() *2

    knight_1 = pygame.transform.scale(characterImg, (CHR_WIDTH,CHR_HEIGHT))
    knight_2 = pygame.transform.scale(characterImg, (CHR_WIDTH,CHR_HEIGHT))
    return (knight_1, knight_2)

"""
function to create character objects
"""
def create_characters(character_sheets):
    """
    create character objects
    returns list of character objects
    """
    players = []

    for char in character_sheets:
        characters.append(spr.Character(30,3,1,DISPLAY_WIDTH/3,DISPLAY_HEIGHT/3,char))

    return players



"""
function to blit
"""

def character(img,x,y,ss_x,ss_y,source_x=0,source_y=0):
    """
    blit character to display
    param1,2 - location on surface display
    param3,4 - starting location on source image
    param5,6 - img size extracted from source

    returns tuple used in surface.blit()
    """
    return (img,(x,y),(source_x,source_y,ss_x,ss_y))


























#
