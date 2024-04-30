dic1 = {
    "name": "Subin",
    "age": 28
}

dic2 = {
     "name": "nimi",
     "age": 10
}

dic3 = {
    "name": "Sanju",
    "age": 29
}

dic4 = {
    "name":"Suhail",
    "age": 24

}


list = [dic1, dic2, dic3, dic4]

for i in list:
    if i['name'][0] == 'S' and i['age'] > 28:
        print(i)

# print(list)

# def SearchName(list, char):
#     for i in list:
#         print(i.name == char)

# SearchName(list, 'S')

