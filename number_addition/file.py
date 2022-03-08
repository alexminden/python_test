# def test(num):
#     test = []
#     value = int(num/2)+1
#     for i in range(value):
#         if i != 0:
#             test.append(int(f"{i}{num-i}"))
#             test.append(int(f"{num-i}{i}"))
#     res = sorted([x*10 for x in test]) if len([x for x in test if x % num == 0]) == 0 else sorted([x for x in test if x % num == 0])
#     return res[0]

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