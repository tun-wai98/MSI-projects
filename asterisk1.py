#Question1
# for i in range(0,5):
#     for j in range(i+1):
#         print("*", end="")
#     print()

#question6
def triangle_star(num):
    for i in range (0, num):
        for j in range (i + 1):
            print("*", end="")
        result = print()
        
    return result

num = int(input("Please enter a number : "))

print(triangle_star(num))