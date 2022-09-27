def is_isogram(string):
    for letter in string:
        print(string.count(letter.lower()))

print(is_isogram('Testarossa'))