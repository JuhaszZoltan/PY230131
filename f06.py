from random import randint

c:int = 0
for n in range(20):
    r:int = randint(1, 12)
    if r % 3 == 0:
        print(r, end=' ')
        c += 1
print(f'\nösszesen {c} db ilyen szám volt')