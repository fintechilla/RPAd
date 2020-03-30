# import wqu_tools.lec1 as lec1
import wqu_tools.lec2 as lec2
def lucas_lehmer(p):
    # print("lucas_lehmer(p) produces lucas_lehmer series for given p-exp")
    ns = [4]
    i = len(ns) - 1
    for i in range(p - 2):
        ns.append((ns[i]**2 - 2) % (2**p - 1))

    return ns

# p = 7
# print("IN lec3: e.g.: lucas_lehmer({}) = ".format(p), " ", lucas_lehmer(p))
# print("length of LL for p = {};".format(len(lucas_lehmer(p))))
p = 17
print("IN lec3: e.g.: lucas_lehmer({}) = ".format(p), " ", lucas_lehmer(p))
print("length of LL for p = {};".format(len(lucas_lehmer(p))))

def get_marsennes(p_start, p_end):
    m_list = []
    for p in range(p_start, p_end):
        m_list.append(2**p - 1)

    return m_list


def ll_prime(p):
    # print("ll_prime(p) determines whether a given exponent for a mersenne number produces a prime mersenne number w/use of l_l series")
    lucas_lehmer_series = lucas_lehmer(p)
    # print("In ll_prime: lucas_lehmer_series: {}".format(lucas_lehmer_series))

    if lucas_lehmer_series[p-2] == 0:
        # print("p_exp is {} result: {}".format(p, 1))
        return 1
    else:
        # print("ll_prime{} result: {}".format(p, 0))
        return 0


# p = 7
# print("ll_series result for p: {} is {}".format(p, ll_prime(p)))
mersennes = get_marsennes(2, 17)                #lec2.my_list
print("IN lec3:input to get_mersenne_primes: mersennes: {}".format(mersennes))
def get_mersenne_primes(prime_list):
    mersennesP = []
    mersenne_primes = []
    for p in prime_list:
        merNo = lec2.mersenne_number(p)
        mersennesP.append(p)
        mersenne_primes.append(ll_prime(p))

    return list(zip(mersennesP, mersenne_primes))


print("Ex.3: {}".format(get_mersenne_primes(lec2.my_list)))
# print("mersenne_primes: {}".format(mersenne_primes))  #              list(zip(mersennes, mersenne_prime)))
# # list_a = [1, 2, 3, 4]
# # list_b = [5, 6, 7, 8]
# # print(list(zip(list_a, list_b)))

# print("ll_prime+++")
# print(ll_prime(15))