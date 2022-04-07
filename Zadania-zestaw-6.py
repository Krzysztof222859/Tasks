# tablice i listy

#6

tab=[15,8,31,47,2,19]
sum=0
for x in tab:
    sum=sum+x

print(sum/len(tab))


#7

tablica=[15,8,31,47,2,19]
e=0
o=0
for i in tablica:
    if i%2==0:
        e+=1
    else:
        o+=1
        
print(f"Liczba elementów: {e} + {o}")


#8

tablica=[-15,8,-31,47,-2,19]
min=tablica[0]
max=tablica[0]
for i in tablica:
    if i>max:
        max=i
    if i<min:
        min=i
print(f"Max: {max}, Min: {min}")


#9

def month(n):
    month=["January","February","March","April","May","June","July","August","September","October","November","December"]
    
    return months[n-1]
print

#10


def compare(array1, array2):
    if len(array1)==len(array2):
        for x in range(len(array1)-1)
            if array1[x] != array2[x]:
                return False
            return True
        
print(f"""a) ["water","book","sky"],["water","book","sky"]: {compare(["water","book","sky"],["water","book","sky"])}
a) [True, False], [True,False,True]:{compare([True,False],[True,False,True])}
b)[5,3,1...""")
        
        



#9

def month(n):
    month=["January","February","March","April","May","June","July","August","September","October","November","December"]
    
    return months[n-1]
print
#9

#10

array=[4,3,7,1,3]

def sum(array):
    sum=0
    for i in array:
        sum=sum+int(i)
    return sum
        
print(sum(array))

def array2str(array)
    result="Array:"
    for x in array2str:
        result+=" " +str(x)
    return result

Numbers=[4,3,7,1,3]

printt(f"""Array: {array2str(Numbers)}
Sum of values: {sum(Numbers)}""")

def compare(array1, array2):
    if len(array1)==len(array2):
        for x in range(len(array1)-1)
            if array1[x] != array2[x]:
                return False
            return True
        
print(f"""a) ["water","book","sky"],["water","book","sky"]: {compare(["water","book","sky"],["water","book","sky"])}
a) [True, False], [True,False,True]:{compare([True,False],[True,False,True])}
b)[5,3,1..."""
        
        
        
)        





#12

arraj=[15,8,31,47,2,19]

for x in reversed(arraj):
    print(x, end=" ")
    
    
#13

arrey=[8,2,5,1,9]

for x in arrey:
    print(x*x, end=" ")


#14
    
array=["Genowefa","Onufy","Celestyna","Alojzy","Pankracy"]



name=""
for n in array:
    if n.length()>name.length():
        name=n
print(name)            

#15

array=["blue","red","yellow","green"]

for x in array
    print(str(x) +"\n")
    
#pominiete    
    
    
#16
    
array=[12,6,4,9,3]

star(n)
    return n*"*"
print(star(12))


#17

a1,a2 =[4,36,12,28,9,44,5] , [5,1,36]

for i in a1:
    if i not in a2:
        print(i)

#18
  
#pomijamy
        
        
  
#19
        
array=[2,3,2,5,8,1,9,8]
unique_list=[]

for i in array:
    if i not in unique_list:
        unique_list.append(i)
for i in unique_list:
        print(i)
        
#

array=[2,3,2,5,8,1,9,8]
unique_list=[]

for i in array:
    if array.count(i)==1:
        unique_list.append(i)
print(unique_list)
        
        
#20
 
array=[15, 38, 7, 23, 14]

def occurs(number, array):
    if number in array:
        return true
    
print(occurs(5))

#

array=[15, 38, 7, 23, 14]

def occurs(number, array):
    
    number=int(input("Podaj liczbe: "))   
    if number in array:
            return True
    
print(occurs(input,array))

#21


array=[5,1,9,6,1]

x=max(array)
array=array-x

y=max(array)

#

array=[5,1,9,6,1]

array.sort()

print(array[-2])


#22

array=[5,1,9,6,1]

result=max(array)-min(array)
print(result)

#23

array=[1,0,9,4]
array.sort()
if len(array)%2!=0:
    print(array[len(array)//2])
else:
    print((array[len(array)//2]+array[len(array)//2-1])/2)

#24

array=[5,1,9,6,1]

x=int(input("Podaj liczbę: "))

suma=0
for i in array:
    if i>x:
        suma=suma+1
        
print(suma)


#25

array=[4,2,8,4,7,9,5]

def minmax(array):
    return [max(array), min(array)] 
    

print(minmax(array))


#26

array=[4,2,8,4,7,9,5]


for i in array:
    print(i, end=" ")

for i in array:
    if i%2==0:
        print(i, end=" ")
        
for i in array:
    if i%2==1:
        print(i, end=" ")
        
        
#27
        
array=[5,4,3,2,6,5]

number=''
for number in array:
    print(str(number), end=' ')
    
    
#28
    
from random import randint
array=[]
for j in range(6):
    array.append(randint(1,999))
l=len(array)
print("-----"*l+"-")
for i in array:
    print("|"+str(i).rjust(4), end='')
print("|")
print("-----"*l+"-")


#29

a1=[5,4,3,2,6,5]
a2=[5,4,3,2,6,5]
count=0
for i in a1:
    if i in a2:
        count+=1
    if count==len(a2):
        print("a1 is subset of a2")
    else:
        print("a1 is not subset of a2")
        
        
#30

import random
array=[5,4,3,2,6,5]

def rand_elem(array):
    for i in range(5):
        print(random.choice(array))

(rand_elem(array))

    
        
        