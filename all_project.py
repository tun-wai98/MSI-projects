base_number = int(input("Enter a number: "))
power_number = int(input("Enter a number: "))
exponent_number = base_number ** power_number
print("The result is", exponent_number)

first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))
third_number = int(input("Enter third number: "))
sum_result = first_number + second_number + third_number
average_result = sum_result / 3
print("The result is", average_result)

print("Hello, Welcome!")
user_text = input("Write a message: ")
user_letter = input("Write a letter: ")
letter_count = user_text.count(user_letter)
print(letter_count)
text_count = len(user_text)
# print(text_count)
percentage = letter_count / text_count * 100
print("The percentage is", percentage)
