div = int(input('Find all divisors of what number:  '))


print(' '.join([str(x) for x in range(1, div + 1) if div % x == 0]))
