name = ["marry", "john", "emma"]
height = [180, 170, 190]

data = sorted(list(zip(height, name)), reverse=True)
#
# for element in data:
print(data)
new_list = []
for element in data:
    new_list.append(element[1])
print(new_list)
    

    
        
        
    