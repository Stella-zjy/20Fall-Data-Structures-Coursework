def anagram(string1, string2):
    """
    :param string1: String -- the first python string.
    :param string2: String -- the second python string.

    :return: True if string1 is anagram of string2
             False otherwise.
    """
    # To do
    s1 = ''
    for i in string1:
        if i.isalpha():
            s1 += i.lower()
    s2 = ''
    for i in string2:
        if i.isalpha():
            s2 += i.lower()
    l1 = list(s1)
    l1.sort()
    l2 = list(s2)
    l2.sort()
    if l1 == l2:
        return True
    return False
    

'''
note: 
To get autograded on gradescope, you program can't print anything.

Thus, please comment out the main function call, if you are submitting for auto grading.

'''

def main():
    string1 = "william shakespeare"
    string2 = "i am a weakish speller"
    print(anagram(string1, string2))   

    string1 = "software"
    string2 = "swear oft"
    print(anagram(string1, string2))  

# if __name__ == '__main__':
#     main()
