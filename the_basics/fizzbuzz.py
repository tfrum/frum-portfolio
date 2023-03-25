array = []

for i in range(100):
    if i % 3 == 0 and i % 5 == 0:
        array.append(' fizzbuzz')
    elif i % 3 == 0:
        array.append(' fizz')
    elif i % 5 == 0:
        array.append(' buzz')
    else:
        array.append(i)

print(array)
