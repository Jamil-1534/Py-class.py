#Print
x=5
y="jamil"
print(x,y)
print(type(x))
print(type(y))
print("Margub Hasan Jamil,")
print("weacome to the Python Programing")

#Use of in Paeameter(For multipal line run in one line)
print("Margub Hasan Jamil",end="")
print(" weacome to the Python Programing",end="")
print(" Its best for you")

#Use of in Sep Paeameter(For "," add in output)
print("Margub Hasan Jamil","weacome to the Python Programing","Lab class 1",2024)
print("Margub Hasan Jamil","weacome to the Python Programing","Lab class 1",2024,sep=",")

#to multipol cotasion use 3"

#use of format(use {} to show the value)
x=5
y=6
print("value of x is {} and y is {}".format(x,y))
'''
#use of input()
x=input("Enetr the value of x")
y=input("Enetr the value of y")
print("value of x is{} and Y is {}".format(x,y))

x=int(input("Enetr the value of x"))
y=float(input("Enetr the value of y"))
print("value of x is{} and Y is {}".format(x,y))'''

a,b,c=7,8,9
a=b=c=10

#use of split()
#use of map()
a,b,c= map(int, input("Enter the value of a, b, c").split())
print(a,b,c)
#type custing
a=3
print(float(a))
print(str(a))

"""we have to read
5Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list*, tuple, range, String*
Mapping Type:	dict*
Set Types:	set, frozenset
Boolean Type:	bool"""