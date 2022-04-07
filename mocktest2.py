#1


tablica=[1,2,3,4,5,6,7,8,9,0,11,12,13,14,15,16,17,18,19,20]
def f1(tablica):
    suma=0
    for i in tablica:
        if i >8 and i%2==0:
            suma=suma+1
    return suma
print(f1(tablica))


#2

import re
a1=[23,7,16,34]
a2=[1,18,79,20,6,111]
def f2(a1,a2):
    x=re.findall("d/{2}",a1)
    y=re.findall("d/{2}",a2)
    if len(x)==len(y):
        return True
    else:
        return False
print(f2(a1,a2))


import re
a1=[23,7,16,34]
a2=[1,18,79,20,6,111]
def f2(a1,a2):
    x=0
    y=0
    for i in a1:
        if i>9 and i<100:
            x+=1
    for i in a2:
        if i>9 and i<100:
            y+=1
    if x==y:
        return True
    else:
        return False
print(f2(a1,a2))


#3

import re
t="Przykładowe liczby parzyste to 16, 2, 114oraz 1014, a także 8"
def f3(t):
    liczby=re.findall("^/d{2}$|^/d{3}$",t)
    suma=0
    for i in liczby:
        suma=suma+int(i)
    return suma
print(f3(t))

import re
t="Przykładowe liczby parzyste to 16, 2, 114oraz 1014, a także 8"
def f3(t):
    liczby=re.findall("hmmmmmm",t)
    suma=0
    for i in liczby:
        suma=suma+int(i)
    return suma
print(f3(t))


import re
t="Przykładowe liczby parzyste to 16, 2, 114 oraz 1014, a także 8"
def f3(t):
    liczby=re.findall(r'\b\d{2}\b|\b\d{3}\b',t)
    suma=0
    for i in liczby:
        suma=suma+int(i)
    return suma
print(f3(t))


#4

"arr1":[2,6,5]
"arr2":[7,1]
"arr3":[2,9,8,1]

d={"arr1":[2,6,5],"arr2":[7,1],"arr3":[2,9,8,1]}
def f4(d):
    suma=0
    for key in d:
        for value in d[key]:
            if value>=5 and value<=10:
                suma+=value
    print(suma)
f4(d)

        
        
#5
        
def f5():
    import re
    with open("poem.txt","r") as file:
        file_read=file.read()
        wiersze=re.findall("[C,c]",file_read)
        suma=0
        for i in wiersze:
            suma+=1
        return suma
print(f5())


def f5(c):
    with open("poem.txt","r") as file:
        text=file.readlines()
        wiersze=0
        for line in text:
            i=0
            for letter in line:
                if letter.lower()==c: i+=1
            if i!=0: wiersze+=1
        return wiersze
print(f5("m"))
    
  
def f5(c):
    with open("poem.txt","r") as file: 
        text=file.readlines()
        wiersze=0
        for line in text:
            if c in line.lower():
                wiersze+=1
        return wiersze
print(f5("m"))
  
  
  
#6

import csv

def f6(g,n1,n2):
    number=0
    with open("people.csv", newline="\n") as csvfile:
        data = csv.reader(csvfile, delimiter = ",")
        for row in data:
            if row[-2].isdigit() and row[-1] ==g and int(row[-2])>=n1 and int(row[-2]) <= n2:
                number +=1
    csvfile.close()
    return number
print(f6("Female",160,180))




 