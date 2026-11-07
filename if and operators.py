 # comp operators >, < , >= , <= , == , != 
# logical operators and , not , or

temp = int(input("Δωσε μια θερμοκρασια: "))

if temp > 10 and temp < 30 :
    print("Βγες εξω εχει καλο καιρο")
elif temp <= 10 :
    print("εχει ψωλα μην βγεις ")
elif not(temp < 30 ) :
    print("Εχει ψωλοζεστη ")