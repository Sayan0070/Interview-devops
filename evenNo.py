#Accept 10 n0 from user
#Store all that no into a list
#from that list find only even no
#print all list and even no
#display all the sum
L =[]
c= []
a = int(input("How many numbers you want to put: "))
for i in range(a):
    L.append(int(input("Type you numbers")))
for i in L:
    if i % 2==0:
        c.append(i)
print(c)
print(sum(c))