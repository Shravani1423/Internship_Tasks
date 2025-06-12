#String = string is  sequence or collections of characters
#"hello" => "h","e","l","l","o"
#string can be presented by :'' or " " or """    """

#accesing string character 
greet = "hello"


#index of string started with 0
print(greet[0])
#last character accessing with -1 index
print(greet[-1])

#python string are immutable (characters in  string are unchangeable)
message ="this is message for you. "
#count the length of string <= len()
lenght =len(message)
print(lenght)
#all name started with capital case <= title()
print(message.title())
#lower()
#upper()
#replace()
print(message.replace("message","msg"))
#isnumeric
x = int(input("enter the number for x :"))
y = int(input("enter the number for y :"))
if(x.isnumeric() and y.isnumeric()):
    print(int(x)+int(y))
else:
    print("invalid input ")

#membership oprators
a = "f" in message
print(a)
print("z" in message)