# WHILE LOOPS
#name = ""
#while len(name) == 0 : #lenght μετραει το μηκως της συμβολοσειρας
    #name = input("What is ur name: ")

#print(f"Hello {name}")

# FOR LOOPS

#import time # σαν μια ετοιμη βιβλιοθηκη της python
#for i in range(10,0,-1):
   #print(i)
   #time.sleep(1) # το sleep ανηκει στην βιβλιοθηκη time αλλιωσ δε θα μπορουσα να εβαζα πχ την λεξει οκευ και να δουλευε το ιδιο  
#print("SLEEP")


# FOR LOOP δε χρειαζεται να κανουμε μονο με το range γινεται πανω σε οτιδηποτε μετριετε
#for letter in "Gewrgia Faki ":
    #print(letter , end = "") 

# NESTED FOR

#rows = int(input("give me rows "))
#columns = int(input("give me columns "))
#symbol = input("give me a symbol ")

#for i in range(rows):
    #for j in range(columns):
       # print(f"{symbol} " " ", end = "") # το default end ειναι \n που αλλαζει σειρα με τα "" μενει στην ιδια 
        # βαζω fstring ωστε να προσθεσω "" για να μπει κενο αναμεσα 
    #print("")    

#BREAK CONTINUE PASS
# Break stops the loop

#while True :
    #name = input("What is your name: ")
    #if name != "":
        #break

#continue  skip the current iteration(επαναληψη)

#number = "1234-567-87"

#for i in number:
    #if i == "-":
      #  continue
   # print(f"{i}" " ", end="")

# pass does nothing
 
for i in range(5,26):
    if i == 7:
        pass
    else:
        print(i , end=",")