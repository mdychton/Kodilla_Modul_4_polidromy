def if_polidrome(text):
    text = text.lower().replace(" ", "")
    return text == text[::-1]

print(if_polidrome("kajak"))                # True
print(if_polidrome("potop"))                # True
print(if_polidrome("Python"))               # False
print(if_polidrome("Kobyła ma mały bok"))   # True to ciekawe :)