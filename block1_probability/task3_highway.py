import math

def highway_prob():
    p30 = 0.95
    # λ = -ln(1 - p30) за 30 минут
    lambda_30 = -math.log(1 - p30)
    
    # за 10 минут
    p10 = 1 - math.exp(-lambda_30 / 3)
    # за 27 минут
    p27 = 1 - math.exp(-lambda_30 * 27 / 30)
    
    return round(p10 * 100, 1), round(p27 * 100, 1)

print(highway_prob())
