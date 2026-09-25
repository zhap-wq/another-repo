#Pu Zhao's program 
def general_admission(n):
    if n<3:
        print("Your whale watch ticket will be free.")
    elif n<=11:
        print("Your whale watch ticket will be $45.")
    elif n<60:
        print("Your whale watch ticket will be $65.")
    else:
        print("Your whale watch ticket will be $57.")

def member_admission(n):
    if n<3:
        print("Your whale watch ticket will be free.")
    elif n<=11:
        print("Your whale watch ticket will be $37.80.")
    elif n<60:
        print("Your whale watch ticket will be $54.60.")
    else:
        print("Your whale watch ticket will be $47.88.")

def main():
    m=input("Are you an aquarium mumber (y or n)?")
    if m=="y":
        year_1=int(input("What is your age?"))
        member_admission(year_1)
    else:
        year_2=int(input("What is your age?"))
        general_admission(year_2)
main()
