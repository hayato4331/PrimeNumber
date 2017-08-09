#!/bin/python
#-*- coding:utf-8 -*-

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
