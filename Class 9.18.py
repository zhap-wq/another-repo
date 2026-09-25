#today's topic is branching 
#relational operators
#>,<,==,>=,<=,!= returns true for false
#= used for assignment: n=5; == used for comparison: if a==0
#Boollean expression: n=5 returns True or False
#one branch: if condition:
#Two branch: if condition: else:
#Multiple branching: if condition: elif condition: else:
#one if one else and whatever number of elif 
#each if is a seperate block

#need a tab to indent in if else or elif
#you can use pass as do nothing in a case
#logical operators: and, or(inclusive disjunction), not, see logic

def scho(month):
    if month== "Sep" or month=="Jan":
        print("School")
    else:
        print("vacation")

def greetings(gender):
    if gender=="n":
        pass
    elif gender=="m":
        print("hi gentlemen")
    elif gender=="f":
        print("hi my lady")
    else:
        print("hi my fella")
        
def main():
    number=float(input("pick a number that you like."))
    if number==0:
        print("neutral")
    elif number<0 :
        print("negative")
    else:
        print("positive")
    g=input("what is your gender:n,m,f,o")
    greetings(g)
    m= str(input("pick a month"))
    scho(m)

main()




    
    
