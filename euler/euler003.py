'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''

def prime_factor(n):
    divisor = 2
    divisores = []
    while n != 1:
        if n % divisor == 0:
            n = n / divisor
            divisores.append(divisor)
        else:
            divisor = divisor + 1
    return divisores

if __name__ == "__main__":
    print(prime_factor(13195))
    print(prime_factor(600851475143))
