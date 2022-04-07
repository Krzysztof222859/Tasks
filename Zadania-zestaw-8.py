#8

person = {
    "name" : "Marek",
    "surname" : "Banach",
    "age" : 25,
    "hobby" : ["swimming", "excursions"],
    "married" : True,
    "phone" : {"landline" : "123444321" , "mobile" : "777888999"}
    }

print(person)
print(person["name"])
print(person["hobby"])
person["surname"]="Nowak"
person["married"]= not person["married"]
person["gender"]="male"
person["hobby"].append("bicycle")
person["phone"]["workphone"]="123456789"

#9

smrtphone = {
    "name" : "iphone",
    "memory" : "64GB",
    "screensize" : "4,7",
    "color" : "black",
    "year" : "2020",
    "casecolor" : "black",
    }

for key in smartphone:
    print(key, "corresponds to:", smatrphone[key])
    
for key in smartphone.items()
    print(key, "=", value)
    
    
#10
    
#####
# Stack definition
##

stack = []

# add value at the end of the stack
def push(value):
    stack.append(value)
    
# remove the topmost element of the stack
#and return its value
def pop():
    if not empty():
        return stack.pop()
    else:
        return None
    
# return true if the stack is empty

def empty():
    return len(stack) == 0

# display stack
def display():
    for i in stack:
        print(i, end=" ")
    print()
    

#11
    
import stack

stack.display()
stack.push(2)
stack.push(14)
stack.push(9)
stack.display()
stack.pop()
stack.display()
stack.push(31)
stack.push(6)
stack.display()
stack.pop()
stack.popo()
stack.display()


#12 w domu


#13

import  json

with open("plikwjasonn.json") as file:
    data=json.load(file)
    
for k,v in data.items():
    print(k,":",v)


#14
    
import json

favourite = {
    "name":"Batman",
    "yeat":"2007",
    "type":"action",
    "actor":"Christian Bale",
    "character":"Batman",
    }

with open ("file.json","w") as file:
    json.dump(favourite, file)


#15

import json

student = {
    "name" : "Jan",
    "surname" : "Nowak",
    "age" : 20,
    "height":180,
    "weight":70,
    "hobby":["football","voleyball"],
    "phone" : {"landline" : "123444321" , "mobile" : "777888999"}
    }

with open("student.json","w") as file:
    json.dump(student, file)
    
#16
    
dictionary = {
    "a":"alfabet",
    "b":"bractwo",
    "c":"cement",
    "d":"dynia",
    "e":"eukaliptus",
    }

x=str(input("Podaj swoje litery: "))

for key in dictionary:
    print(f" Dla wartości {x} kod nasz kod ICAO jest nastepujący: {dictionary[x]}")
    
#to poprawnie
    
dictionary = {
    "a":"alfabet",
    "b":"bractwo",
    "c":"cement",
    "d":"dynia",
    "e":"eukaliptus",
    }

x=str(input("Podaj swoje litery: "))
s=''
for letter in x:
    s+=dictionary[letter]+' '
print(s.strip())    


#17
    
dictionary ={
    "a":"alfabet",
    "b":"bingo",
    "c":"cynamon",
    "d":"dynia",
    "e":"eukaliptus",
    }


with open ("dictionary.txt","w") as file:
    for i in dictionary:
        file.write(i+" "+dictionary[i]+"\n")
    
#to poprawnie
        
dictionary ={
    "a":"alfabet",
    "b":"bingo",
    "c":"cynamon",
    "d":"dynia",
    "e":"eukaliptus",
    }


with open ("dictionary.txt","w") as file:
    for i in dictionary:
        file.write(i+" "+dictionary[i]+"\n")
        
        




