def capitalize(phrase):
    """Capitalize first letter of first word of phrase.

        >>> capitalize('python')
        'Python'

        >>> capitalize('only first word')
        'Only first word'
    """

    upper_phrase = phrase.capitalize()
    print(upper_phrase)

capitalize('python')
capitalize('only first word')