# x = (1, 2, 3, 4)
# y = x

# x = (1, 2, 3)


# print(x, y)

# x = [1, 2, 3, 4, 5]

# y = x

# x[0] = 6

# print(x, y)

# str = "Subin"

# y = str

# str = "Poornima"

# print(str, y)

def get_largest_number(number, n):
    number.sort()
    
    return number[-n:]

nums = [1, 55, 898, 33, 3, 43 , 8]

print(nums)
largest = get_largest_number(nums, 2)
print(nums)

