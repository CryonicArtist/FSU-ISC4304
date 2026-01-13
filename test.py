a = 0
b = 10
c = 5
while a < b:
    a = a + 1
    if a < c:
        print(a, end=' ')
    else:
        print(a*a, end=' ')
print("done")