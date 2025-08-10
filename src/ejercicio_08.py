def fibonacci():
    fib = (1, 1)
    while len(fib) < 20:
        fib += (fib[-1] + fib[-2],)
    for num in fib:
        if num % 2 != 0:
            print(num)

fibonacci()
