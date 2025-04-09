import math


def f(x, y):
    expr1 = 37 * math.exp(4 * (59 - 88 * x**2)) - 29 * y
    expr2 = .02 + 52 * (x**3 - y**2)**3
    return math.sqrt(expr1) + math.sqrt(expr2)


def main(x=None, y=None):
    return f(float(x), float(y))


if __name__ == "__main__":
    points = [(-0.27, .15), (.87, -.32), (.23, -.15), (.89, -.8), (.61, .34)]
    for x, y in points:
        print(f"main({x}, {y}) ≈ {main(x, y):.2e}")

