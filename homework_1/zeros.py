from math import factorial


def zeros(n):
    c = 0
    f = factorial(n)
    is_zero = True
    while is_zero:
        is_zero = f % 10 == 0
        f //= 10
        c += 1
    return c-1


if __name__ == "__main__":
    assert zeros(0) == 0
    assert zeros(6) == 1
    assert zeros(30) == 7

