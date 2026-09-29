"""utils.py - a small collection of beginner-friendly helper functions."""


def is_palindrome(s):
    """Check whether a string is a palindrome.

    A palindrome is text that reads the same forwards and backwards,
    like "level" or "Race car". Spaces, punctuation, and capital letters
    are ignored when checking.

    Parameter:
        s (str): The string to check.

    Returns:
        bool: True if the string is a palindrome, otherwise False.

    Example:
        is_palindrome("Race car")  ->  True
        is_palindrome("Hello")     ->  False
    """
    # Keep only letters and numbers, and make everything lowercase
    cleaned = ""
    for character in s:
        if character.isalnum():
            cleaned = cleaned + character.lower()

    # Compare the cleaned string with its reverse
    reversed_text = cleaned[::-1]
    return cleaned == reversed_text


def count_words(text):
    """Count how many words are in a piece of text.

    Words are separated by spaces (or other whitespace such as tabs
    and new lines). Extra spaces between words are ignored.

    Parameter:
        text (str): The text whose words you want to count.

    Returns:
        int: The number of words in the text. An empty string returns 0.

    Example:
        count_words("Python is fun")  ->  3
        count_words("")               ->  0
    """
    words = text.split()
    return len(words)


def celsius_to_fahrenheit(c):
    """Convert a temperature from Celsius to Fahrenheit.

    This uses the formula: Fahrenheit = Celsius * 9 / 5 + 32

    Parameter:
        c (int or float): The temperature in degrees Celsius.

    Returns:
        float: The temperature in degrees Fahrenheit.

    Example:
        celsius_to_fahrenheit(0)    ->  32.0
        celsius_to_fahrenheit(100)  ->  212.0
    """
    return c * 9 / 5 + 32


# This part only runs when you run the file directly (python utils.py)
if __name__ == "__main__":
    print(is_palindrome("Race car"))         # True
    print(is_palindrome("Hello"))            # False
    print(count_words("Python is fun"))      # 3
    print(count_words(""))                   # 0
    print(celsius_to_fahrenheit(0))          # 32.0
    print(celsius_to_fahrenheit(100))        # 212.0