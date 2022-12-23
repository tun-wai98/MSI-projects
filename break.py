my_list = [ 1,2,3,"stop", 5, "stop", 4.1]

for i in my_list:
    print(i)
    if i == "stop":
        print("THE LOOP WILL STOP")
        break
print("This is outside of the loop")

my_list = [ 1,2,3,"stop", 5, "stop", 4.1]
index = 0
while index < len(my_list) :
    current_element = my_list[index]
    print(current_element)
    if current_element == "stop":
        print("THE LOOP WILL STOP")
        break
    index += 1

my_list = [ 1,2,3,"stop", 5, "stop", 4.1]
for i in my_list:
    if i == "stop":
        continue
    print(i)
