def vowel_or_consonant(ch):
     if ch.lower() in ['a', 'e', 'i', 'o', 'u']:
         print(f"{ch} is a vowel.")
     else:
         print(f"{ch} is a consonant.")
ch = input("Enter a character: ")
vowel_or_consonant(ch)