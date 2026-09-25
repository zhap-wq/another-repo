def leap_year(year):
    if year % 4 !=0:
        print("Not a leap year")

    elif year % 4 ==0 and year % 100 !=0:
        print("A leap year!")

    elif year % 4 ==0 and year % 100==0 and year % 400 !=0:
        print("Not a leap year")

    else:
        print("A leap year!")

def main():
    y=int(input("Please enter a year: "))
    leap_year(y)

main()
