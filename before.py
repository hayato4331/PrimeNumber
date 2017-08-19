#!/bin/python
#-*- coding:utf-8 -*-

# Python's studu now...

#import

#function
def fermat(p,n):
    if (p**(n-1))%n == 1 :
        ans ="true"

    elif p**(n-1)%p == 0:
        ans = "false"

    else :
        ans = "error"

    return ans

#main
FastPrime = 2
prime = FastPrime

print("Number?")
num=int(input())
print(fermat(prime,num))