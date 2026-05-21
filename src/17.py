def is_palindrome(text):
    rev_text = text[::-1]
    return True if rev_text == text else False


input_text = input().strip().lower()
result = is_palindrome(input_text)
print(result)
