def vc_count(word):
    """
    ### Friendly tip: This function can't solve the problem, 
    ### you need more parameters to pass information between recursive functions.
    ### So, define another function!! Return the result from your new function!!
    
    :param word: String -- the input string
    :return: List[Int] -- the first integer is the number of vowels, 
                          the second integer is the number of consonants.
    """
    n = len(word)
    x = v_count(word, n)
    return [x, n - x]
    
def v_count(word, n) :
    if n == 1:
        if word in 'aeiouAEIOU':
            return 1
        return 0
    else:
        x = word[0]
        if x in 'aeiouAEIOU':
            return 1 + v_count(word[1:], n - 1)
        return v_count(word[1:], n - 1)
        
    

def main():
    print(vc_count("GoodMorningShanghai"))   # [7, 12]
    print(vc_count("WhatsUpGuys"))           # [3, 8]
    print(vc_count("EnjoyNationalHoliday"))  # [9, 11]
    print(vc_count("aaaaaaaaaaaaaaaAAAAA"))  # [20, 0]
    print(vc_count("hmmmmmmmmmmmmmmm"))      # [0, 16]

# if __name__ == '__main__':
#     main()
