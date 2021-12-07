x = int(input('Enter Start Range: '))
y = int(input('Enter End Range: '))
numbers = []
for i in range(x, y + 1):
    count = 0
    for j in range(1, i + 1):
        if i % j == 0:
            count += 1
    if count == 2:
        numbers.append(i)
print(numbers)