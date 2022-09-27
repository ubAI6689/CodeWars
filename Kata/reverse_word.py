def reverse_words(text):
    words=text.split()
    for wordindex, word in enumerate(words):
        word[wordindex] = reverse(word)

    return " ".join(word for word in words)

def reverse(word):
    l = len(word)
    res = ""
    for index in range(1,l+1):
        res+=word[-index]
    return res