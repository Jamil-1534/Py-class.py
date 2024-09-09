#range(9)=0 to 8
#range(3-10)= 3 to 10

#index n=number of element

'''Example X=(1,2,3,4,5,6,7) so n=7
and so x(4)=5'''


my_tuple = (1, 2, 3, 4, 5)

print(my_tuple)
print(my_tuple[3]) 

my_string = "hwllo world"

print(my_string[1:7:1])  
print(my_string[1:7:2])
print(my_string[0:5:1])

#Accessing all elements of sequence type
#for forlup = have to dic="for x in sequence type"
number=[3,4,5,"abc",4.5,"xyz"]
for x in number:
    print(x)
    for x in range(len(number)): #len(number)= n(number of element)
        print(number[x])


#build in methods of list in python
x=[4,6,8,9]

#append()add the new values end of the list
x.append(10)
x.append(15)
print(x)

#len() to get the size of list
print("the size of the list is:",len(x))

#use of inser() to add value in any index ir position in
x.insert(2, 10)
print("the updated list is ",x)
x.append(12)
x.append(13)
print("the updated list is ",x)

#count() to get the no. of occurences of any value in list
print(x.count(11))

#use of remove()
'''x.remove(11)
print(x)'''''#print hoi ni(jane na kan)

#use of pop() for remove last number
x.pop
print(x)
x.pop(2)
print(x)

# use of extend()
n1=[1,2,3,4]
n2=[5,6,7,8]
n1.extend(n2)
print(n1)

#use of sort()
x.sort()
print(x)

#use of recoverse()
x.remove()
print(x)

#use min()
print(min(x))

#use of max()
print(max(x))

#use of clear()
x.clear()
print(x)
