#5

def display_university_address():
    print("Cracow University of Economics")
    print("Rakowicka 27")
    print("31-510 Kraków, POLAND")
    
display_university_address()    


#6

def numbers_in_layout():
    for x in range (0,9,3):
        for y in range (1,4):
            print(f' {x+y}', end='')
        print()
    
numbers_in_layout()   


#7

def multiplication (x,y):
    print(f"{x} * {y} = {x*y}")
multiplication (5,8)


#8

def display_numbers(N):
    for x in range(1,N+1):
        print(x)
display_numbers(15)        
    

#9

def multiplication(x,y):
    return x*y

print(f"15*12 is a {multiplication(15,12)}")


#10

def read_number()
    x=int(input("Podaj dowolna liczbe:"))
    return x

x=read_number()
y=read_number()
suma=x+y
print(f"{x} + {y} = {suma}")


#11

def factorial(n):
    
    # 0! = 1, 1! = 1
    if n==1 or n ==1:
        return 1
    
    # n! = n * (n-1)!
    if n > 1:
        return n * factorial(n-1)
    
x=10
print(f" {x} = {factorial(x)}")
    
    
#12
    
def sum(n):
    
    if n<= 1:
        return n
    else:
        return n + sum(n-1)
    
x=10
print("f Sum of this numbers from 1 to {x} is {sum(x)}")         
    

#moduły...


#16

def month(n):
    if   n==1:
        return "January"
    elif n==2:
        return "February"
    elif n==3:
        return "March"
    elif n==4:
        return "April"
    elif n==5:
        return "May"
    elif n==6:
        return "June"
    elif n==7:
        return "July"
    elif n==8:
        return "August"
    elif n==9:
        return "September"
    elif n==10:
        return "October"
    elif n==11:
        return "November"
    elif n==12:
        return "December"
    
x=7
print(f" For number {x} of month we call its {month(x)}")


#pedro

m=["January", "February", "March", "April", "May" , "June" , "July", "August", "September", "October", "November", "December"]
def month(n):
    print(m[n-1])
month(7)



#17

def letterFrequency(letter):

    count = 0
  
    for char in text:
  
        if char == letter:
            count += 1

    return count
  
  
x = "e" 
print("The letter {x} in this text appears {count} times.")


#podjescie 2

def counting_letters():

    napis=str("You never get a second chance to make a first impression")
    print(napis)
    liczba=0
    for char in napis:
        if char=="e":
            liczba+=1

    print(liczba)

counting_letters()


#18

def getsum(n):
 
    sum=0
    while (n!=0):
         
        sum=sum+int(n%10)
        n=int(n/10)
         
    return sum

n=7182
print(getsum(n))


#19

def checking(x):
    if x>=5 and x<=9:
        print("True")
    else:
        print("False")
        
checking(7)       

#20

def power(x,n):
    
    if n==0:
        return 1
    elif x==0:
        return 0
    else:
        return x**n

a=5
b=3
print(f" {a} to the {b} power is {power(a,b)}")


#21

def function(a,b):
    if (a>b):
        print("true")
    elif (a<b):
        print("false")
   
   
#inaczej


def function(a,b):
    if (a>b):
        return "true"
    elif (a<b):
        return "false"
   
   
x=2
y=3

print(f"We have the {x} and {y} and we say true when a is more, flase if b is more {function(x,y)}")


#22

def function(a):
    if a%2 ==0:
        return "true"
    else:
        return "false"
    
print(function(17))   


#

greater = lambda x: x%2==0

print(greater(4))
    
    
    