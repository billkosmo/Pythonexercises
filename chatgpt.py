 # askhsh 1
#name = input("what is ur name? ")
#grade1 = int(input("Enter first grade: "))
#grade2 = int(input("Enter second  grade: "))
#average = (grade1+grade2)/2
#print(f"Student : {name}")
#print(f"Average : {average}")

#if average >= 5:
    #print("Passed!")
#else:
    #print("Failed!")

#askhsh 2
# while True:
#  number = int(input("guess the number: "))
#  if number > 5:
#   print("Too high!")
#  elif number <5:
#   print("Too low!")
#  else:
#   print("Correct!")
#   break
 # Ο αριθμος μου ειναι το 5

# askhsh 3

# grades = []
# sum = 0
# Passed = 0
# Failed = 0
# for i in range(5):
#     grade = int(input("Enter grade: "))
#     grades.append(grade)
#     sum+= grade
#     if grade >= 5:
#         Passed += 1
#     else:
#         Failed += 1

    




# average = sum/5


# print(f"Grades: {grades}")
# print(f"Average: {average}")
# print(f"Passed: {Passed}")
# print(f"Failed: {Failed}")



# askhsh 4

students = {}
passedstudents = []
failedstudents = []
total = 0
highest = 0
maxname = ""
lowest = 10000000
minname = ""
for i in range(5):
    name = input("Give me your name: ")
    grade = int(input("Give me your grade: "))
    students.update({name:grade})
    total += grade
    if grade >= 5:
        passedstudents.append(name)
    else:
        failedstudents.append(name)

    if grade > highest:
        highest = grade
        maxname = name

    if grade < lowest:
        lowest = grade
        minname = name 

   



average = total/5

print()
print()
print("Students:")
for keys,values in students.items():
    print(f"{keys}: {values}")
    

print()
print()
print(f"Average: {average}")

print()
print("Passed: ", end= "")

for k in passedstudents:
    print(k, end=",")
    


print()
print("Failed: ", end = "")
for q in failedstudents:
    print(q, end =",")



print()
print()
print(f"Highest Grade: {maxname}-{highest}")
print(f"Lowest Grade: {minname}-{lowest}")