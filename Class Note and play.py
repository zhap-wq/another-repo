#string: "True" is not True
word="say"
print(word)

#integer 
a=1
print(a)

#float
b=0.2
print(b)

#boolean 
c=True
print(c)

#function to return the type of a variable 
print(type(a))
print(type(True))
print(type(1234))
print(type(1.234))
print(type(13*4))

#variable dstore individual data items, name can cotian letters, numbers and underscore, no special character e.g. @#
#you can not start with a number.
#varableesa in lowercase, use underscore to separate two words

first_name="Pu"
last_name="Zhao"
print(first_name, last_name)

# = for assigning value, == for comparing value

sum=33+90
print(sum)


#string and varable is differnt, string is printed literally, variable name is more like a symbol, in might represent a number.

day="saturday"
saturday=5
day=saturday
print(day)

#day is not "saturday" anymore since day's value is reassigned by varable saturday, which is 5

#python has alot of key words, you can't use keywords to name your variable


#arithmetic operator

addition =3+5
subtraction=4-3
multiplication=3*4
division=5/3

#return integer quotient 
floor_division=5//2

#retern remainders 
modulo=6%4

#5^2
exponentiation=5**2

#order: parentheses, expoentiation, multiplication and devision (floor dividsion,modulo), additiona and substraction
order=2+6*5%4
print(order)
