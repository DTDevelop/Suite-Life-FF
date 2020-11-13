"""
Using character class, creation of characters

#currently players spawn in same location
#adjust via function create_characters()
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

    CHR_WIDTH = knights[0].get_width()*2 #width 8, height 5
    CHR_HEIGHT = knights[0].get_height()*2

    knights_scaled = []
    for knight in knights:
        knights_scaled.append(pygame.transform.scale(knight,(CHR_WIDTH,CHR_HEIGHT)))
    return knights_scaled

#test output
#print(scale_char_imgs(load_assets("relative_directory.txt")))

"""
function to create character objects
"""
def create_characters(character_sheets,display_width,display_height):
    """
    create character objects
    returns tuple of character objects
    """
    players = []

    for char in character_sheets:
        players.append(spr.Character(30,3,0,display_width/3,display_height/3,char))

    return players


"""
function to blit
"""

#UNDER CONSTRUCTION --
def blit_character(players):
    """
    blit character to display
    param1,2 - location on surface display
    param3,4 - starting location on source image
    param5,6 - img size extracted from source

    returns list of tuples to blit
    """
    blits = []
    for player in players:
        blits.append((player.get_img(),(player.get_x(),player.get_y()),
        0,0,player.get_img().get_width()/8,player.get_img().get_height()/8))
    return blits


























#
