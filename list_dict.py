#LIST OPERATIONS
l=list()
#creation of list
n=int(input("Enter the no of elements:"))
print("Enter the elements:")
for i in range(n):
    m=int(input())
    l.append(m)
print("The list created as:",l)

#appending list
it=int(input("Enter the element to add to the list:"))
l.append(it)
print("List after appending:",l)

#accessing element
ac=int(input("Enter the index to access the element:"))
print("The element at",ac,"is:",l[ac])

#slicing
beg=int(input("Enter the starting index for sublist:"))
end=int(input("Enter the ending index for sublist: "))
print("The sublist is:",l[beg:end])

#insert
inde=int(input("ENter the index to insert the element:"))
ele=int(input("Enter the element to insert:"))
l.insert(inde,ele)
print("The list after inserting the element:",l)

#Deletion
#pop
print("The popped element:",l.pop())
#remove
rel=int(input("Enter the element to remove:"))
l.remove(rel)
print("The element after removing",rel,"is:",l)

#to find length
print("The length of the list is:",len(l))

#sort
l.sort()
print("The sorted list:",l)

#reverse
l.reverse()
print("The reversed list:",l)


#DICTIONARY OPERATIONS
#Creation of dictionary
mydic={1:"Alina",2:"Krishna",3:"Mariya"}
print(mydic)

#accessing value using key 
key=int(input("Enter the key to access value:"))
print("THe value is:",mydic[key])

#accessing value using get
print(mydic.get(3))

#adding key-val
print("After adding new value:")
mydic[4]="Priya"
print(mydic)

#list of keys and values
k=mydic.keys()
print(k)
v=mydic.items()
print(v)
# Using pop() to remove a key-value pair and get its value
remval= mydic.pop(1)
print("Removed value:",remval)  

# Using popitem() to remove the last key-value pair
lastitem = mydic.popitem()
print("Last item removed:",lastitem)
