def fibonacci_generator(n=0, m=1, maximum=10):
    count = 0
    while count < maximum:
        yield n
        n, m = m, n + m
        count += 1

gen = fibonacci_generator(maximum=10)
for number in gen:
    print(number)
