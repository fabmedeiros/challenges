'''
Each new term in the Fibonacci sequence is generated by adding the previous
two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed
four million, find the sum of the even-valued terms.
'''

def fibonacci_sum_even(limit):
    '''Return a sum of even fibonacci numbers above limit'''
    sumfib = 0
    a = 0
    b = 1
    while(b < limit):
        t = a
        a = b
        b += t
        if not b % 2:
            sumfib += b
    return sumfib

if __name__ == '__main__':
    print(fibonacci_sum_even(4000000))
