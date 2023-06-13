def encrypt(plaintext):
    for j in range(26):
        str_list = list(plaintext)
        i = 0 
        while i < len(plaintext):
            if not str_list[i].isalpha():
                str_list[i] = str_list[i]
            else:
                a = "A" if str_list[i].isupper() else "a"
                str_list[i] = chr((ord(str_list[i]) - ord(a) + j) % 26 + ord(a))
            i  = i + 1
        print ''.join(str_list)

if __name__ == "__main__":
    plaintext = "abc"
    encrypt(plaintext)
