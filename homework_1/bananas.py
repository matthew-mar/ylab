from itertools import combinations


def bananas(s):
    result = set()
    
    banana_len = len("banana") 
    for comb in combinations(range(len(s)), len(s) - banana_len):
        s_list = list(s)
        
        for i in comb:
            s_list[i] = '-'
        
        b = ''.join(s_list)
        if b.replace('-', '') == 'banana':
            result.add(b)
    
    return result
    

if __name__ == "__main__":
    assert bananas("banann") == set()
    assert bananas("banana") == {"banana"}
    assert bananas("bbananana") == {"b-an--ana", "-banana--", "-b--anana", "b-a--nana", "-banan--a",
                         "b-ana--na", "b---anana", "-bana--na", "-ba--nana", "b-anan--a",
                         "-ban--ana", "b-anana--"}
    assert bananas("bananaaa") == {"banan-a-", "banana--", "banan--a"}
    assert bananas("bananana") == {"ban--ana", "ba--nana", "bana--na", "b--anana", "banana--", "banan--a"}
