from curses.ascii import isalpha

abc = {
    'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7,'i':8,'j':9,'k':10,'l':11,'m':12,'n':13,'o':14,'p':15,'q':16,'r':17,'s':18,'t':19,'u':20,'v':21,'w':22,'x':23,'y':24,'z':25
}

key_list=list(abc.keys())

def rot13(message):
    res=[i for i in message]
    for i, char in enumerate(res):
        if isalpha(res[i]):
            if abc[res[i].lower()]+13<26:
                if res[i].isupper():
                    res[i]=key_list[abc[res[i].lower()]+13].upper()
                else:
                    res[i]=key_list[abc[res[i]]+13]
            else:
                if res[i].isupper():
                    res[i]=key_list[abc[res[i].lower()]+13-26].upper()
                else:
                    res[i]=key_list[abc[res[i]]+13-26]
                    
    return "".join(res)

print(rot13("T"))