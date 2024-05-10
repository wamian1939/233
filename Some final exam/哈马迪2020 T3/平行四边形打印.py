def f(size,bool = False):
    lines = []
    count = 0
    start = ord('A')
    if bool is False:
        for row in range(size):
            line = ''
            for col in range(size):
                line += chr(start + count % 26)
                count += 1
            if row % 2 == 0:
                line = line[::-1]
            lines.append(' ' * (size-row-1) + line)
    else:
        for row in range(size):
            line = ''
            for col in range(size):
                line += chr(start + count % 26)
                count += 1
            if row % 2 == 1:
                line = line[::-1]
            lines.append(' ' * (row) + line)

    for line in lines:
        print(line)
print(f(7,True))

