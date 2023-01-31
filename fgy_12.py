k:int = int(input('sztsz első tagja: '))
d:int = int(input('sztsz differenciálja: '))

print('első 20 tag: ')
for x in range(20):
    print(k, end=' ')
    k += d