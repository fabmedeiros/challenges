'''
2520 is the smallest number that can be divided by each of the numbers
from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible
by all of the numbers from 1 to 20?
'''

def smallest_number(limit):
    rest = -1
    number = 0
    while not rest == 0:
        number += 1
        for i in range(limit, 0, -1):
            if not number % i == 0:
                rest = -1
                break
            else:
                rest = 0
    return number

if __name__ == "__main__":
    print(smallest_number(10))
    print(smallest_number(20))
