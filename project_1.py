'''Mini project of python (K222MB-INT108) to perform simple calculation such as
add(+),subtact(-),multiplly(*),divide(/),pow(a,b),sine,cosine and tan as well as
modulus.'''
import math
def introduction():
    '''This projected was created on 15-nov-2022 by AphasarAnshari for mini project
    1st terminal of python project on the topic "simple calculator"'''
    print('\t\t\tSIMPLE CALCULATOR')
    print('\tHere you can perform[+,-,*,/,%,pow,sin,cos,tan]')
    print("\t\t 'exit' to break the loop")
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
def sum(a,b):
    '''To calculate the sum of two number'''
    a+=b
    return a
def sub(a,b):
    '''To calculate the subtract of two number'''
    a-=b
    return a
def mult(a,b):
    '''To calculate the multiply of two number'''
    a*=b
    return a
def div(a,b):
    '''To calculate the divide of two number'''
    a/=b
    return a
def mod(a,b):
    '''To calculate the mod of two number'''
    a%=b
    return a
def pow(a,b):
    '''To calculate the power of base with power'''
    a=math.pow(a,b)
    return a
def sin(a):
    '''To calculate the sine of a number'''
    a=math.radians(a)
    a=math.sin(a)
    return a
def cos(a):
    '''To calculate the cosine of a number'''
    a=math.radians(a)
    a=math.cos(a)
    return a
def tan(a):
    '''To calculate the tan of a number'''
    a=math.radians(a)
    a=math.tan(a)
    return a
introduction()
try:
    while(1):
        a=input("Enter 1st value: ",)
        if a=='exit':
            break
        a=int(a)
        o=input("enter operator for calculation: ")
        if o=='exit':
            break
        else:
            if o=='+':
                b=int(input('Enter 2nd number: '))
                s=sum(a,b)
                print('Sum =',s)
            elif o=='-':
                b=int(input('Enter end number: '))
                s=sub(a,b)
                print('Subtraction:',s)
            elif o=='*':
                b=int(input('Enter end number: '))
                s=mult(a,b)
                print('Multiplication:',s)
            elif o=='/':
                b=int(input('Enter end number: '))
                s=div(a,b)
                print('Division:',s)
            elif o=='%':
                b=int(input('Enter end number: '))
                s=mod(a,b)
                print('Modulus:',s)
            elif o=='^':
                b=int(input('Enter 2nd number: '))
                s=pow(a,b)
                print(f'{a} power {b} :',s)
            elif o=='sin':
                s=sin(a)
                print(f'sin({a}):',s)
            elif o=='cos':
                s=cos(a)
                print(f'cos({a}):',s)
            elif o=='tan':
                s=tan(a)
                print(f'tan({a}):',s)
except:
    print("something went wrong")