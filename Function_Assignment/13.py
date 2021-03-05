tuple1=input("enter the tuple: ")
l1=tuple1.split(',')
t=tuple(l1)
print(t)
lst=list(t)
for i in range(len(lst)):
    lst[i]=int(lst[i])
lst.sort(key=lambda x:lst)
print(tuple(sorted(lst)))