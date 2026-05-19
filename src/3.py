n = int(input())
scores = list(map(int, input().split()))

sc = sorted(set(scores))

print(list(sc)[-2])
