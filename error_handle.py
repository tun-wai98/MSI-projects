first_num = input("Enter first number: ")
second_num = input("Enter second number: ")

try:
    first_num = int(first_num)
    second_num = int(second_num)

    result = first_num + second_num

    print("The result is", result)

except:
    print("Please enter number only")