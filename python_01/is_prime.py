def is_prime(num):
    """判断一个数是不是素数"""
    for factor in range(2, int(num ** 0.5)+1):
        if num % factor == 0:
            return False
    return True if num != 1 else False

if __name__ == '__main__':
    num = int(input('判断素数：'))
    print(f'{num}',end='')
    if not is_prime(num):
        print('不',end='')
    print('是素数。')