from itertools import groupby

nums = list(map(int, input().strip()))

res: list = []

for x, y in groupby(nums):
    res.append((x, sum(1 for _ in y)))

s = ""
print(*[s.join(f"({val}, {cnt})") for cnt, val in res])
