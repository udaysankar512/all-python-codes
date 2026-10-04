# Write a program to check if a number is prime.
num = int (input("Enter a number :"))
res = 0
for i in range(2,num):
    if num % i == 0:
       res = 1
       
if res == 1:
    print("The number is not a prime number")
else:
    print("The number is a prime number")