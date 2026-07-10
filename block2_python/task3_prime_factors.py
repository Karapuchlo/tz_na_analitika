def prime_factors(n: int) -> list:
    factors = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1 if d == 2 else 2  # проверяем только 2 и нечётные
    if n > 1:
        factors.append(n)
    return factors

# Пример
print(prime_factors(56))
