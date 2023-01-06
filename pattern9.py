height = int(input('Enter height : '))

for row in range(1, height+1):
    for _ in range(height-row):
        print(' ', end='')
    for i in range(1, row+1):
        print(i, end=' ')
    print()