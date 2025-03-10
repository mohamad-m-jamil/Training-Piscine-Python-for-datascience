import sys


NESTED_MORSE = {
    "A": ".- ", "B": "-... ", "C": "-.-. ",
    "D": "-.. ", "E": ". ", "F": "..-. ",
    "G": "--. ", "H": ".... ", "I": ".. ",
    "J": ".--- ", "K": "-.- ", "L": ".-.. ",
    "M": "-- ", "N": "-. ", "O": "--- ",
    "P": ".--. ", "Q": "--.- ", "R": ".-. ",
    "S": "... ", "T": "- ", "U": "..- ",
    "V": "...- ", "W": ".-- ", "X": "-..- ",
    "Y": "-.-- ", "Z": "--.. ",
    "1": ".---- ", "2": "..--- ",
    "3": "...-- ", "4": "....- ", "5": "..... ",
    "6": "-.... ", "7": "--... ",
    "8": "---.. ", "9": "----. ", "0": "----- ",
    " ": "/ "
}


def encode_to_morse(string):
    """
    Converts a given string into Morse code.

    This function maps each alphanumeric character and space in the input
    string to its corresponding Morse code representation.

    Args:
        string (str): The input string to be encoded.

    Returns:
        str: The Morse code representation of the input string.

    Raises:
        ValueError: If the input string contains an invalid character.
    """
    morse_code = ""
    for char in string.upper():
        if char in NESTED_MORSE:
            morse_code += NESTED_MORSE[char]
        else:
            raise ValueError("Invalid character in input")
    return morse_code.strip()


def main():
    """
    Main function to handle command-line input and convert it to Morse code.

    The function checks if exactly one argument is provided, then calls
    `encode_to_morse` to perform the conversion. If an invalid character
    is found, an error message is displayed.

    Usage:
        python script.py "Your message"

    Example:
        Input: python script.py "SOS"
        Output: "... --- ..."
    """
    if len(sys.argv) != 2:
        print("AssertionError: the arguments are bad")
        sys.exit()

    input_string = sys.argv[1]
    try:
        morse = encode_to_morse(input_string)
        print(morse)
    except ValueError:
        print("AssertionError: the arguments are bad")


if __name__ == "__main__":
    main()
