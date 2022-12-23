first_num = input("Enter the first number: ")
second_num = input("Enter the second number: ")
op = input("Enter the operator(+,-,*,/): ")

try:
    first_num = int(first_num)
    second_num = int(second_num)

    output = True
    if op == '+':
        result = first_num + second_num
    elif op == '-':
        result = first_num - second_num
    elif op == '*':
        result = first_num * second_num
    elif op == '/':
        result =first_num / second_num
    else:
        output = False
        print("Wrong operator")

    if output:
         print("The result is", result)

except:
    print("Please enter number only")