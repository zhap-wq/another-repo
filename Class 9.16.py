#in function, python is extremely picky with indentation, so please make you indentation right
#space and tab are not the same for the interpreter, please use tab
#please make your all tab space align to each others. 
def func():
    print("this is a function.")

#function with two input, the input order matter when you call the function 
def hihi(baby,mom):
    print(baby)
    print(mom+"!")

#function with defult input
def zhao(p="hellow"):
    print(p)
    
#function has input 
def greeting(name):
    print("hello",name)

def main():
    func()
    zhao()
    print("hihi",end="")
    print("zhao")
    n=input("what is your name?")
    greeting(5)
    hihi("kisskiss","loveyou")
#this says print hihi and end with nothing, the default is to end and returns to the next line

#scope of varable, the function only now variable defined inside itself 

main()



