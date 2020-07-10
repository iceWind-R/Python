def is_palindrome(num):
    """判断回文数"""
    temp = num
    total = 0
    while temp > 0:
        total = total * 10 + temp % 10
        temp //= 10
    return total == num

if __name__ == '__main__':
    num = int(input('判断回文数：'))
    print(f'{num}',end='')
    if not is_palindrome(num):
        print('不',end='')
    print('是回文数。')