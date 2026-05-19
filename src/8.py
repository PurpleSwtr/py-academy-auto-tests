s = input()
width = int(input())
ls = [s[i : i + width] for i in range(0, len(s), width)]
[print(line) for line in ls]
