"""
class for all sprites
includes characters, interactable & obstruction objects
"""

import pygame
#moving references:
#https://www.pygame.org/docs/tut/MoveIt.html
#https://stackoverflow.com/questions/16044229/how-to-get-keyboard-input-in-pygame
#https://www.pygame.org/docs/ref/key.html#pygame.key.get_pressed

class Sprite():
    """
    sprite class object
    """
    def __init__(self,x,y,img):
        """
        initialize sprite class
        positional values for given object
        """
        self._x_pos = x
        self._y_pos = y
        self._img = img

    def __str__(self):
        """
        string representation
        """
        return self._img, 'Located at', (_x_pos,_y_pos)

    def get_pos(self):
        """
        returns position of object as tuple
        """
        return (self._x_pos,self._y_pos)

    def get_x(self):
        """
        returns x position
        """
        return self._x_pos

    def get_y(self):
        """
        returns y position
        """
        return self._y_pos

    def get_img(self):
        """
        returns source img string
        """
        return self._img

class Character(Sprite):
    """
    character class object
    """
    def __init__(self,hp,str,velocity,x,y,img):
        """
        initialize character object
        """
        self._health = hp
        self._str = str
        self._player_hit = False #invulnerable period
        self._velocity = velocity
        #increments by fraction (self*accel) until cap velocity
        self._orientation = None #based on last keypress, pre-set from spawn
        super().__init__(x,y,img)

class Tiles(Sprite):
    """
    Tile class object
    """
    def __init__(self,x,y,img):
        """
        initialize tile object
        """
        super().__init__(x,y,img)

class Obstruction(Sprite):
    """
    Obstruction class object
    """
    def __init__(self,x,y,img):
        """
        initialize obstruction object
        """
        super().__init__(x,y,img)

class Item(Sprite):
    """
    Item class Object
    """
    def __init__(self,type,remaining_use,potency,x,y,img):
        """
        initialize obstruction object
        """
        self._type = type #heal, #weapon
        self._remaining_use = remaining_use
        self._potency = potency
        super().__init_(x,y,img)

    def get_type(self):
        """
        return type of item
        """
        return self._type

    def get_remaining_use(self):
        """
        returns remaining use number
        """
        return self._remaining_use

    def get_potency(self):
        """
        return potency
        """
        return self._potency














#
