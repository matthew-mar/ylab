from functools import reduce


def count_find_num(primesL, limit):
    prod = reduce((lambda a, b: a * b), primesL, 1)
    
    if prod > limit:
        return []
    
    nums = [prod]
    
    for m in primesL:
        for n in nums:
            p = n * m
            while (p <= limit) and (p not in nums):
                nums.append(p)
                p *= m

    return [len(nums), max(nums)]


if __name__ == "__main__":
    primesL = [2, 3]
    limit = 200
    assert count_find_num(primesL, limit) == [13, 192]
    
    primesL = [2, 5]
    limit = 200
    assert count_find_num(primesL, limit) == [8, 200]
    
    primesL = [2, 3, 5]
    limit = 500
    assert count_find_num(primesL, limit) == [12, 480]
    
    primesL = [2, 3, 5]
    limit = 1000
    assert count_find_num(primesL, limit) == [19, 960]
    
    primesL = [2, 3, 47]
    limit = 200
    assert count_find_num(primesL, limit) == []
