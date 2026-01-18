total_list = {}


def test_function(func, limit):
    for x in range(1, limit + 1):
        for y in range(1, limit + 1):
            if get(x, y, func) != get(y, x, func):
                return False
    return True


def get(x, y, func):
    res = y
    for i in range(x):
        res = func[res]
    return res


def get_function(limit, n=1, func={}):
    #print(n, limit, count, func)
    count = 0
    if n <= limit:
        for i in range(1, limit + 1):
            func[n] = i
            count += get_function(limit, n + 1, func)
        return count
    else:
        if test_function(func, limit):
            #print(func)
            total_list[func[1]] = total_list.get(func[1], 0) + 1
            return 1
    return 0


def fill_function(limit, func):
    for x in range(1, limit):
        if x in func:
            val = func[x]
            if val in func:
                func[x + 1] = func[val]


if __name__ == "__main__":
    print(get_function(3))
    print(total_list)
    total_list = {}
    print(get_function(4))
    print(total_list)
    total_list = {}
    print(get_function(5))
    print(total_list)
    total_list = {}
    print(get_function(6))
    print(total_list)
    total_list = {}
    print(get_function(7))
    print(total_list)
    total_list = {}
    print(get_function(8))
    print(total_list)
    total_list = {}
    print(get_function(9))
    print(total_list)
    total_list = {}
    # func = {}
    # count = 0
    # for i in range(1, n + 1):
    #     ct = 0
    #     for j in range(1, n + 1):
    #         for k in range(1, n + 1):
    #             for m in range(1, n + 1):
    #                 for l in range(1, n + 1):
    #                     func[1] = i
    #                     func[2] = j
    #                     func[3] = k
    #                     func[4] = m
    #                     func[5] = l
    #                     if test_function(func):
    #                         #print(func)
    #                         count += 1
    #                         ct += 1
    #     print(ct)
    # print(count)
