"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""
from math import sqrt
def primes(number_of_primes):
    list = []
    first_prime = 2
    if number_of_primes < 1:
        raise ValueError
    while len(list)<number_of_primes:
        isprime = True
        
        for x in range(2, int(sqrt(first_prime) + 1)):
            if first_prime % x == 0: 
                isprime = False
                break
        
        if isprime:
            list.append(first_prime)
        
        first_prime += 1
    
    return list

