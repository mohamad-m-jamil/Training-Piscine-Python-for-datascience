import sys


def main():
    """
    Analyzes and counts different types of characters in the input text.

    This function takes command-line arguments and calculates the number of:
    - Total characters (excluding the program name)
    - Uppercase letters
    - Lowercase letters
    - Punctuation marks
    - Spaces
    - Digits

    If no input is provided, it prompts the user to enter a value and exits.

    Usage:
        python script.py "Your text here"

    Example:
        Input: python script.py "Hello, World! 123"
        Output:
            The text contains 16 characters:
            2 upper letters
            8 lower letters
            2 punctuation marks
            2 spaces
            3 digits
    """
    if len(sys.argv) < 2:
        print("enter value")
        sys.exit()
    i = 1
    spaces = -1
    characters = 0
    upperletters = 0
    lowerletters = 0
    punctuationmarks = 0
    digits = 0
    while i < len(sys.argv):
        string = sys.argv[i]
        j = 0
        while j < len(string):
            characters += 1
            if string[j] == " ":
                spaces += 1
            elif 'A' <= string[j] <= 'Z':
                upperletters += 1
            elif 'a' <= string[j] <= 'z':
                lowerletters += 1
            elif string[j] in r"!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~":
                punctuationmarks += 1
            elif '0' <= string[j] <= '9':
                digits += 1
            j += 1
        if i < len(sys.argv) or i == len(sys.argv):
            characters += 1
        spaces += 1
        i += 1
    characters -= 1
    print(f"The text contains {characters} characters:")
    print(f"{upperletters} upper letters")
    print(f"{lowerletters} lower letters")
    print(f"{punctuationmarks} punctuation marks")
    print(f"{spaces} spaces")
    print(f"{digits} digits")


if __name__ == "__main__":
    main()
