def findprimes(min, max):
    for Number in range(min, max + 1):
        count = 0
        for i in range(2, (Number // 2 + 1)):
            if (Number % i == 0):
                count = count + 1
                break
        if (count == 0 and Number != 1):
            print(" %d" % Number, end='  ')
    print()


def primes():
    minimum = int(input(" Enter the Minimum Value for Primes: "))
    maximum = int(input(" Enter the Maximum Value for Primes: "))
    findprimes(minimum, maximum)

def primesTester():
    minimum = 3
    maximum = 67
    print("minimum = 3 | maximum = 54 | primes: ", end="")
    findprimes(minimum, maximum)
    print()
    minimum = 98
    maximum = 169
    print("minimum = 33 | maximum = 98 | primes: ", end="")
    findprimes(minimum, maximum)
    print()
    minimum = 473
    maximum = 576
    print("minimum = 473 | maximum = 532 | primes: ", end="")
    findprimes(minimum, maximum)

if __name__ == "__main__":
    primesTester()