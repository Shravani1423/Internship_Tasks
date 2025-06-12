python =int(input("Enter your python marks between(0-100) :"))
java =int(input("Enter your java marks between(0-100) :"))
C =int(input("Enter your C marks between(0-100) :"))
HTML =int(input("Enter HTML python marks between(0-100) :"))
SQL =int(input("Enter SQL python marks between(0-100) :"))

 
if(java < 0 or java>100 or
    python<0 or python>100 or 
    SQL<0 or SQL>100 or 
    C<0 or C>100 or
   HTML<0 or HTML>100 ):
   print("invalid input")

# if(0 <= python <=100 )and
# (0 <= java <=100 )and
# (0 <= C <=100 )and
# (0 <= SQL <=100 )and
# (0 <= HTML <=100 ):
  

else: 
   fail =0
   if java < 40 :
      fail +=1
   if python < 40:
    fail +=1
   if SQL < 40 :
     fail +=1
   if HTML < 40:
    fail +=1
   if C < 40:
      fail +=1

   if fail > 2 :
      print("FAILED")

   elif fail < 0 :
    print("ATKT")

   else :

      total =(python+java+SQL+C+HTML)/5

      if(total >= 75):
         print(f"{total} marks so A grade")
      elif(total >= 60 and total < 75):
        print(f"{total} marks so B grade")
      elif(total >=40 and total < 60):
          print(f"{total} marks so C grade")



