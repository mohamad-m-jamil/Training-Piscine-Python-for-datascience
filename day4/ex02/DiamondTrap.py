from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    def __init__(self, first_name, is_alive=True):
        Baratheon.__init__(self, first_name, is_alive)

    def set_eyes(self, value):
        """seting the eye coloer"""
        self.eyes = value

    def get_eyes(self):
        """seting the eye coloer"""
        return self.eyes

    def set_hairs(self, value):
        """seting the eye coloer"""
        self.hairs = value

    def get_hairs(self):
        """seting the eye coloer"""
        return self.hairs
