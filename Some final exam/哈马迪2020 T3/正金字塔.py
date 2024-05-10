def f(n):
    lines = []
    count = 0
    for row in range(n):
        print(' ' * (n-row-1), end='')
        for col in range(2*row+1):
            print(chr(ord('A') + count % 26), end='')
            count += 1
        print()
print(f(5))