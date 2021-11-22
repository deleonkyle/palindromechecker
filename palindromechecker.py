def PalindromeCheck(s):
    s = s.lower()
    length = len(s)
    if length < 2:
        return True
    elif s[0] == s[length - 1]:
        return PalindromeCheck(s[1: length - 1])

    else:
        return False


userIn = input("Input a Word or number/s: ")
ans = PalindromeCheck(userIn)

if ans:
    print(userIn + " is a Palindrome")

else:
    print(userIn + " is not a Palindrome")
