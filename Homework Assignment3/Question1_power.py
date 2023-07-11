def power(x,n):
    """
    Compute x^n, where x, n can both be negative integer.
    :param x: Int -- the base
    :param n: Int -- the exponent

    :return: Int -- x^n
    """
    if n == 0:
        return 1
    elif n == 1:
        return x
    elif n == -1:
        return 1 / x
    
    partial = n // 2
    
    if n % 2 == 0:
        return power(x, partial) * power(x, partial) 
    else:
        return power(x, partial) * power(x, partial) * x
    
def main():
    print(power(-2, 4))     # 16
    print(power(4, 3))      # 64
    print(power(-2, -3))    # -0.125

# if __name__ == '__main__':
#     main()

