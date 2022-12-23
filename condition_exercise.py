guess_num = int(input("Please guess a number: "))
actual_num = 100

if guess_num < actual_num :
    print("too low")
elif guess_num == actual_num:
    print("correct")
else:
    print("too high")