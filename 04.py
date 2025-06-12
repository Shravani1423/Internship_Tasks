#loops

#for <= if you got sequence (collection or array type objects)
#syntax => for var in object :
# size ="4444444444"
# for i in size :
#     print(i)
#     print("hello world")

#using range 
# for i in range (3,3) :
#     print(f"{i}.hello world")

#even or odd
# for i in range(1 , 11):
#     iseven = (i%2 == 0)
#     isodd ="odd"

#     if iseven:
#         evenstr ="even"
#         print(f"{i}.hello world - {isodd} line")

#while => condotion based
#syntax: while condition
# i=1
# limit = 10
# while i <= limit:
#     iseven = (i%2 == 0)
#     isodd ="odd"

#     if iseven:
#         evenstr ="even"
#     print(f"{i}.hello world - {isodd} line")
#     i+=1

#sum of first 10 numbers using for loop
sum =0
for i in range (1, 11):
    sum += i
print(f"sum of first 10 numbers :{sum}")

#sum of first 10 numbers using while loop
# sum =0
# i = 1
# while(i<=10):
#     sum+=i
#     i+=1
# print(f"sum of numbers : {i}")

#break/pass/continue stetment and else block and control stetment
# sum =0
# for i in range (1, 11):
#     if i == 5:
#        continue
#     print(f"current number is {i}")
#     sum += i
#     if i == 5:
#        # break
#        pass
# else :
#     print(f"sum of first 10 numbers :{sum}")
 
for i in range (1,10):
    print(i)
    if i == 5:
        break
    i+=1


