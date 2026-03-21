def isPalindrome(str):
    i = 0
    j = len(str) - 1
    str = str.lower()  # convert to lowercase for making it case insensitive
    while(i < j):
        if(str[i] != str[j]):
            return False
        i += 1
        j -= 1
    
    return True

str = input()

if(isPalindrome(str)):
    print("palindrome")
else:
    print("not palindrome")