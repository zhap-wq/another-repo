def eligibility(age, res):
    if age>=35:
        if res>=14:
            print("You can run for representative, senator, or president")
        elif res<14 and res>=9:
            print("You can run for representative or senator")
        elif res<9 and res>=7:
            print("You can run for representative")
        else:
            print("You can run no political office yet")

    elif age>=30 and age<35:
        if res>=14:
            print("You can run for representative or senator")
        elif res<14 and res>=9:
            print("You can run for representative or senator")
        elif res<9 and res>=7:
            print("You can run for representative")
        else:
            print("You can run no political office yet")

    elif age>=25 and age<30:
        if res>=14:
            print("You can run for representative")
        elif res<14 and res>=9:
            print("You can run for representative")
        elif res<9 and res>=7:
            print("You can run for representative")
        else:
            print("You can run no political office yet")

    else:
        print("You can run no political office yet")

def main():
    a=int(input("Age: "))
    r=int(input("Years lived in U.S.: "))
    eligibility(a,r)

main()
