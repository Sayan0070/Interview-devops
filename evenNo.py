#Accept 10 n0 from user
#Store all that no into a list
#from that list find only even no
#print all list and even no
#display all the sum
L = []
c = []

while True:
    try:
        a = int(input("How many numbers do you want to put? "))
        if a > 0:
            break
        else:
            print("Please enter a positive integer.")
    except ValueError:
        print("Please enter a valid integer.")

for i in range(a):
    while True:
        try:
            num = int(input("Enter a number: "))
            L.append(num)
            break
        except ValueError:
            print("Please enter a valid integer.")

for i in L:
    if i % 2 == 0:
        c.append(i)

print("All numbers:", L)
print("Even numbers:", c)
print("Sum of even numbers:", sum(c))
