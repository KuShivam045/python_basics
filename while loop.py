a = int(input("enter the number \t"))
digit = 40
b = []
while digit <= a:
    if digit % 3 == 0:
        b.append(digit)
    digit = digit + 1
print(b)
print(sum(b))