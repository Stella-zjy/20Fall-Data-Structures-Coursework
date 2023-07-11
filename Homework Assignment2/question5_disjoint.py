def three_way_disjoint(l1, l2, l3):
    """
    :param l1: List -- the first list of elements
    :param l2: List -- the second list of elements
    :param l3: List -- the third list of elements

    :return: True if l1,l2,l3 are disjoint.
    False if l1,l2,l3 are not disjoint.
    """
    l = l1 + l2 + l3
    l.sort()
    for i in range(0, len(l) - 2):
        if l[i] == l[i + 1] == l[i + 2]:
            return False
    return True

'''
Note: 
To get autograded on gradescope, you program can't print anything.

Thus, please comment out the main function call, if you are submitting for auto grading.

'''
def main():
    l1 = [1,2,3,4,5]
    l2 = [6,7,8,9,10,11,12]
    l3 = [5,13,14,15,16]
    l4 = [5,6,7,8,9,10,11]

    print(three_way_disjoint(l1,l2,l3))   # True, yes three way disjoint.
    print(three_way_disjoint(l1,l4,l3))   # False, not three way disjoint.

# if __name__ == '__main__':
#     main()
