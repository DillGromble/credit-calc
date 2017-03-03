def genPrimes():
    primes = []
    x = 1
    while True:
        x += 1
        for p in primes:
            if x % p == 0:
                break
        else:
            primes.append(x)
            yield primes[-1]

            
doot = genPrimes()

for i in range(int(input("Prints up to Nth prime...  \nN= "))):
    print(next(doot))
        

 

