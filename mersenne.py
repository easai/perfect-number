from sympy import symbols


def sqrt(x):
    y = 1
    prev = 0
    while 1 <= abs(y-prev):
        prev = y
        y = 1.0/2*(prev+x/prev)
    while (y+1)*(y+1) < x:
        y += 1
    return int(y)


def is_perfect(x):
    n = sqrt(x)
    sum = 0
    for i in range(1, n+1):
        if x % i == 0:
            sum += i
            if i != x/i:
                sum += x/i
    return 2*x == sum


p = symbols("p")
mersenne = 2**p-1
even_perfect_number = 2**(p-1)*mersenne

for i in [1, 4, 5, 7, 8]: 
    n = even_perfect_number.subs([(p, i)])
    m = mersenne.subs([(p, i)])
    desc = "is perfect." if is_perfect(n) else "is not perfect."
    print(f"p={i}, 2^p-1={m}, 2^(p-1)*mersenne={n}, {desc}")
