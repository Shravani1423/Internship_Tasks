# a = input("enter the first number :")
# b = input("enter the second number :")
#print(a + b)

#int, float, str, list, tuple, dic, set, complex, boolen
#convert one data type into another type
#implicit - Auto - same category
# c = int(a)+float(b)
# print("the value of c is ",c , " with type", type(c))
#explicit - 
# print("the value of c is ",int(c) , " with type", type(c))

#formatted string 
# print(f"the value of c is {c} and type of c is {type(c)}")


#operators
#used to perform certain operations of variable and values
#arithmatic
# +, -, /, *, //, %, **

#logical
#  and, or, not

#bitwise
# &, |, ~, ^, >>, <<

#comparision
# ==, !=, <, >, <=, >=

#assingment
#=, +=, -=, *=, /=, %=, **=

#special
# identity =>  is,  is not
#membership => in, not in


print("--------------------------- decition making / conditional statements --------------------------------")

#if, else, elif

#if => spicified condition when met , execute the respective block of code
# num =int(input("enter the number : "))
# if num > 0:
#     print(f"{num} number is positive ")

#if else 
# num =int(input("enter the number : "))
# if num > 0:
#     print(f"{num} number is positive ")

# else :
#     print("f{num} number is negative ")


# if - elif- else
num =int(input("enter the number : "))
if num > 0:
    print(f"{num} number is positive ")

elif num == 0:
    print(f"{num} number is zero ")

else :
    print(f"{num} number is negative ")