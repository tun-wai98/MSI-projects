marks = int(input("Please enter your mark: "))

if marks < 40 :
    print("Fail")
elif 40 <= marks < 60 :
    print("Pass")
elif 60 <= marks < 80 :
    print("Credit")
elif 80 <= marks <= 100 :
    print("Distinction")
else :
    print("Out of range")

guess_num = int(input("Please enter a number"))
actual_num = 100

if guess_num < 100:
    print("too low")
elif guess_num == 100:
    print(correct)
else:
    print("too high")
