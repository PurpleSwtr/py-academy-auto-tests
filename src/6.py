s = input()

new = ""

for char in s:
    up_char = char.upper()
    new_char = char.lower() if char.isupper() else char.upper()
    new += new_char

print(new)
