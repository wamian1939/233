from itertools import zip_longest
def f(height):
    lines = []
    count = 0
    start = ord('A')
    while height > 0:
        line = ''
        for i in range(height):
            line += chr(start + count % 26)
            count += 1
        lines.append(' ' * len(lines) + line)
        height = height - 2
    for line in zip_longest(*lines, fillvalue=' '):
        print(''.join(line).strip())


if __name__ == '__main__':
    f(11)