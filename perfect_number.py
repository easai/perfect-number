class PerfectNumber:
    def sqrt(self, x):
        y = 1
        prev = 0
        while 1 <= abs(y-prev):
            prev = y
            y = 1.0/2*(prev+x/prev)
        while (y+1)*(y+1) < x:
            y += 1
        return int(y)

    def factor(self, x):
        n = self.sqrt(x)
        lst = []
        for i in range(1, n+1):
            if x % i == 0:
                lst.append(i)
                if i != x/i:
                    lst.append(int(x/i))
        return lst

    def divisorFunction(self, d, k):
        res = 0
        for x in d:
            res += x**k
        return res

    def is_perfect(self, x):
        n = self.sqrt(x)
        sum = 0
        for i in range(1, n+1):
            if x % i == 0:
                sum += i
                if i != x/i:
                    sum += x/i
        return 2*x == sum


num = 28
num = 8589869056
num = 137438691328
# num = 2305843008139952128
# # num = 2658455991569831744654692615953842176
# if is_perfect(num):
#     print(f"{num} is a perfect number.")
# else:
#     print(f"{num} is not a perfect number.")

p = PerfectNumber()
if p.is_perfect(num):
    print(f"{num} is a perfect number.")
else:
    print(f"{num} is not a perfect number.")
