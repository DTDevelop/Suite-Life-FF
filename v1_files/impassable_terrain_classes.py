"""
Map Class + Furniture Class
"""

class Map():
    """
    creates map object
    """
    def __init__(self, width = 100, height = 100):
        """
        initializes map
        """
        self._width = width
        self._height = height
        self._half_width = self._width/2
        self._half_height = self._height/2
        self._map_center = (self._width, self._height)

    def __str__(self):
        """
        string representation
        """
        width = 'map has a width of', self._width
        height = 'and a height of', self._height

        return str(width)+str(height)

    def get_width(self):
        """
        returns width
        """
        return self._width

    def get_height(self):
        """
        returns height
        """
        return self._height

    def get_half_width(self):
        """
        returns half width
        """
        return self._half_width

    def get_half_height(self):
        """
        returns half height
        """
        return self._half_height

    def get_map_center(self):
        """
        reutnrs map center point
        """
        return self._map_center

class Furniture():
    """
    creates furniture object
    """
    def __init__(self, width = 25, height = 25):
        """
        initalize furniture
        """
        self._width = width
        self._height = height
        self._center = (self._width/2, self._height/2)

    def __str__(self):
        """
        string representation
        """
        width = 'furniture has a width of', self._width
        height = 'and a height of', self._height

        return str(width)+str(height)

    def get_width(self):
        """
        returns width
        """
        return self._width

    def get_height(self):
        """
        returns height
        """
        return self._height

    def get_center(sefl):
        """
        returns furniture center point
        """
        return self._center
































    #
