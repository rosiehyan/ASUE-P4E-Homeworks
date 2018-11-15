a = int(input("Enter a positive number. "))
primes = [] 
def primes_check(num):
    for n in range(2, num):
        if num%n == 0: 
            return False 
    return True 
def find_primes(num):
    for e in range(2, num+1):
        if primes_check(e):
            primes.append(e) 
find_primes(a)             
print(primes)

