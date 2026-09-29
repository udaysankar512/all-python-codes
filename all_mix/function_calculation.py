def digit_cal(num,input):
    value = 0
    retu_num = 0
    for i in range(input+1): # i = 1,2,3,4
        value = num*(10**i) # num =4 / number = 4 *10**0 = 4 when i = 0
        retu_num += value # transfer teh value in a different contenear 
    print(retu_num)
    return retu_num

def calculate(number,digit): # n + nn + nnn + nnnn  [n + (n*10 + n*1) + (n*100+n*10 +n*1) + (n*1000 +n*100+n*10 +n*1)]
    sum = 0
    for i in range(digit):
        sum += digit_cal(number,i)
    
    return sum
    
num = int(input("Enter a number :"))
upTo = int(input("Enter the digites upto you sum :"))

result = calculate(num,upTo)
print("The result is :",result)