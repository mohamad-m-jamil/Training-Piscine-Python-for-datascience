import random
import string
from dataclasses import dataclass, field, InitVar


def generate_id() -> str:
    """Generates a random 15-character student ID."""
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    name: str = field(init=True)
    surname: str = field(init=True)
    active: bool = field(default=True)
    login: str = field(init=False)
    id: str = field(init=False, default_factory=generate_id)

    extra_args: InitVar[dict] = field(default=None)

    def __post_init__(self, extra_args):
        """Initialize login and handle extra arguments."""
        self.login = self.name[0].capitalize() + self.surname.lower()

        if extra_args:
            for key in extra_args:
                print("TypeError: Student.__init__() got an unexpected "
                      f"keyword argument '{key}'")
