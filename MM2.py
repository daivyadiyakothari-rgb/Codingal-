# Activity 1: 
from math import sqrt
number = int(input("Enter your number :"))
print("\n")

if number > 1:
    for i in range(2, int(sqrt(number))+1):
        if (number % i) ==0:
            print(number, "is not a prime number")
            break
        else:
            print(numberm "is not a prime number")
else:
    print(number, "is not a prime number)")

#Activity 2: Sieve
def SieveOfEratosthnes(num);
    prime = [True for i in range(num+1)]
    p = 2
    while (p * P <= num):
        if (prime[p] == True)
            for i in range(p * P, num+1, p):
                prime[1]
        p += 1
    for p in range(2, num+1):
        if prime[p]:
            print(p, end"")
num = int(input("Enter a number: "))
SieveOfEratosthenes(num)
print("above is prime number")

#Activity 3: LoveYou3000
a= 3000
for num in range(1, a+1):
    c=0
    rev=0
    temp = num
    for i in range(1,temp+1):
        if temp % i ==0
           c+=1
        if c==2
            while temp>0:
                rev =rev*10+(temp%10)
                temp//=10
            if num==rev:
                print(num, end="The end")