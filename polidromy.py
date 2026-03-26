def if_polidrome(text):

    """Function is checking if the given text is a polidrome. It ignores spaces and lower cases.
    :param text: string
    :return: boolean"""

    text = text.lower().replace(" ", "")
    return text == text[::-1]

print(if_polidrome("kajak"))                # True
print(if_polidrome("potop"))                # True
print(if_polidrome("Python"))               # False
print(if_polidrome("Kobyła ma mały bok"))   # True to ciekawe :)