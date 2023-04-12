num_list = []  # initialize an empty list to store the numbers
even_sum = 0  # initialize a variable to store the sum of the even numbers

# accept 10 numbers from the user and append to the list
for i in range(10):
    num = int(input("Enter a number: "))
    num_list.append(num)

    if num % 2 == 0:  # if the number is even, add it to even_sum
        even_sum += num

    even_list = [num for num in num_list if num % 2 == 0]  # generate the list of even numbers

# print both the entire num_list and even_list
print("The original list is:", num_list)
print("The even numbers in the list are:", even_list)
print("The sum of the even numbers is:", even_sum)
