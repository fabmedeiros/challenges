'''
A palindromic number reads the same both ways. The largest palindrome
made from the product of two 2-digit numbers is 9009 = 91 x 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''

def palindrome(n):
    s = str(n)
    i = 0
    j = len(s) - 1
    while i < j and s[i] == s[j]:
        i = i + 1
        j = j - 1
    return j <= i

def largest_palindromic_number(start, end):
    largest = 0
    for a in range(start, end):
        for b in range(start, end):
            if palindrome(a * b):
                if a * b > largest:
                    largest = a * b
    return largest

if __name__ == "__main__":
    print(largest_palindromic_number(10, 100))
    print(largest_palindromic_number(100, 1000))
