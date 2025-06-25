#List
"""
marks = [94.4,87.5,15.5,14.5,35.5,"apple","hee"]
print(marks)
print(type(marks))
print(marks[0])
print(len(marks))
marks[0]="Vaibhav"
print(marks) """
"""
marks = [85,55,66,82,62,55]
print(marks[1:4])

"""
#methods

"""
list = [2,1,6]
#list.append(5)
#list.sort()
#list.sort(reverse=True)
#list.insert(1,88)
#list.remove(2)
#list.pop(2)

print(list)
"""

#Tuples in Python
"""
tup = (2,1,3,5,6,8)
#print(type(tup))
print(tup[0])
"""

#methods
"""
tup = (2,3,51,4,88,6,5,7,2,2,2)
print(tup.index(3))
print(tup.count(2))
"""

# Let's Practice
# wap to ask user to enter name of there 3 favorite movies and stores them in a list
"""
mov1 = input("Enter movie:")
mov2 = input("Enter movie:")
mov3 = input("Enter movie:")

movies = []
movies.append(mov1)
movies.append(mov2)
movies.append(mov3)

print(movies)
"""
#wap to check if a list contains a palindrom of elements
"""
l1 = [1,2,3,2,1]
l2 = [2,5,8,8,8]
copy_l1 = l1.copy()
copy_l1.reverse()

if (copy_l1 == l1):
    print("Palendrom")
else:
    print("Not a palendrom")
"""

#wap to count the number of studnets wiwth the "A" grade in the followiwng tuple
# store the above values in a list and store them from A - D

grade = ["C","D","A","A","A","B","B","A"]
grade.sort()
print(grade)