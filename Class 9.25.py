#reviewing: slides, class code example, homework, labs
#print end with no new line 
def main ():
    name=input("What is your name")
    print("Hello ", end="")
    print(name)
#return statement needs varable to hold
    a= hi()
    print(a)
#or print it directly
    print(hi())


    
#never forget to cast the input if you want a number but default input is a string

#exam is about first 3 topics, returning is no included
#scope problem so you need to pass information out: which is return value
#return
#you can return a chain function 

def hi():
    n=5
    return n

main()
