my_list = [ 1,2,'s', 3.1]
print(list(enumerate(my_list)))

for i, c in enumerate(my_list):
    print(i)
    print(c)