from math import floor


def zeros(n):
    c = 0
    while (n != 0):
        c += int(floor(n / 5))
        n /= 5
    return c


if __name__ == "__main__":
    assert zeros(0) == 0
    assert zeros(6) == 1
    assert zeros(30) == 7
