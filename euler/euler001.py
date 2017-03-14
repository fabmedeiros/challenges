'''
If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
'''
def sum_multi_3_5(num):
    '''Return a sum of all numbers below num multiplies of 3 or 5'''
    sum = 0
    for i in range(1, num):
        if i/3 and not i % 3:
            sum += i
        elif i/5 and not i % 5:
            sum += i
    return sum

if __name__ == '__main__':
    # test
    print(sum_multi_3_5(10))
    # question
    print(sum_multi_3_5(1000))
