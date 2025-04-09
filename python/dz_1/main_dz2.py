def main(x: float) -> float:
    if x < 31:
        result = (62 * x**7
                  - (1 - x / 71 - 58 * x**2)**6
                  - x**2)
    elif 31 <= x < 58:
        result = 28 * (88 + 33 * x)**7
    else:
        result = x**2 - x**3 - 0.03
    return result


if __name__ == "__main__":
    test_values = [95, 27, 69, -7, 50]
    for value in test_values:
        print(f"main({value}) = {main(value):.2e}")
