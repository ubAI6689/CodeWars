# https://www.codewars.com/kata/5390bac347d09b7da40006f6/train/python
def to_jaden_case(string):
    ans=""
    res=string.split()
    for word in res:
        ans+=word.capitalize()
        if word is not res[len(res)-1]:
            ans+=" "
    return ans

print(to_jaden_case("hey what's up"))