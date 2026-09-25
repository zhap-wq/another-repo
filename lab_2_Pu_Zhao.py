import random
import math

def prize_per_square_inch(price, radius):
    print("Your pizza will cost $"+str(price/100))
    area=(radius*radius)*math.pi
    print("Its area is", round(area ,2),"square inches")
    final_p= price/area
    print("The cost per square inch is", str(round(final_p,2))+" cents")

def main():
    dia=float(input("What diameter pizza do you want (8-16 inches)?"))
    rad=dia/2
    pri=random.randint(1200,1800)
    prize_per_square_inch(pri,rad)

main()

def get_diners():
    dine=random.randint(5,9)
    print("There will be",dine,"diners at your table")
    
def get_courses():
    cou=random.randint(3,7)
    print("The meal will consist of",cou, "courses")
def main_2():
    print("Lunch")
    get_diners()
    print("Dinner")
    get_diners()
    get_courses()

main_2()
    
