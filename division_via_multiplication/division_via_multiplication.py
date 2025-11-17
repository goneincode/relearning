def get_reciprocal(number: float) -> float:
    """Returns the reciprocal of a number."""
    return 1 / number


def div_via_multiplication(dividend: float, divisor: float) -> float:
    """Divides two numbers via multiplication."""
    return dividend * get_reciprocal(divisor)


if __name__ == "__main__":
    print(div_via_multiplication(float(100), float(10)))
