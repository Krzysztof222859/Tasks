#5

class pieces_of_music():
    
    def __init__(self, artist, track_title, album, year):
        self.artist=artist
        self.track_title=track_title
        self.album=album
        self.year=year
        
    def __str__(self):
        return "Performer: " + self.artist + "\n" + "Song: " + self.artist + "\n" + "Album: " + self.album + "\n" + "Year: " + self.year
        return "Song: " + self.track_title
        return "Album: " + self.album
        return "Year: " + self.year
    
    
pom=pieces_of_music("Ed Sheeran", "Hearts Don't Break Around Here", "Devide", "2017")
print(pom)


#7

class Message():
    def __init__(self):
        self.message=""
    
    def set_message(self, message):
        self.message=message.capitalize()+"BYE."
        
    def show_message(self):
        print(self.message)
        
class SMS(Message):
    def __init__(self, sender, recipient):
        super().__init__()
        self.sender=sender
        self.recipient=recipient
        
    def send_sms(self):
        print("Sending SMS...", "\n", "From: ", self.sender, "\n", "To: ", self.recipient, "\n", self.message) 
        print(f"Sending SMS...\nFrom: {self.sender}\nTo: {self.recipient}\n {self.message}")
        
        
class eMail(Message):
    def __init__(self, senders_adress, recipients_adress, subject):
        self.senders_adress=senders_adress
        self.recipients_adress=recipients_adress
        self.subject=subject
        super().__init__()
        
    def send_email(self):
        print(f"Sending email...\nFrom: {self.senders_adress}\nTo: {self.recipients_adress}\nSubject: {self.subject}\n {self.message}")


message=Message()
message.set_message("wlazl kotek na plotek i sobie tam siedzi")
message.show_message()
sms=SMS("Darek","Jarek")
sms.send_sms()
email=eMail("darek@wp.pl","jarek@wp.pl","mejl")
email.send_email()
        
        
#8

class cell_phones():
    
    def __init__(self, name, year, color):
        self.name=name
        self.year=year
        self.color=color
    
    def unlock_phone(self):
        print(f"Phone: {self.name} is unlocked")
        
    def lock_phone(self):
        print(f"Phone: {self.name} is locked")
        
    def __str__(self):
        return "Your phone name is: " + self.name + "\n" + "Color of phone is: " + self.color + "\n" + "It's year of production is: " + self.year
    
motorola=cell_phones("SuperMotorola","2007","white")
print(motorola)
motorola.unlock_phone()
motorola.lock_phone()
szamsung=cell_phones("Galaxy S8", "2015", "blue")
print(szamsung)
szamsung.unlock_phone()
szamsung.lock_phone()
print(szamsung)
        
        
#9

class book():
    
    def __init__(self):
        self.name="Opowieści z Narnii"
        self.year="2002"
        self.author="XY"
        
class paper_book(book):
    
    def __init__(self):
        super().__init__()
        self.number_of_sites="400"
        
    def __str__(self):
        return "Name: " + self.name + "\n" + "Year: " + self.year + "\n"  + "Author: " + self.author + "\n" + "No of sites: " + self.number_of_sites 
        
class e_book(book):
    
    def __init__(self):
        super().__init__()
        self.where_saved="Disc-C"
         
    def __str__(self):
        return "Name: " + self.name + "\n" + "Year: " + self.year + "\n"  + "Author: " + self.author + "\n" + "Where saved: " + self.where_saved
        
        
paper=paper_book()
print(paper)
electronic=e_book()
print(electronic)


#10

# class definition
class Film():
    # class variables

    cinema = "Multikino"
    def __init__(self, title):
        self.title = title


    def __str__(self):
        return f"{self.title} ({Film.cinema})"
    

# program
film1 = Film("The Shawshank Redemption")
print(film1)
film2 = Film("Pulp Fiction")
print(film2)

# renaming the cinema (changing the value
# of a class variable)
Film.cinema = "Cinema City "
print(film1)
print(film2)


#11

class studenci():
    
    ID=1000
    
    
    def __init__(self,name, surname, kierunek, uczelnia):
        self.name=name
        self.surname=surname
        self.kierunek=kierunek
        self.uczelnia=uczelnia
        
        
    
    
    
    def __str__(self):
        return "Imie: " + self.name + "\n" + "Nazwisko: " + self.surname + "\n" + "Kierunek: " + self.kierunek + "\n" + "Uczelnia: " + self.uczelnia + "\n" + "ID studenta: " + str(studenci.ID)
        studenci.ID+=1
    
stud1=studenci("Bartek","Admamowicz","Informatyka","UEK")
print(stud1)
studenci.ID+=1
stud2=studenci("Dariusz","Dudek","Ekonomia","UEK")
print(stud2)
studenci.ID+=1
stud3=studenci("Adam","Kowalski","Finanse","UEK")
print(stud3)
        
        
#12

class Arrays():

    @staticmethod
    def print_in_col(array):
        for c in array:
            print(c)
            
    @staticmethod
    def print_in_row(array):
        for c in array:
            print(c, end=", ")
        
            
my_array=[4,1,8,7,2]
Arrays.print_in_col(my_array)
Arrays.print_in_row(my_array)


#no nie wiem jak zz tym stripem...


#13

import random

class Arrays():

    @staticmethod
    def print_in_col(array):
        for c in array:
            print(c)
            
    @staticmethod
    def print_in_row(array):
        for c in array:
            print(c, end=", ") 
        
    @staticmethod
    def creating_arrayc(number,value):
        arrayc=[]
        for c in range(number):
            arrayc.append(value)
        return arrayc
    
    @staticmethod
    def creating_arrayd(number,m,n):
        arrayd=[]
        for c in range(number):
            arrayd.append(round(random.uniform(m,n)))
        
    @staticmethod
    def choosing_numbers(array,x,y):
        sum=0
        for c in array:
            if c > x and c < y:
                sum+=1
        return sum
    
    
my_array=[4,1,8,7,2]
Arrays.print_in_col(my_array)
Arrays.print_in_row(my_array)
print("\n")
print(Arrays.creating_arrayc(5,2))
print(Arrays.creating_arrayd(3,1,5))
print(Arrays.choosing_numbers(my_array,2,5))


#14

import math

class Area():
    
    @staticmethod
    def area_of_triangle(a,h):
        return (1/2*a)*h
    
    @staticmethod
    def area_of_rectangle(a,b):
        return a*b
    
    @staticmethod
    def area_of_circle(r):
        return math.pi*(r**2)
    
print(Area.area_of_triangle(3,4))
print(Area.area_of_rectangle(7,6))
print(Area.area_of_circle(2))


#15

class Point():
    
    def __init__(self,x,y):
        self.x = x
        self.y = y
        
    def __str__(self):
        return f'P({self.x},{self.y})'
    
    def __eq__(self, other):
        return self.x== other.x and self.y== other.y
    
    def distance(self, other):
        ogorek=(self.x-other.x)**2
        pietroszka=(self.y-other.y)**2
        return(ogorek+pietroszka)**0.5


p1=Point(5,4)
p2=Point(3,2)
print(p1)
print(p2)
print(p1==p2)

if p1==p2:
    print("Distance: 0")
    
else:
    print(p1.distance(p2))
    