user_inpput = input("Enter a string :")
result = {'upperCase':0,'lowerCase':0}
for i in user_inpput:
    if 'A' <= i <='Z':
        result['upperCase'] += 1
    if 'a' <= i <= 'z':
        result['lowerCase']+= 1
    else :
        pass

print(result)