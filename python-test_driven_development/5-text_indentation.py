#!/usr/bin/python3
def text_indentation(text):
    """
    Format the input text by adding 2 newlines after (:?.)
    Args:
        text (str): The input text to be formatted.
    Raises:
        TypeError: If the 'text' argument is not a string.
    """
    if not isinstance(text, str):
        raise TypeError(
            "text must be a string"
        )
    for char in ".?:":
        text = text.replace(char, char + "\n\n")
    line_without_spaces = [lines.strip(' ') for lines in text.split('\n')]
    formatted_text = "\n".join(line_without_spaces)
    print(formatted_text, end="")
