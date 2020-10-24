"""
Food Item Class
"""

class Food():
    """
    create food item object
    """
    def __init__(self, health = 3, weight = 3):
        """
        initialize food
        """
        self._health = health #upon 0, removed from inventory
        self._weight = weight #vs strenght, result projectile speed

        # sprite spawn front of character
        # life cycle until impact on Character object or impassable terrain

    def __str__(self):
        """
        string representation of food
        """
        health = 'Food has\n', self._health, 'health\n'
        speed = self._weight, ' weight'

        return str(health)+str(speed)

    def get_health(self):
        """
        returns remaining HP of food item
        """
        return self._health

    def get_weight(self):
        """
        returns throw speed
        """
        return self._weight

    def deduct_health(self):
        """
        decrement health by 1
        """
        self._health -= 1

        #shooting keypress handler should remove
        #food from inventory upon 0 HP
















    #
