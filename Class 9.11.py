
#ways to combines things to print

#the first way, but it put in a space between $ and price 
price =3
print("the price with tax is $", price)

#a second way, string concactination
price_1=6
print("the price with tax is $"+ str(price))

#third way, formatted string
price_2=9.9
print(f'The price with tax is ${price:.2f}\n')

# * can also used for repeat strings
print("hi"*3)
