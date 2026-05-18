from functools import reduce

numbers = list(map(int, input().split()))

r = reduce(lambda x, y: x * y, numbers)
print(str(r))
