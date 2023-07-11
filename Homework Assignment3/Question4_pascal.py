def pascal(n):
    """
    :param n: Int -- Levels of pascal triangle

    :return: List[List[Int]] -- a list of sublists, which contains pascal values.
    """
    if n == 1:
        return [[1]]
    elif n == 2:
        return pascal(1) + [[1, 1]]
    output = pascal(n - 1)
    x = [1]
    for i in range(n - 2):
        y = output[-1][i] + output[-1][i + 1]
        x.append(y)
    x.append(1)
    return output + [x]
        

def main():
    print(pascal(4))    # [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]]

# if __name__ == '__main__':
#     main()




