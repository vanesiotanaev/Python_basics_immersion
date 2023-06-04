# Написать порграмму, которая выводит в консоль таблицу умножения "как на тетрадках".

print()
for i in range(2, 10):
    print()
    for j in range(2, 10):
        print(f'{i} X {j} = {i * j}')
print()