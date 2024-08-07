s = input("Enter a string: ")
is_palindrome = True
length = len(s)
for i in range(length // 2):
    if s[i] != s[length - i - 1]:
        is_palindrome = False
        break
if is_palindrome:
    print(s, "is a palindrome")
else:
    print(s, "is not a palindrome")
