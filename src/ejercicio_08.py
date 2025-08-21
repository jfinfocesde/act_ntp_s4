def fibonacci():
    fib = (0, 1)
    while len(fib) < 20:
        fib += (fib[-1] + fib[-2],)
    impares = [n for n in fib if n % 2 != 0]
    return fib, impares
print(fibonacci())