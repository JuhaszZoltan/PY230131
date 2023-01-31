# while

x:int = 9
while x >= 1:
    print(x, end=' ')
    x -= 2

print(end='\n')

x:int = 10
while x >= 1:
    if x % 2 == 1: print(x, end=' ')
    x -= 1

print(end='\n')

for n in range(1, 10, 2):
    print(10 - n, end=' ')