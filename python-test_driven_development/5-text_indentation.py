#!/usr/bin/python3
"""Module for text indentation."""


def text_indentation(text):
    """Prints text with 2 new lines after '.', '?', and ':'.

    Args:
        text: Input text to format (must be string)

    Raises:
        TypeError: If text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    if text == "":
        return

    i = 0
    while i < len(text):
        if text[i] in ".?:":
            print(text[i], end="\n\n")
            i += 1
            # Skip spaces immediately after delimiter
            while i < len(text) and text[i] == ' ':
                i += 1
            continue
        print(text[i], end="")
        i += 1
