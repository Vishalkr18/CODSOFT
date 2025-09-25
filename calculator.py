def calculator(a,b,operation):
    if operation=="+":
        return a+b
    elif operation=="-":
        return a-b
    elif operation=="*":
        return a*b   
    elif operation=="/":
        return a/b
        
a = int(input("Enter the number a: "))
b = int(input("Enter the number b: "))
operation = input("Enter the operation: ")

print(calculator(a,b,operation))