subListCount = int(input("How many subjects' percentages do you want to calculate: "))
sub = []

for i in range(1, subListCount + 1):
    print(f"=========== Subject {i} ============ ")
    subName = input(f"Enter your subject {i} name: ")
    marks = int(input(f"Enter your subject {i} marks: "))

    if marks < 0 or marks > 100:
        print("Invalid marks. Please enter marks between 0 and 100.")
        exit()

    sub.append({
        "subName": subName,
        "marks": marks,
    })

for subject in sub:
    for key, value in subject.items():
        print(f"{key.title()}: {value}")

fail = 0
for subject in sub:
    if subject["marks"] < 40:
        fail += 1

if fail > 2:
    print("FAILED")
elif fail > 0:
    print("ATKT")
else:
    total = sum(subject["marks"] for subject in sub)
    average = total / subListCount

    if average >= 75:
        print(f"{average} marks so A grade")
    elif average >= 60:
        print(f"{average} marks so B grade")
    elif average >= 40:
        print(f"{average} marks so C grade")
    else:
        print("You have failed.")
