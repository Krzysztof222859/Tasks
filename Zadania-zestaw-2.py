#10

 name="Krzysztof "
 surname="Zietek"
 name+surname
 
#11

c=int(input("Podaj pierwsza liczbe:"))
d=int(input("Podaj druga liczbe:"))
s=c+d
print(f"Suma to: {s}")

#12

print("My name is", name, "I'm", age, "years old, and my height is ",  height, "cm.")
print(f"My name is {name}, I'm {age} years old, and my height is {height}cm")

#13

print(f"The value is {l}, and its second power is {p}")

print("The value is {}, and its second power is {}".format("7","49"))

print("The value is {}, and its second power is {}".format(l,p))

#14

radius=7
pi=3.14
area=(pi*(radius**2))
circumference=(2*pi*radius)
print(f"Pole tego okregu wynosi: {area} a jego obwod wynosi: {circumference}.")

#15

c=int(input("Podaj pierwsza wartośc temperatury w stopniach Celciusa:"))
f=c+273
print(f"Wartośc temp w celciuszach to {c}, a w fereiheitach to {f}.")

#18

w=int(input("Podaj swoj wzrost w cm: "))
s=w*0.032808
c=w*0.039370
print(f"Mam {w} cm wzrostu a to jest {s} stóp oraz {c} cali.")

#19

a=int(input("Podaj wartośc a: "))
b=int(input("Podaj wartośc b: "))
c=int(input("Podaj wartość c: "))
o=((a+b+c)/2)
P=(o*(o-a)*(o-b)*(o-c))**0.5
print(f"Wartośc pola trojkata wynosi {P}") 

#20

m=float(input("Podaj swoja wage (kg): "))
w=float(input("Podaj swój wzrost (m): "))
B=m/(w**2)
print(f"Wartośc Twojego BMI wynosi {B}")

#21

import random
x=(random.randint(1, 6))
y=(random.randint(1, 6))
z=(random.randint(1, 6))
s=x+y+z
print(f"Kolejne liczby wynoszą: x={x}, y={y}, z={z}, a suma tych trzech wartości to: {s}")

#22

import random
x = int(input("Wybierz liczbe od 1 do 6: "))
y = (random.randint(1, 6))

if (x==y):
    print("True")
else:
    print("Sproboj jeszcze raz:")

####################

import random
x = int(input("Wybierz liczbe od 1 do 6: "))
y = (random.randint(1, 6))

while (x!=y):
    x = int(input("Wybierz liczbe inna: "))

print("True")


#23

k=float(input("Podaj kwote zakupu: "))
v=0.23*k
print(f"Wartość watu z podanej kwoty (23%) to: {v} ")
