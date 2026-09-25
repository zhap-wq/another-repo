#class 9.9 note

# function takes parentheses and it is used to perform actions, indicated by ()
#some functions built into language others in modules bundled with Python 
#some function we learn: type(), print(), input()

#input function
input()

#output function: print()

#input output together: separate line way  
print("Your name is: ")
name=input()
print("Hello "+name)

#another way: same line way 
name=input("Your name is: ")
print("hello "+name)
# you can only + a same type of value, + int, concatinate strings, interger+float=float

#every input is through input() is interpreted as a string.
#if you want the input as number and stored it as an number. Please store it using type transformation.
#Convert the value to int or float 
#Here is an right example

name= int(input("Your lucky number: "))
sq=name**2
print ("The number squar of it is :", sq)

#or if you want float:
name_2= float(input("Your lucky number: "))
sq_2=name_2 ** 2
print ("The number squar of it is :", sq_2) 

#print things seperated using comma
print(6, "Hello")

#round(value, a) will use to round value to a decimal places.
print(round(sq_2 , 2))
