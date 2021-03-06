from random import randrange, getrandbits
import sys
import fileinput
def is_prime(n, k=128):
    # To test if a number is prime
    """
        Args: n = Number to be tested
            : k = Number of tests
    """
    if n == 2 or n == 3:
        return True

    if n <= 1 or n % 2 == 0:
        return False

    # find r and s
    s = 0
    r = n - 1
    while r & 1 == 0:
        s += 1
        r //= 2
    # do k tests
    for _ in range(k):
        a = randrange(2, n - 1)
        x = pow(a, r, n)
        if x != 1 and x != n - 1:
            j = 1
            while j < s and x != n - 1:
                x = pow(x, 2, n)
                if x == 1:
                    return False
                j += 1
            if x != n - 1:
                return False
    return True
def generate_prime_candidate(length):
    """ Generate an odd integer randomly
        Args:
            length -- int -- the length of the number to generate, in bits
        return a integer
    """
    # generate random bits
    p = getrandbits(length)
    # apply a mask to set MSB and LSB to 1
    p |= (1 << length - 1) | 1
    return p
def generate_prime_number(length=128):
    """ Generate a prime
        Args:
            length -- int -- length of the prime to generate, in          bits
        return a prime
    """
    p = 4
    # keep generating while the primality test fail
    while not is_prime(p, 128):
        p = generate_prime_candidate(length)
    return p


def genp(l):
    return generate_prime_number(int(l))

def geng(l):
    return generate_prime_number(int(l-1))

def genpk(p):
    return randrange(1,int(p))

def calg(g,x,p):
    return pow(int(g),int(x),int(p))

InputFile = sys.argv[1]
OutputFile = sys.argv[2]
testcasecount = 0
f=open(InputFile,"r")
for x in f:
    testcasecount=testcasecount+1
    print("\n#TEST CASE "+ str(testcasecount))
    a=x.split()
    p,g,a,b = [ long(a[value]) for value in range(4)]
    Ga = calg(g,a,p)
    print("Ga = " + str(Ga))
    Gb = calg(g,b,p)
    print("Gb = " + str(Gb))
    Gab = calg(Gb,a,p)
    print("Gab = " + str(Gab))
    Gba = calg(Ga,b,p)
    print("Gba = " + str(Gba))
    print("Gab = " + str(Gab) + " and Gba = "  + str(Gba))

    with open(OutputFile, 'a' ) as Output:
        Answer = str("\nAlice's secret key (Gab): " + str(Gab) + " and " + "Bob's secret key (Gba): " + str(Gba)+ "\n")
        Answer += str("As both of them match, a Diffie Hellman Key was successfully established!\n\n")
        Output.write(Answer)

    print("\n")
