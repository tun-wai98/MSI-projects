numbers = [3, 6, 5, 8]

def filter_even_odd (numbers, even_or_odd):
    filtered_list = []
    for i in numbers:
        if i % 2 == even_or_odd :
            filtered_list.append(i)

    return filtered_list

print(filter_even_odd([3,5,6,8], True))
#True 1 False 0
