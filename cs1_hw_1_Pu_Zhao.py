import random 
# Heat Index Calculator
t=float(input("What is the temperature in Fahrenheit? :"))
h=float(input("What is the relative humidity as a percent? :"))
hi=round(-42.379 + 2.04901523*t + 10.14333127*h - 0.22475541*t*h - 0.00683783*t*t - 0.05481717*h*h
+ 0.00122874*t*t*h + 0.00085282*t*h*h - 0.00000199*t*t*h*h)
print("The heat index is", hi, "!")

# Currency Conversion
price=float(input("What is the cost of the item ? "))
p_to_d= round(price/0.74, 2)
d_to_p= round(price*0.74,  2)
print("Using the curren exchange rate of $1=\u00A30.74 :")
print("A \u00A3",price, "item from Britain would cost $", p_to_d,"in U.S. dollars.")
print("A $", price, "item from the U.S. would cost \u00A3",d_to_p, "in British pounds.")

#Mad lib
print("the computer will generate a BC mad lib for you. Please choose some words first:")
a=input("plural noun:")
b=input("adjective:")
c=input("adverb:")
d=input("transitive verb (present tense plural):")
r_1=random.randint(1,3)
r_2=random.randint(1,3)
r_3=random.randint(1,3)
r_4=random.randint(1,3)

print("Boston College has lots of marron and gold "+(a+' ')*r_1)
print("Their football team is "+(b+' ')*r_2)
print("The students "+ (c+' ')*r_3+(d+' ')*r_4+"Baldwin the Eagle")

