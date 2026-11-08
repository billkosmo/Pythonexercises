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

# students = {}
# passedstudents = []
# failedstudents = []
# total = 0
# highest = 0
# maxname = ""
# lowest = 10000000
# minname = ""
# for i in range(5):
#      name = input("Give me your name: ")
#      grade = int(input("Give me your grade: "))
#      students.update({name:grade})
#      total += grade
#      if grade >= 5:
#         passedstudents.append(name)
#      else:
#          failedstudents.append(name)

#      if grade > highest:
#          highest = grade
#          maxname = name

#      if grade < lowest:
#          lowest = grade
#          minname = name 

   



# average = total/5

# print()
# print()
# print("Students:")
# for keys,values in students.items():
#      print(f"{keys}: {values}")
    

# print()
# print()
# print(f"Average: {average}")
# print()
# print("Passed: ", end= "")

# for k in passedstudents:
#      print(k, end=",")
    


# print()
# print("Failed: ", end = "")
# for q in failedstudents:
#      print(q, end =",")



# print()
# print()
# print(f"Highest Grade: {maxname}-{highest}")
# print(f"Lowest Grade: {minname}-{lowest}")

# stu = input("Give me a name: ")
# if stu in students:
#     print(students[stu])
# else:
#     print("Student not found")













#askhsh 5
# products = {}
# tc = 0
# cheapest = None
# onmin = ""
# moreexpensive = None
# onmax = ""
# for i in range(5):
#     prod = input("Give me a product: ")
#     price = float(input("Give me the price: "))
#     products[prod] = price
#     tc += price
#     if moreexpensive == None or price > moreexpensive:
#         moreexpensive = price
#         onmax = prod
#     if cheapest == None or price < cheapest:
#         cheapest = price
#         onmin = prod


# print("Products: ")
# for keys,values in products.items():
#     print(f"{keys}: {values}")

# print()
# print()
# print(f"Total: {tc}")

# print()
# print()
# print(f"Most expensive: {onmax} - {moreexpensive}")
# print()
# print(f"Cheapest: {onmin} - {cheapest}")

# print()
# print()

# sp = input("Search product: ")
# if sp in products:
#     print(f"Price: {products[sp]}")
# else:
#     print("product not found!")

#askhsh 6


bank  = {
    "customer1": {
        "name": "Nikos",
        "PIN": 1234,
        "balance": 500,
        "history":[]
        
    },
    "customer2": {
        "name": "Maria",
        "PIN": 5678,
        "balance": 1200,
        "history":[]
        
    },
    "customer3":{
        "name":"John",
        "PIN":4321,
        "balance":750,
        "history":[]
        
    }
}
tryes = 0
k = 0
while tryes < 3:
   if k == 1:
    break
   user = input("Username: ")
   pin = int(input("PIN:"))
   print() 
   if user in bank and pin == bank[user]["PIN"]:
    print(f"Welcome {bank[user]["name"]}!")
    print()
    print()
    
    while True:
      print("""1. Check balance
2. Deposit money
3. Withdraw money
4. Transaction history
5. Logout""")
      print()
      opt = int(input("Choose an option: "))
      if opt == 1:
           print(f"Balance: {bank[user]['balance']}")
      elif opt == 2:
              dep = int(input("Give me deposit money: "))
              if dep <= 0:
                   print("You have to insert money!")
                   continue
              else:
                   bank[user]["balance"] += dep
                   bank[user]["history"].append(f"Deposit: +{dep}")
      elif opt == 3:
              draw = int(input("Give me withdraw money: "))
              if draw <= 0:
                   print("You have to type an amount!")
                   continue
              elif draw > bank[user]["balance"]:
                   print("You dont have enough money!")
                   continue
              else:
                   bank[user]["balance"] -= draw
                   bank[user]["history"].append(f"Withdraw: -{draw}")
      elif opt == 4:
              print("Transaction History: ")
              print()
              print()
              for i in bank[user]["history"]:
                   print(i)
              print()
              print()
              print(f"Current balance: {bank[user]['balance']}")
      elif opt == 5:
              print("Logout")
              k = 1
              break
      else:
           print("Invalid option!")
   else:
        tryes += 1
        print("Wrong username or PIN!")
        print(f"Attempts remaining: {3 - tryes}")

if tryes == 3:
    print("Account locked!")


            
       
                           
                   

          


         






