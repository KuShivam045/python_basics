def test(a,b) :
    l = []
    while a <= b:
        l.append(a)
        a = a + 2
    else:
        print("Else this  is going to block")
    return l
a = int(input("Enter the value of a\t"))
b = int(input("Enter the value of b\t"))
# lst = test(l)

c = test(a,b)
print(c)