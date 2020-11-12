"""
Character Class
"""

import food_item_class

class Character():
    """
    create a character object
    """
    def __init__(self, x = 0, y = 0, health = 3, walk_speed = 3, strength = 3):
        """
        initialize character
        """
        #general player attributes
        self._health = health
        self._walk_speed = walk_speed
        self._strength = strength #vs food weight, result projectile speed
        self._player_hit = False
        self._x_place = x
        self._y_place = y
        self._orientation = None #facing direction, sets upon key down

        #general food item attributes
        self._food_item = None
        self._has_food = False

    def __str__(self):
        """
        string representation
        """
        health = 'Player has\n', self._health, ' health\n'
        walk = self._walk_speed, ' walk speed\n'
        strength = self.strength, ' strength\n'
        location = 'located at: ', (self._x_place, self._y_place)

        return str(health)+str(walk)+str(strength)+str(location)

#basic methods
    def get_health(self):
        """
        returns players current health
        """
        return self._health

    def get_walk_speed(self):
        """
        returns players current walking speed
        """
        return self._walk_speed

    def get_strength(self):
        """
        returns players current throwing speed
        """
        return get.strength

    def player_hit(self):
        """
        returns T/F, if player has been hit
        """
        return self._player_hit

    def deduct_health(self):
        """
        decrement health by 1
        """
        self._health -= 1


    def get_x(self):
        """
        returns x coordinate of player
        """
        return self._x_place

    def get_y(self):
        """
        returns y coordinate of player
        """
        return self._y_place

#food methods
    def has_food(self):
        """
        returns T/F, if player has food
        """
        return self._has_food

    def gain_food(self, food):
        """
        gives character food item
        """
        #parses item object & places values into player object to store
        self._food_item = food
        self._has_food = True

    def get_food(self):
        """
        returns current food object in hand
        """
        return self._food_item

    def set_orientation(self, direction):
        """
        sets new orientation
        """
        self._orientation = direction

    def get_orientation(self):
        """
        gets orientation
        """
        return self._orientation

#movement methods
    def move_x(self, x):
        """
        changes x value coordinate
        """
        self._x_place += x

    def move_y(self, y):
        """
        changes y value coordinate
        """
        self._y_place += y

#projectile calculation
    def projectile_speed(self):
        """
        returns speed of projectile
        player strength vs food weight
        """
        projetile_speed = (self.get_food().get_weight())-self._strength
        if projectile_speed < 0:
            projectile_speed = 0
        return projectile_speed
























#
