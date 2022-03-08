def test(num):
    res = -1
    i = 2
    while res == -1 and i < 100:
        test = list(f"{num * i}")
        test2 = [int(x) for x in test]
        if sum(test2) == num:
            res = int("".join(test))
        i+=1
    return res

    
print(test(12))