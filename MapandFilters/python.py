
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Works up the stack
avg = map(
        lambda n: n + 5,
        filter(lambda n: n % 2 == 0,numbers)
    )

for a in avg:
    print(a)