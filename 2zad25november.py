#tazi funkciq obrushta niz s izpolzvane na slice
def reverse(s):
    return s[::-1]
print(reverse("Hello"))

#tazi funkciq obrushta niz s rekursiq
def recursive(s):
    if len(s)==0:
        return s
    else:
        return s[-1] + recursive(s[:-1])
print(recursive("Hello"))