def expected_unique_animals():
    n = 6  # количество визитов
    k = 6  # количество видов животных
    # Ожидаемое число уникальных видов = k * (1 - (1 - 1/k)^n)
    exp = k * (1 - (1 - 1/k) ** n)
    return round(exp, 2)

print(expected_unique_animals())
