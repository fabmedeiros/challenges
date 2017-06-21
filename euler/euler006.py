'''
The sum of the squares of the first ten natural numbers is,

1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)^2 = 55^2 = 3025

Hence the difference between the sum of the squares of the first
ten natural numbers and the square of the sum is 3025 - 385 = 2640.

Find the difference between the sum of the squares of the first
one hundred natural numbers and the square of the sum.
'''

def sum_square(n):
    square_sum = 0
    sum_square = 0
    for i in range(1, n + 1):
        square_sum += i ** 2
        sum_square += i
    return sum_square ** 2 - square_sum

if __name__ == "__main__":
    print(sum_square(10))
    print(sum_square(100))
