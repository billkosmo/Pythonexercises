#STRING SLICING
 #index[] πιο ευκολο δουλευει με τις ανωκατω τελειες
#slice()  πιο δυσκολο δουλευει με το κομμα
#[start:stop:step]
 
#name = "gewrgia faki"
# η αριθμηση των θεσεων αρχιζει απο το 0
#first_name = name[0:3]
# ο δεικτης start ειναι inclusive δλδ η αρχη εμπεριεχεται
# ο δεικτης stop ειναι exclusive δλδ το τελος δεν εμπεριεχεται
# στην θεση οπου θελω να σταματησω κανω +1 

#last_name = name[8:12]


#print(first_name)
#print(last_name)

#αμα στο start το αφησεις κενο η Python καταλαβαινει οτι αρχιζει απο την αρχη δλδ απο την θεση 0
# αντιστοιχα και για υο stop η python κτλβαινει οτι τοτ θες μεχρι το τελος μεχρι την θεση n

#loco_gewrgia = name[::2]
# το step σου λεει ανα ποσες θεσεις θα περνει ενα γραμμα απο το str
#print(loco_gewrgia)

#anapodo_gamwtw = name[::-1]
# αμα θες η αριθμηση σου να αρχιζει απο το τελος δλδ απο τα δεξια προς τα αριστερα τοτε τα steps αρχιζουν απο το -1..
#print(anapodo_gamwtw)

url1 = "https://google.com"
slice1 = slice(8,14)
#print(url1[slice])
#το slice ουσιαστικα το φτιαχνεις σαν ενα μεμονομενο tool και πας και το βαζεις πανω σε ενα str για να δουλεψει με τις αγγιλες
 
slice2 = slice(8,-4)
print(url1[slice2])