def case_calculator(string):
    result = {'UpperCase':0,'LowerCase':0}
    for i in string:
        if 'A' <= i <='Z':
            result['UpperCase'] += 1
        if 'a' <= i <= 'z':
            result['LowerCase'] += 1
        else:
            pass
    return result

user_input = input("Enter a string :")
value = case_calculator(user_input)
print(value)