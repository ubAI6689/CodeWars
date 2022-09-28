from curses.ascii import isalpha

def is_pangram(s):
    s=s.lower()
    a=set()
    for i in s:
        if isalpha(i):
            a.add(i)
    return len(a)==26

print(is_pangram("1bcdefghijklmnopqrstuvwxyz"))