# 1. Write a program to print 4th element from first and 4th element from last in a tuple.
# tup=(10,20,30,40,50,60)
# print(tup[3])
# print(tup[-4])

# 2.Write a program to check whether an element exists in tuple or not.
# tup=(10,20,30,40,50,60)
# element=int(input("enter the element: "))
# if element in tup:
#     print(f"element {element} present in tuple ")
# else:
#     print(f"element {element} not in tuple")

# 3.Write a program convert list in to tuple.
# lis=[1,2,3,4,5,6,67,7,9] 
# print(tuple(lis))

# 4.Write a progeam to find the index of an item in tuple.
# tup=(12,29,30,40,50,60)
# item=int(input("enter the elemmt: "))
# if item in tup:
#     index=tup.index(item)
#     print(index)

# 5.Write a program to replace last value of tuples in list to 100.

lis = [(10, 20, 40), (40, 40, 60), (70, 80, 90)]
new_list = []
for i, tup in enumerate(lis):
    temp = list(tup)
    temp[-1] = 100
    if i == 1:
        temp[1] = 50
    new_list.append(tuple(temp))  
print(new_list)