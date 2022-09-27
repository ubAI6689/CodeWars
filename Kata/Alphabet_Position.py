import string


def alphabet_position(text):
    alpha='abcdefghijklmnopqrstuvwxyz'
    res=[]
    t=text.lower()
    for i in t:
        if i in alpha:
            res.append(str(string.ascii_lowercase.index(i)+1))
    return " ".join(res)

print(alphabet_position("The sunset sets at twelve o' clock."))