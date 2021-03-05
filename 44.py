startindex = int(input("enter the start: "))
stopindex = int(input("enter the stop index: "))
step = int(input("enter the step to move"))
t1 = input("enter the list of tuple: ")
t2 = tuple(int(x) for x in t1.split(','))
__slice = t2[startindex:stopindex:]
print(__slice)
