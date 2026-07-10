def expected_winners():
    n = 80  # участников
    # Матожидание = n * 1/4
    return round(n * 0.25, 1)

print(expected_winners())  # 20.0
