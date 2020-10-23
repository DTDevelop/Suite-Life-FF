"""
Character Class
"""

class Character():
    """
    create a character object
    """
    def __init__(self, x = 0, y = 0, health = 3, walk_speed = 3, throw_speed = 3):
        """
        initialize character
        """
        #general player attributes
        self._health = health
        self._walk_speed = walk_speed
        self._throw_speed = throw_speed
        self._player_hit = False
        self._x_place = x
        self._y_place = y

        #general food item attributes
        self._food_num = None
        self._has_food = False
        self._food_health = 0
        return

    def __str__(self):
        """
        string representation
        """
        health = 'Player has\n', self.get_health(), ' health\n'
        walk = self.get_walk_speed(), ' walk speed\n'
        throw = self.get_throw_speed(), 'throw speed\n'
        location = 'located at: ', (self.get_x(), self.get_y())

        return str(health)+str(walk)+str(throw)+str(location)

#player methods
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

    def get_throw_speed(self):
        """
        returns players current throwing speed
        """
        return get._throw_speed

    def player_hit(self):
        """
        returns T/F, if player has been hit
        """
        return self._player_hit

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

    def gain_food(self, food_num, food_health):
        """
        gives character food item
        """
        #parses item object & places values into player object to store
        self._food_num = food_num
        self._item_health = food_health

    def throw_food(self):
        """
        changes values upon throwing food
        """
        if has_food:
            self.deduct_food()

    def deduct_food(self):
        """
        deduct food count
        """
        self._food_health -= 1

    def get_food_num(self):
        """
        returns food number
        """
        return self.food_num

    def get_food_count(self):
        """
        get food count of current item
        """
        return self._food_health
