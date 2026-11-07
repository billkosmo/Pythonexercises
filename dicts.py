#   ΛΕΞΙΚΑ είναι μια ενσωματωμένη δομή δεδομένων που αποθηκεύει πληροφορίες με τη μορφή ζευγών κλειδιού - τιμής με τα { keys:Values }

capitals = {"USA":"Washigton","Germany":"Berlin","Russia":"Moscow"}

#print(capitals.get("Russia")) # ψαχνει το κλειδι στο λεξικο και εμφανιζει την τιμη του 
#print(capitals.get("greece")) # αμα δεν υπαρχει εμφανιζει αντιστοιχο μηνυμα

#print(capitals.values()) # μεθοδος που σου επιστρεφει ολες τις τιμες
#print(capitals.keys()) # μεθοδος που σου επιστρεφει ολα τα κλειδια

#print(capitals.items()) # επιστρεφει κλειδια και τιμες ολα μαζι


for keys in capitals.keys():
   print(keys)          # εμφανιζει μονο κλειδια μεσα σε loop 

#for values in capitals.values():
   # print(values)            # εμφανιζει μονο τιμες μεσα σε loops


#for i in capitals:
   # print(i)   # γραφοντας μονο το ονομα του λεξικου θα σου εμφανισει μονο τα κλειδια 

#capitals["Greece"] = "Athens"     
#capitals.update({"Egypt":"Cairo"})
# απο πανω εχω δυο τροπους για να προσθετεις κλειδια με τιμες στο λεξικο σου 

#capitals.pop("USA") # βγαζει κλειδι με την τιμη του μαζι απο το λεξικο 
#capitals.clear() # καθαριζει ολο το λεξικο ΑΛΛ δε το διαγραφει


#for keys,values, in capitals.items():
 #print(keys,values ) # αμα θελω να εμφανισω μεσα σε loop και κλειδια και τις τιμες τους (.items) πρεπει να βαλω και τις δυο μεταβλητες keys,values