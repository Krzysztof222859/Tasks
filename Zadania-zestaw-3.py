#6

x=int(input("Podaj wartość twojej prędkości:"))
if x>130:
    print("Jedziesz za szybko")
else:
    print("Masz dobrą prędkość")
          

speed_limit = 130
car_speed=int(input("Podaj wartość twojej prędkości:"))
if car_speed > speed_limit:
    print("Jedziesz za szybko")
else:
    print("Masz dobra predkość")


#7
    
x=int(input("Podaj dowolną liczbe całkowita:"))
if x %2 == 0:
    print(f"Liczba {x} jest liczbą parzystą")
else:
    print(f"Liczba {x} jest liczbą nieparzystą")


#8
    
Paul_age=21
Annie_age=18
adult_age=18
if Annie_age >= adult_age  and  Paul_age>=adult_age:
    print("Annie and Paul are adult")
else:
    print("Nie są to osoby dorosłe")
    

#9
    
x=int(input("Podaj liczbę całkowitą"))
y=int(input("Podaj liczbę całkowitą"))
if x>0 or y>0:
    print("Przynajmniej jedna liczba jest dodatnia")
else:
    print("Liczby nie są dodatnie")
    
  
#10
    
for sentence in range (1,6,1):
    print("Practice makes perfect")
    
    
#11
    
for x in range(1,21):
    print (x)
    
 
#12

suma=0
for i in range(100,151):
    suma=suma+i
print(f"Suma liczb z przedziału od 100 do 150 wynosi: {suma}")    
    

#13

licznik =1

for mianownik in range(1,11):
    print(licznik/mianownik)
    
#to samo tylko petla while
    
x=1

while x<=10:
    print(1/x)
    x=x+1
    
    
#suma liczb nie wiadomo ile podajemy -> while, do momentu az poda 0    
    
    
#16
    
x=int(input("Podaj pierwsza liczbe calkowita:"))
y=int(input("Podaj druga liczbe calkowita:"))
if x>y:
    print(f"{x}, {y}")
else:
    print(f"{y}, {x}")
      
      
#17
    
x=int(input("Podaj pierwsza wspolrzedna:"))
y=int(input("Podaj druga wspolrzedna:"))    
if x==0 and y==0:
    print("Jest to punkt 0,0")
elif x>0 and y>0:
    print("Jest to pierwsza cwiartka ukladu wspolrzednych")
elif x>0 and y<0:
    print("Jest to druga cwiartka ukladu wspolrzednych")
elif x<0 and y<0:
    print("Jest to trzecia cwiartka ukladu wspolrzednych")
elif x<0 and y>0:
    print("Jest to czwarta cwiartka ukladu wspolrzednych")
else:
    print("Zle wartosci")
    
    
#18
    
p=0
d=0
j=0
x=int(input("Podaj liczbe pieniedzy w PLN"))
y=x
while x-5>=0:
    x-=5
    p+=1
while x-2>=0:
    x-=2
    d+=1
while x-1>=0:
    x-=1
    j+=1
print("Wartośc i liczba pieniadzow przedstawione ponizej")
print("5 zl -" ,p)
print("2 zl -" ,d)
print("1 zl -" ,j)
      

#19

x=int(input("Podaj wiek swojego psa:"))
if x<=2:
    print(f"Wiek twojego psa w przeliczeniu to: {x*10.5}")
else:
    print(f"Wiek twojego psa w przeliczeniu to: {(2*10.5)+((x-2)*4)}")
       
#20
    
x=int(input("Podaj liczbę całkowita: "))
for y in range (1,11):
    print(f"{x} x {y} = {x*y}")
    
    
#21
    
university="UEK w Krakowie"
print(university)
for x in university
    print(x, " ", end=" ")
    
    

#22
    
for number in range(1,31):
    if  number %3==0 and number %5==0:
        print(f"{number} BINGO")
    elif number %5==0:
        print(f"{number} FIVE")
    elif number %3==0:
        print(f"{number} THREE")
    else:
        print(number)
        
        
#23
        
for x in range (1,10):
    print(str(x)*x) 
        
        
        
#24
        
for x in range (1,6):
    print("*"*x)
for y in range (4,0,-1):
        print(y*"*")
        

#25
        
b=int(input("wysokosc"))
for i in range(a):
    print("*", end="")
print("")
for j in range(b-2):
    print("*"+""*(2*a-3)+"*")
for k in range(a):
    print("*", end="")


#26

'''

kod=(1,2,3,4)
x=int(input("Podaj pierwsza cyfre kodu:"))
y=int(input("Podaj druga cyfre kodu:"))
z=int(input("Podaj trzecia cyfre kodu:"))
c=int(input("Podaj czwarta cyfre kodu:"))
if kod==(x,y,z,c):
    print("Podano prawidlowy kod")
elif kod!=(x,y,z,c):
    print("Podano niepoprawny kod, wpisz jeszcze raz. Druga proba")
elif kod!=(x,y,z,c):
    print("Podano niepoprawny kod, wpisz jeszcze raz. Trzecia proba")
elif kod!=(x,y,z,c):
    print("Podano niepoprawny kod po raz trzeci, karta zostaje zablokowana")  '''


x="1234"
z=0
for i in range (3):
    y=input('Enter the PIN code:')
    if y!=x:
        print("Incorrect...")
        z+=1
    else:
        print("Podano dobry kod")
        break
if z==3:
    print("Podano niepoprawny kod po raz trzeci, karta zostaje zablokowana")

#27

for i in range(6,-1,-3):
    for j in range(1,4):
        print(f' {i+j}',end='')
    print()
    
while...    

#28

x=0
y=1
print(x, end=",")
for i in range (50):
    print(y, end=",")
    y=y+x
    x=y-x

#29
    
for i in range()
    print("Podaj liczbę:")

#31
    
from random import*
for i in range(20):
    print(randint(5,10), " " ,end="")

 
#32

from random import*
for i in range (1,8):
    for j in range(6):
        print(randint(1,49), " ", end="")
    print() 