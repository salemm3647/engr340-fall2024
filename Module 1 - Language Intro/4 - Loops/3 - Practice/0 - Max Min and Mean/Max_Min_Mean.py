# In this assignment you will be tasked with finding the maximum and
# minimum values of a list, as well as its average.

# Here is the list in question:
list_one = [4, 58, 55, 94, 11, 89, 69, 12, 97, 2, 38, 20, 25, 6, 95, 89, 11, 89, 19, 85, 44, 28, 6, 86, 96, 21,
            11, 84, 52, 9, 19, 11, 57, 35, 76, 74, 46, 3, 72, 99, 15, 27, 40, 98, 53, 94, 21, 44, 112, 92]

# Here are the variables to store your answers in:
list_max = list_one[0]
list_min =list_one[0]
list_average = -1

# To find each value you will need to have a new For Loop,
# and use a few If Statements as well. No max() or min() functions
# allowed though, that'd be too easy.


# First Loop Here:
for element in list_one:
    if element<list_min:
        list_min=element
    else:
        continue

for element in list_one:
    if element>list_max:
        list_max=element
    else:
        continue
sum=0
for element in list_one:
    sum += element

list_average=sum/(int((len(list_one))))

print(list_min)
print(list_max)
print(list_average)



# Second Loop Here:


# Third Loop Here:
















