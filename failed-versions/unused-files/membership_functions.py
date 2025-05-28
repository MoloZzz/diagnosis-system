def triangular(x, a, b, c):
    if x <= a or x >= c:
        return 0.0
    elif x == b:
        return 1.0
    elif a < x < b:
        return (x - a) / (b - a)
    else:
        return (c - x) / (c - b)

def fuzzify_intensity(x):
    return {
        "low": triangular(x, 0, 0, 5),
        "medium": triangular(x, 3, 5, 7),
        "high": triangular(x, 5, 10, 10),
    }
