import numpy as np
from math import *


def mersenne_number(p):
    return 2 ** p - 1


# print("IN lec2: mersenne_number(p=5) {}".format(mersenne_number(5)))
my_list = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61]
# print("IN lec2: my_list of primes: {}".format(my_list))


def is_prime(number):
    primeNumber = True
    if 1 <= number <= 3:
        return primeNumber

    for n in range(2, number):
        if number % n == 0:
            primeNumber = False
            return primeNumber

    return primeNumber

def get_mersenne_primes(n_start, n_end):
    # print("get mersenne primes from an assumed list of primes given p-exp: start {} and end {} points inclusive:".format(n_start, n_end))
    another_list = []
    for num in my_list:
        if num in my_list and n_start <= num <= n_end:
            another_list.append(mersenne_number(num))

    return another_list


# print("IN lec2: get_mersenne_primes(3, 65): {}".format(get_mersenne_primes(3, 65)))
def is_prime_fast(number):
    primeNumber = True
    if 1 <= number <= 3:
        return primeNumber

    for n in range(2, floor(sqrt(number)) + 1):
        if number % n == 0:
            primeNumber = False
            return primeNumber

    return primeNumber

def get_primes_fast(n):
    primes = []

    for i in range(2, n + 1):
        if is_prime_fast(i):
            primes.append(i)

    return primes

def get_primes(n):
    primes = []

    for i in range(3, n + 1):
        if is_prime(i):
            primes.append(i)

    return primes

num = 65
# print("get_primes_fast({})".format(get_primes_fast(num)))
# print("get_primes({})".format(get_primes(num)))


# n = 67867967
# # print("is_prime({}) = {}".format(n, is_prime(n)))
# #
# # print("is_prime_fast({}) = {}".format(n, is_prime_fast(n)))
#
# assert is_prime(n) == is_prime_fast(n)


# print("IN lec2: is_prime(11): {}".format(is_prime(11)))




# mersennes = get_primes(3, 65)


# print("IN lec2: mersennes: {} ". format(mersennes))

def is_prime_list(list):
    for n in list:
        print(is_prime(n))


# is_prime_list(mersennes)

# def mersenneP_exp(mersenne_list):
#     p = []
#     for el in mersenne_list:
#         print("Retrieve: el: {}".format(el))
#         temp = np.log((el + 1) / 2)
#         print("Retrieve: temp: {}".format(temp))
#         p.append(temp)
#
#     return p

# print(mersenneP_exp(mersennes))
# for n in range(10):
#     # print("n: {} {}".format(n, is_prime(n)))
#     assert is_prime(n) == is_prime_fast(n)
