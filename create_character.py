"""
Using character class, creation of characters
"""

import pygame
import sprite_class as spr

#use example
#create_characters(scale_char_imgs(load_assets("relative_directory.txt")))

"""
load asset file(s)
"""
def load_assets(directories):
    """
    helper function for scale_char_imgs
    reads directory txt file, gets desired char directories
    returns list of wanted directories to load
    """
    char_directories = []
    with open(directories) as f:
        for line in f:
            if "Assets\Knight_Character_Pack" in line:
                char_directories.append(line.rstrip('\n')) #strips only \n
    return char_directories

#test output
#print(load_assets("relative_directory.txt"))

def scale_char_imgs(directories):
    """
    helper function for create_characters
    returns loaded/scaled character sheets
    """
    knights = []
    for directory in directories:
        knights.append(pygame.image.load(directory))
    # knight_1 = pygame.image.load("Assets\Knight_Character_Pack\knight_1.png")
    # knight_2 = pygame.image.load("Assets\Knight_Character_Pack\knight_3.png")

    CHR_WIDTH = knights[0].get_width() *2#width 8, height 5
    CHR_HEIGHT = knights[0].get_height() *2
    for knight in knights:
        pygame.transform.scale(knight,(CHR_WIDTH,CHR_HEIGHT))
    # knight_1 = pygame.transform.scale(knight_1, (CHR_WIDTH,CHR_HEIGHT))
    # knight_2 = pygame.transform.scale(knight_2, (CHR_WIDTH,CHR_HEIGHT))
    return knights

#test output
print(scale_char_imgs(load_assets("relative_directory.txt")))

"""
function to create character objects
"""
def create_characters(character_sheets):
    """
    create character objects
    returns tuple of character objects
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
