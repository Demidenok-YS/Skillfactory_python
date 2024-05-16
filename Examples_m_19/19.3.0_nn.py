"""реализуем бесконечную последовательность чисел Фибоначчи, при это она будет эффективной,
потому что для вычисления каждого следующего числа нам нужно
будет хранить в памяти лишь два предыдущих значения."""

def fib():
    a,b = 0,1
    yield a
    yield b

    while True:
        a,b = b, a + b
        yield b
for num in fib():
   print(num)