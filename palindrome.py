def isPalindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False

print(isPalindrome("abcdcba"))  # TRUE
print(isPalindrome("aba")) # TRUE
print(isPalindrome("c"))  # TRUE
print(isPalindrome("radar"))  # TRUE
print(isPalindrome("level"))  # TRUE
print(isPalindrome("pencil"))  # FALSE
print(isPalindrome("ark"))  # FALSE
print(isPalindrome("aa"))  # TRUE