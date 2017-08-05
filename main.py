#!/bin/python
#-*- coding:utf-8 -*-

# Python's studu now...

#import

#function

#main
FastPrime = 2
prime = FastPrime

print("How many?")
count = int(input())
num = 2
p = 2

while num < count :
    if (p**(num-1)) % num == 1:
        print(str (num) + "is Prime Number")
        num += 1
    elif p**(num-1) % p == 0:
        print(str(num) + "is Number")
        num += 1

# #Exception handling
#        else :
#            print("error")
#            break

#BeforePlogram
## def fermat(p,n):
##     if (p**(n-1))%n == 1 :
##         ans ="true"
##
##     elif p**(n-1)%p == 0:
##         ans = "false"
##
##     else :
##         ans = "error"
##
##     return ans
##
## #main
## FastPrime = 2
## prime = FastPrime
##
## print("Number?")
## num=int(input())
## print(fermat(prime,num))