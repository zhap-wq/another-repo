#be careful of else, if you want to make things very strict,
# in if a variable is defined in a branch, you cannot access it in another branch 
# also think of comutational efficiency

import random 

def circle_operations(r,o):
    area = 3.14*r**2
    if o=="a":
        print('Area is',round(area,2))
    elif o=="p":
        perimeter = 3.14*r*2
        print('Perimeter is '+ str(round(perimeter,2)))
        
    elif o=="v":
        h = random.randint(7,10)
        print('Random height chosen:',h)
        print(f'Volume is: {area*h:.2f}')
    else:
        pass

def main():
	radius = int(input('What is the radius of your circle? '))
	options=input("What do you want to calculate, a, p, v?")
	circle_operations(radius,options)

main()          	
