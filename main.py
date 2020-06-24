import re

def isPalindrome(s):
        return s == s[::-1]

s = "anna"
ans = isPalindrome(s)

if ans:
        print("is a paindrome")
else:
        print("is not a palindrome")

# ========================================

def isPalindrome(s):
        return s == s[::-1]
        cleaned_isPalindrome = re.sub(r[^A-Za-z]', ('s.lower'))
    s = "kayak"
    ans = isPalindrome(s)
    print(cleaned_phrase)
if ans:
        print("is a paindrome")
else:
        print("is not a palindrome")
# ========================================

def isPalindrome(str):

    for i in range(0, int(len(str)/2)):
        if str[i] != str[len(str)-1-1]:
            return False
        return True

s = "stuntnuts"
ans = isPalindrome(s)

if (ans):
        print("is a paindrome")
else:
        print("is not a palindrome")
# ========================================    

def isPalindrome(s):
        rev = ''.join(reversed(s))
        if (s == rev):
            return True
        return False    

s = "lisaonetatenobasil"
ans = isPalindrome(s)

if ans:
        print("is a paindrome")
else:
        print("is not a palindrome")
# ========================================

def isPalindrome(s):
        return s == s[::-1]

s = "A man, a plan, a cat, a ham, a yak, a yam, a hat, a canal: Panama"
ans = isPalindrome(s)

if ans:
        print("is a paindrome")
else:
        print("is not a palindrome") 

# ========================================
def isPalindrome(s):
        return s == s[::-1]

s = "Doc, note, I dissent. A fast never prevents a fatness. I diet on cod"
ans = isPalindrome(s)

if ans:
        print("is a paindrome")
else:
        print("is not a palindrome")

    
    
    