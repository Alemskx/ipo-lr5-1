str=input("Введи строку:")
print("Длина строки = ",len(str))
glasn=0
soglasn=0
for i in str:
    if i=="а" or i=="у" or i=="о" or i=="и" or i=="э" or i=="ы" or i=="я" or i=="ю" or i=="е" or i=="ё":
        glasn+=1
    else:
        soglasn+=1

print("Гласных букв = ",glasn)
print("Согласных букв = ",soglasn)