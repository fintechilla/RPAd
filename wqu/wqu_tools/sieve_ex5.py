import lec2 as lec2


def list_true(n):
    nums = []
    nums.append(False)
    nums.append(False)
    for i in range(2, n + 1):
        nums.append(True)
    return nums


assert len(list_true(20)) == 21
assert list_true(20)[0] is False
assert list_true(20)[1] is False


def mark_false(bool_list, p):
    len_list = len(bool_list)
    for i in range(2, len_list):
        if (i * p) < len_list:
            bool_list[i * p] = False
    return bool_list


assert mark_false(list_true(6), 2) == [False, False, True, True, False, True, False]


def find_next(bool_list, p):
    len_list = len(bool_list)
    x = None
    for i in range(p + 1, len_list):
        if bool_list[i]:
            return i
    return x


def prime_from_list(bool_list):
    ret_list = []
    i = 2
    while i <= len(bool_list):
        pos = find_next(bool_list, i)
        print("i: {}, pos: {}".format(i, pos))
        if pos is not None:
            ret_list.append(pos)
            i = pos
        else:
            return ret_list

    return ret_list


# assert find_next([True, True, True, True], 2) == 3
# assert find_next([True, True, True, False], 2) is None
# assert find_next([True, True, True, False, False, True], 3)
# assert find_next([False, False, False, False, False, True, True], 4) == 5
# assert prime_from_list([False, False, True, True, False]) == [2, 3]


def sieve(n):
    bool_list = list_true(n)
    # print("len(list): {}; list_true: {}".format(len(bool_list), bool_list))
    p = 2
    while p is not None:
        bool_list = mark_false(bool_list, p)
        # print("p: {}, bool_list: {}".format(p, bool_list))
        p = find_next(bool_list, p)
        # print("P - next: {}".format(p))

    return prime_from_list(bool_list)


# assert sieve(1000) == lec2.get_primes(1000)
z = 1000
# print("result: {}".format(sieve(z)))
# print("get_primes: {}".format(lec2.get_primes(z)))
assert sieve(z) == lec2.get_primes(z)

# assert 1 == 1