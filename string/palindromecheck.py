def ispalindrome():
    s = input("Enter your string: ")#input from user
    left, right = 0, len(s) - 1 #s refers to the string we have taken

    while left < right:
        if s[left] != s[right]: #string[left] != s[right]
            return False
        left += 1
        right -= 1
    return True
res= ispalindrome()
print("Palindrome?" , res)
