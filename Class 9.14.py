#import two things altogether, math for special math value and operations 
import random, math
print(math.pi)

#Three ways to out put two value together 
area=math.pi
print("Hello",area)
print("Hello "+str(area))
print(f'Volume is {area:.2f}')

#functions perform task, indicated by ()
#e.g. input(), type(), random.randint(a,b), round(), int(), float(), str(), print()
#several dozen build into python
#you can build your own function
#use def folloed by name and (), and colon 
#def hi():
#we need colon and indentation


#blocknes need colon and indentation

#here is an example for function

def greetings():
    print("hello my darling.")
    print("good morning.")

greetings()

#main is not automatically shown, we always have def main(): and run main task in it.
#you defined peripheral functions outside of main

#functions with parameters 
def verse(animal, sound):
    print("My name is ", animal)
    print("My faviorate sound is", sound)

verse("love","wangwang")
