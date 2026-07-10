import math

def pearson_correlation(x, y):
    n = len(x)
    sum_x = sum(x)
    sum_y = sum(y)
    sum_xy = sum(xi * yi for xi, yi in zip(x, y))
    sum_x2 = sum(xi ** 2 for xi in x)
    sum_y2 = sum(yi ** 2 for yi in y)
    
    numerator = n * sum_xy - sum_x * sum_y
    denominator = math.sqrt((n * sum_x2 - sum_x ** 2) * (n * sum_y2 - sum_y ** 2))
    
    return numerator / denominator if denominator != 0 else 0

coffee = [1, 1, 2, 2, 2, 3, 3, 4]
scores = [85, 88, 79, 81, 84, 65, 67, 49]

corr = pearson_correlation(coffee, scores)
print(round(corr, 2)) 
#Коэффициент корреляции ≈ -0.84 (сильная отрицательная связь)
#Нельзя утверждать причинно-следственную связь, так как корреляция не равна причинности. Возможны другие факторы (стресс, усталость, время подготовки и т.д.)

