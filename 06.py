#dictionary
#colection of items or elements
#is presrnt in key:values format
#is denoted by {}
#example
# emp ={
#     "name" :"john",
#     "age" :32,
#     "position" :"softwer devloper"
# }
#accesings values in dictionary
#doesn't supported to indexing
#values are access with the help of key

# print(emp)
# print(emp["age"])

#add new data in dictionary
# emp["salary"]=3.5
# print(emp)

#remove an element
# del emp["age"]
# print(emp)

#update
# emp.update()

#methods of dictionary
#values()
# print("----------- values ------------")
# print(emp.values())
# for v in emp.values():
#     print(v)
# #keys()
# print("----------- keys ------------")
# print(emp.keys())
# for v in emp.keys():
#     print(v)
# #items()
# print("----------- items ------------")
# print(emp.items())
# for v in emp.items():
#     print(v)

#multiple emplyees 
#list of dictioner
emp =[]
size =int(input("enter number of employees :"))

for i in range(1, size+1):
    emp1={}
    print(f" ----------- employee{i} details ----------")
    eid =int(input("enter emp id :"))
    name =input("enter emp name :")
    email=input("enter emp email :")
    emp.append(
        {
            "id":eid,
            "name":name.title(),
            "email": email.lower(),

        }
    )
    for emp1 in emp :
        for key,value in emp.items ():
            print(f"{key.title()} : {value}")
