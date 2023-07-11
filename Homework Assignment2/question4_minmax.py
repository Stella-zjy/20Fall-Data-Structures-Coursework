def minmax(list1):
    """
    find both the minimum and maximum within list1.
    # You can assume list1 size is even.
    required number of comparisons: 3n/2  (This is not big O, you should limit your "<", ">" comparisons)

	:param list1: List -- list of integers
    :return: a tuple of two integers. The first integer is the minimum, the second integer is the maximum.
    """
    group_of_min = []
    group_of_max = []
    
    for i in range(len(list1)//2):
        group_of_min += [min(list1[2 * i], list1[2 * i + 1])]
        group_of_max += [max(list1[2 * i], list1[2 * i + 1])]
    
    minimun = group_of_min[0]
    for each in group_of_min[1:]:
        if each < minimun:
            minimun = each
    
    maximun = group_of_max[0]
    for each in group_of_max[1:]:
        if each > maximun:
            maximun = each
 
    return (minimun, maximun)


'''
Note: 
To get autograded on gradescope, you program can't print anything.

Thus, please comment out the main function call, if you are submitting for auto grading.

'''
def main():
    print(minmax([150, 24, 79, 50, 98, 88, 345, 3]))    # (3, 345)
    print(minmax([678, 227, 764, 37, 956, 982, 118, 212, 177, 597, 519, 968, 866, 121, 771, 343, 561, 100]))  # (37, 982)

# if __name__ == '__main__':
#     main()