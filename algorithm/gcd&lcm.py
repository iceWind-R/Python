def gcd(x, y):
    # 最大公约数
    (x, y) = (x, y) if x < y else (y, x)
    for factor in range(x, 0, -1):
        if x % factor == 0 and y % factor == 0:
            return factor

def lcm(x, y):
    # 最小公倍数
    return x * y // gcd(x, y)

if __name__ == '__main__':
    x = int(input('请输入x：'))
    y = int(input('请输入y：'))

    print(f'最大公约数：{gcd(x, y)}')
    print(f'最小公倍数：{lcm(x, y)}')
