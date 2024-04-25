student_dic = {
    "name": "Rahul",
    "age": 10,
    "std": 5
}

student_dic1 = {
    
    'name':"Subin",
    "age": 8,
    "std": 5
}

student_dic2 = {
    
    'name':"Subin",
    "age": 8,
    "std": 6
}



list = []

list.append(student_dic)
list.append(student_dic1)
list.append(student_dic2)

print(list)
# print(student_dic['age'])


def Classavg(student, std):
    
    total_age = 0
    count = 0
       
    for i in student:
            if i['std'] == std:
                total_age += i['age'] 
                count += 1
                
    if count == 0:
        return 0
    else:
        return total_age / count
                




print(Classavg(list, 6))
        
        
        
        
        

