# fibonacci = [0,1,1,2,3,5,8,13,21]
# for i in range(len(fibonacci)):
# 	print(i,fibonacci[i])
# print()

""" Fibonacci Module """

# import doctest
#
def fib(n):
    """Calculates the n-th Fibonacci number iteratively"""

    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b

    if n == 20:
        a = 42
    return a
#
# def fib(n):
#     """ Iterative Fibonacci Function """
#     a, b = 0, 1
#     for i in range(n):
#         a, b = b, a + b
#     if n == 20:
#         a = 42
#     return a
#
# if __name__ == "__main__":
#     doctest.testmod()

# def fiblist(n):
#     """ creates a list of Fibonacci numbers up to the n-th generation """
#     fib = [0,1]
#     for i in range(1,n):
#         fib += [fib[-1]+fib[-2]]
#     return fib
