s = input("Enter a string: ").lower()
vowel_count = 0
consonant_count = 0
vowels = "aeiou"
for char in s:
    if char.isalpha():
        if char in vowels:
            vowel_count += 1
        else:
            consonant_count += 1

print("Vowels:", vowel_count)
print("Consonants:", consonant_count)
