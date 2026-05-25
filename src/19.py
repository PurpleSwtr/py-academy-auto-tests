conditions = {
    "FizzBuzz": lambda x: x % 3 == 0 and x % 5 == 0,
    "Fizz": lambda x: x % 3 == 0,
    "Buzz": lambda x: x % 5 == 0,
}


def fizzbuzz(n: int) -> list:
    res = []
    if not isinstance(n, int):
        return res

    for num in range(1, n + 1):
        for label, check_func in conditions.items():
            if check_func(num):
                res.append(label)
                break
        else:
            res.append(str(num))

    return res


n = int(input().strip())
result = fizzbuzz(n)
for item in result:
    print(item)
