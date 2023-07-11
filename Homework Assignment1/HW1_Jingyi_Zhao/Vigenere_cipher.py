def vigenere_encrypt(plain, key):
    """
    :param plain: String -- a python input string. The plain text.
    :param key: String -- a python input string. The key.

    :return: String -- the cipher python string text.
    """
    # To do
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    table = {}
    for i in range(26):
        table[letters[i]] = i
    
    while len(key) < len(plain):
        key += key
    
    output =''
    for index in range(len(plain)):
        new_index = table[plain[index]] + table[key[index]]
        if new_index > 25:
            new_index -= 26
        output += letters[new_index]
    return output
    

def vigenere_decrypt(cipher, key):
    '''
    :param cipher: String -- a python input string. The cipher text.
    :param key: String -- a python input string. The key.

    :return: String -- the plain python string text.
    '''
    # To do
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    table = {}
    for i in range(26):
        table[letters[i]] = i
    
    while len(key) < len(cipher):
        key += key
    
    output =''
    for index in range(len(cipher)):
        new_index = table[cipher[index]] - table[key[index]]
        if new_index < 0:
            new_index += 26
        output += letters[new_index]
    return output   


'''
note: 
To get autograded on gradescope, you program can't print anything.

Thus, please comment out the main function call, if you are submitting for auto grading.

'''
def main():
    print(vigenere_encrypt("ATTACKATDAWN", "NYUSH"))   # NRNSJXYNVHJL

    print(vigenere_encrypt("DATASTRUCTURE", "NYUSH"))   # QYNSZGPOUAHPY

    print(vigenere_encrypt("ABCDEFGHIJKLMNOPQRSTUVWXYZ", "NYUSH"))  # NZWVLSEBAQXJGFVCOLKAHTQPFM

    print(vigenere_encrypt("CUTE", "NYUSH"))  # PSNW

    print(vigenere_decrypt("NRNSJXYNVHJL", "NYUSH"))   # ATTACKATDAWN
    print(vigenere_decrypt("QYNSZGPOUAHPY", "NYUSH"))   # DATASTRUCTURE
    print(vigenere_decrypt("NZWVLSEBAQXJGFVCOLKAHTQPFM", "NYUSH"))   # ABCDEFGHIJKLMNOPQRSTUVWXYZ
    print(vigenere_decrypt("PSNW", "NYUSH"))  # CUTE

# if __name__ == '__main__':
#     main()
