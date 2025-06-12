
subListCount =int(input("how many subjects persentage you want to calculate : "))
sub =[]
for i in range(subListCount):
  mark=int(input(f"Enter your subject mark for subject {i + 1}:"))
  if(mark < 0 or mark > 100):
       print("invalid marks ")
       exit
    
  List = sub.append(mark)

fail=0
for j in sub:
    if j < 40:
        fail +=1


    if fail > 2 :
      print("FAILED")

    elif fail < 0 :
      print("ATKT")

else :
    total =(sum(sub))/subListCount

    if total >= 75:
      print(f"{total} marks so A grade")
    elif total >= 60:
        print(f"{total} marks so B grade")
    elif total >= 40:
        print(f"{total} marks so C grade")



