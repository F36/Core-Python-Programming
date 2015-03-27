def gcd(x, y):
    i = min(x, y)
    while i > 0:
        if x % i == 0 and y % i == 0:
            return i
        i -= 1

def lcm(x, y):
    i = max(x, y)
    while i <= x * y:
        if i % x == 0 and i % y == 0:
            return i
        i += 1
