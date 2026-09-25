import random 
def excursion(day):
    n=random.randint(1,6)
    if day=="W":
        if n%2==0:
            print("Wednesday's trip: castle")
        elif n%3!=0:
            print("Wednesday's trip: island")
        else:
            print("Wednesday's trip: museum")
    elif day=="S":
        if n%2==0 and n%3==0:
            print("Saternday's trip: cathederal")
        elif n%2==0:
            print("Saternday's trip: zoo")
        else:
            print("Saternday's trip: park")

def main():
    excursion("W")
    excursion("S")
    print("Have fun exploring!")

main()
            
