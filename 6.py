strng1= input("enter the sentence: ")
strnot=strng1.find('not')
strpoor=strng1.find('poor')
if strnot > strpoor > 0 and strnot>0:
    strng1=strng1.replace(strng1[strnot:(strpoor + 4)], 'good')
    print(strng1)
else:
    print(strng1)