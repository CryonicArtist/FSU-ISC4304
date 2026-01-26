pattern = '*'
# Solid Square with size 5
n = 5
print("Solid square with size", n)
for i in range(n):
    for j in range(n):
        print(pattern, end='')
    print() 

# Solid Trangle with size 9
n = 9
print("Solid triangle with size", n)
for i in range(n):
    for j in range(i + 1):
        print(pattern, end='')
    print()

# Checkerboard with size 8
n = 8
print("checkerboard square with size", n)
for i in range(n):
    for j in range(n):
        if (i + j) % 2 == 0:
            print(pattern, end='')
        else:
            print(' ', end='')
    print()

pattern = 'X'

# Wild loop square
n = 5
print("Solid square with size", n)
row = 0
while row < n:
    col = 0
    while col < n:
        print(pattern, end='')
        col += 1
    print()
    row += 1

# While loop for triangle
n = 9
print("Solid triangle with size", n)
row = 0
while row < n:
    col = 0
    while col <= row:
        print(pattern, end='')
        col += 1
    print()
    row += 1

# While loop for checkerboard
n = 8
start = 0 
x = 0
y = 0
print("checkerboard square with size", n)
row = 0
while row < n:
    col = 0
    while col < n:
        if (row + col) % 2 == 0:
            print(pattern, end='')
        else:
            print(' ', end='')
        col += 1
    print()
    row += 1


# Empty Square
n = 20
print("an empty square with size", n)

corner = '*'
vertical = '|'
horizontal = '-'
row = 0
while row < n:
    col = 0
    while col < n:
        if (row == 0 or row == n - 1) and (col == 0 or col == n - 1):
            # Corners
            print(corner, end='')
        elif (row == 0 or row == n - 1):
            # Horizontal boundaries
            print(horizontal, end='')
        elif (col == 0 or col == n - 1):
            # Vertical boundaries
            print(vertical, end='')
        else:
            # Empty interior
            print(' ', end='')
        col += 1
    print()
    row += 1