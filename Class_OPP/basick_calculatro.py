num1 = int(input("Enter the first number :"))
opperation = input("Enter the operationn :")
num2 = int(input("Enter the first number :"))

match opperation:
    case '+':
        print (num1 + num2)
    case '-':
        print (num1 - num2)
    case '*':
        print(num1 * num2)
    case '/':
        print(num1/num2)
    case _ :
        print("Invalid sintax")
