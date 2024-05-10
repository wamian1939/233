def f(a, b, c):
    lines = []
    count = 0
    start = c
    for row in range(b):
        line = ''
        for col in range(a):
            line += str((count + start) % 10)
            count += 1
        if row % 2 == 1:
            line = line[::-1]
        lines.append(line)
    for line in lines:
        print(line)

print(f(17,4, 5))
