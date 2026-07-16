# palindrome_check.py
# Check whether a given string/number is a palindrome

text = input("Enter a string or number: ").strip()

cleaned = text.replace(" ", "").lower()
if cleaned == cleaned[::-1]:
    print(f"'{text}' is a palindrome.")
else:
    print(f"'{text}' is not a palindrome.")
