# Goldbach Hypothesis : >2 even number can be sum of two prime numbers 
def isPrime(n):
    if n==2 or n==3: return True
    if n%2==0 or n<2: return False
    for i in range(3, int(n**0.5)+1, 2):
        if n%i==0:
            return False
    return True

def goldbach(T):
    S = T[0]
    E = T[1]
    if S < 4 :
        S = 4
    if S % 2 == 1:
        S += 1
    for i in range(S, E+1, 2):
        isGoldbach = False
        for j in range(i // 2 + 1):
            if isPrime(j):
                k = i - j
                if isPrime(k):
                    isGoldbach = True
                    if i % ((E-S)/10)==0:
                        print('%d=%d+%d' % (i, j, k))
                    break
        if not isGoldbach:
            print('Goldbach failed !')
            break
