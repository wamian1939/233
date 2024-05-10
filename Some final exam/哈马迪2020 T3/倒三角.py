def f(height):
    # 对于倒三角的每一行
    for row in range(height-1,-1,-1):
        # 打印前导空格
        print(' ' * (height - row-1), end='')


        # 计算并打印每一行的数字序列，从中心0开始向两边递增
        # 中间是0，左边递增到1, 2, ..., row，右边也是1, 2, ..., row
        # 打印左半部分（不包括中心的0）
        for num in range(row, 0,-1):
            print(num, end='')

        # 打印中心的0
        print(0, end='')

        # 打印右半部分
        for num in range(1, row + 1):
            print(num, end='')

        # 完成一行后换行
        print()


# 调用函数查看输出
f(10)
