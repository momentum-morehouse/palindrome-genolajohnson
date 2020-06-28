import re

# def is_palindrome(s):
#         return s == s[::-1]

# s = "anna"
# ans = is_palindrome(s)

# if ans:
#         print("is a palindrome")
# else:
#         print("is not a palindrome")

# # ========================================

def is_palindrome():
    word = input("Enter word or phrase: ")
    cleaned_is_palindrome = re.sub(r'[^A-Za-z]',"", word.lower())
    if cleaned_is_palindrome == cleaned_is_palindrome[::-1]:
        print(word, "is a palindrome")
    else:
        print(word, "is not a palindrome")

is_palindrome()
# ========================================

# def is_palindrome(str):

#     for i in range(0, int(len(str)/2)):
#         if str[i] != str[len(str)-1-1]:
#             return False
#         return True

# s = "stunt nuts"
# ans = is_palindrome(s)

# if (ans):
#         print("is apalindrome")
# else:
#         print("is not a palindrome")
# ========================================    

# def is_palindromee(s):
#         rev = ''.join(reversed(s))
#         if (s == rev):
#             return True
#         return False    

# s = "lisaonetatenobasil"
# ans = is_palindrome(s)

# if ans:
#         print("is a palindrome")
# else:
#         print("is not a palindrome")
# # ========================================

# def is_palindrome(s):
#         return s == s[::-1]

# s = "A man, a plan, a cat, a ham, a yak, a yam, a hat, a canal: Panama"
# ans = is_palindrome(s)

# if ans:
#         print("is a palindrome")
# else:
#         print("is not a palindrome") 

# # ========================================
# def is_palindrome(s):
#         return s == s[::-1]

# s = "Doc, note, I dissent. A fast never prevents a fatness. I diet on cod"
# ans = is_palindrome(s)

# if ans:
#         print("is a paindrome")
# else:
#         print("is not a palindrome")

    
    
    