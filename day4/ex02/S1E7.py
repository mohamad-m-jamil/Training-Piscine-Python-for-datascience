from S1E9 import Character


class Baratheon(Character):
    """Representing the Baratheon family."""

    def __init__(self, first_name, is_alive=True):
        """Initialize a Baratheon character."""
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def die(self):
        """Kill the character."""
        self.is_alive = False

    def __str__(self):
        return f"{self.first_name} {self.family_name} - Eyes: {self.eyes},\
        Hairs: {self.hairs}"

    def __repr__(self):
        return (f"Baratheon('{self.first_name}', '{self.family_name}', "
                f"'{self.eyes}', '{self.hairs}')")


class Lannister(Character):
    """Representing the Lannister family."""

    def __init__(self, first_name, is_alive=True):
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def die(self):
        """Kill the character."""
        self.is_alive = False

    def __str__(self):
        return f"{self.first_name} {self.family_name} - Eyes: {self.eyes},\
        Hairs: {self.hairs}"

    def __repr__(self):
        return (f"Lannister('{self.first_name}', '{self.family_name}', "
                f"'{self.eyes}', '{self.hairs}')")

    @classmethod
    def create_lannister(cls, first_name, is_alive=True):
        """
        Create a Lannister character using a class method.
        This allows for chained/dynamic creation of a Lannister.
        """
        return cls(first_name, is_alive)
