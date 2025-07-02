#creating function  function is defined using the def keyword
#function is a block of code which only run when it is called.
# arguments information can be passed into functions as ardguments
#only function definition  in python
# creating function
#def myfunc(a,b):
   # print("hello world")

    
   # print(a+b)
#myfunc(10,12)
#def comp_prog(lang):
    #print(lang+"programming")
#comp_prog("java ")
#comp_prog("c++ ")
#def add(num1,num2):
    #return num1+num2
#print(add(2,5))
num1=int(input("enter num1 "))
num2=int(input("enter num2 "))

def kabsh(x,y):
    print(x-y)
    print(x*y)
    print(x/y)
    return x-y
assert kabsh(num1,num2) == 8# assert deals with the retun and if the value we returned is false then it tells us t there is an error

    