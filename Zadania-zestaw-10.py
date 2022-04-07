#7

class University():

    #object constructor (__init__ method)


    def __init__(self, name, fullname):
        # object states/attributes (fields)
        self.name = name
        self.fullname= fullname
        
        
        # object bahaviors (methods)
    def print_name(self):
        print(self.name)
        
    def set_name(self, newname):
        self.name=newname
        
        
#9

    def print_fullname(self):
        print(self.fullname)
    
    def set_fullname(self, name):
        self.fullname=name
    
uni=University("UJ","Uniwersytet Jagiellonski")
uni.print_name()
uni.print_fullname()
uni.set_name("UEK")
uni.set_fullname("Uniwerystet Ekonomiczny")
uni.print_name()
uni.print_fullname()

#10

class TV():
    def __init__(self):
        self.is_on=False        
        self.channel_no=1
        self.channels=[]
    
        
    def turn_on(self):
        self.is_on=True
        
    def turn_off(self):
        self.is_on=False
    
    def show_status(self):
        if self.is_on==True:
            print(f"TV is on channel {self.channels}")
        else:
            print("TV is off")
        
    def change_status(self):
        if self.is_on==True:
            self.is_on=False
        elif self.is_on==False:
            self.is_on=True
            
    def change_status_quick(self):
        self.is_on=not self.is_on
    
    def set_channel(self, new_channel_no):
        self.channel_no=new_channel_no
    
    def set_channels(self, channels_list):
        self.channels=channels_list
        
    def show_channels(self):
        print(self.channels)
            




tv=TV()
tv.show_status()
tv.turn_on()
tv.show_status()
tv.turn_off()
tv.show_status()
tv.change_status()
tv.show_status()
tv.change_status()
tv.show_status()
tv.change_status_quick()
tv.show_status()


tv.show_status()
tv.turn_on()
tv.show_status()
tv.set_channel(5)
tv.show_status()
tv.turn_off()
tv.show_status()
tv.set_channels(["TVP1","TVP2","TVN","Polsat","Filmbox","Discovery"])
tv.show_channels()


#14

class TV():
    def __init__(self):
        self.is_on=False        
        self.channel_no=1
        self.channels=[]
        self.volumme=0
    
        
    def turn_on(self):
        self.is_on=True
        
    def turn_off(self):
        self.is_on=False
    
    def show_status(self):
        if self.is_on==True:
            i=self.channel_no
            print(f"TV is on channel {self.channel_no}"+ " " + self.channels[i-1] + " " + f"volumme: {self.volumme}")
        else:
            print("TV is off")
        
    def change_status(self):
        if self.is_on==True:
            self.is_on=False
        elif self.is_on==False:
            self.is_on=True
            
    def change_status_quick(self):
        self.is_on=not self.is_on
    
    def set_channel(self, new_channel_no):
        self.channel_no=new_channel_no
    
    def set_channels(self, channels_list):
        self.channels=channels_list
        
    def show_channels(self):
        print(self.channels)
        
    def set_volumme(self, new_volumme):
        self.volumme=new_volumme
        
    def increase_volumme(self):
        if self.volumme<=10:
            self.volumme+=1
        
    def decrease_volumme(self):
        if self.volumme>=0:
            self.volumme-=1
            

tv=TV()

tv.set_channels(["TVP1","TVP2","TVN","Polsat","Filmbox","Discovery"])
tv.show_channels()
tv.turn_on()
tv.show_status()
tv.set_channel(5)
tv.show_status()
tv.increase_volumme()
tv.show_status()


#16

class Book():
    
    def __init__(self):
        self.title="Dziady"
        self.author="Adam Mickiewicz"
        self.number_of_pages=150
        self.page_no=1
        self.open=False
        
    def open_book(self):
        self.open=True
        
    def show_status(self):
        if self.open==True:
            print(f"This book's name is {self.title} and it's author is {self.author}. It has {self.number_of_pages} pages and now you're on page {self.page_no}.")
        elif self.open==False:
            print("Book is closed")
     
     
    def reading_pages(self):
        if self.open==True:
            self.page_no+=5
        else:
            print("Book is closed, you can't read man")
         
    def reading_pages2(self, new_no):
        self.page_no=new_no
        
    def close_book(self):
        self.open=False
         
        
book=Book()
book.open_book()
book.show_status()
book.reading_pages()
book.reading_pages()
book.show_status()
book.close_book()
book.show_status()
book.reading_pages()
book.show_status()


#17

from random import uniform

class thermometer():
    
    def __init__(self):
        self.turn_on=False
        self.temperature_value=36.6
        
    def turning_on(self):
        self.turn_on=True
        
    def turning_off(self):
        self.turn_on=False
        
    def measuring(self, measured_temperature):
        self.temperature_value=measured_temperature
        
    
        
    def show_status(self):
        print(f"Wartośc zmierzonej temperatury to: {round(self.temperature_value,1)}.")
        if self.turn_on==True and self.temperature_value >=37.0 and self.temperature_value <=41.0:
            print("Fever")
        elif self.turn_on==True and self.temperature_value >=37.0 and self.temperature_value >= 41.0:
            print("CRITICAL TEMPERATURE")
        elif self.turn_on==False:
            print("Thermometer is turned off")
         
theo=thermometer()
theo.turning_on()
theo.measuring(uniform(34,42,))
theo.show_status()
theo.turning_off()
theo.show_status()

        
#18

from random import randint


class Bank():
    
    def __init__(self):
        self.account_no=randint(00000000000000000000000000, 99999999999999999999999999)
        self.balance=0
        
        
    def show_balance(self):
        print(self.balance)
        
    def deposit_money(self, new_balance):
        self.balance=self.balance+new_balance
        
    def withdraw_money(self, new_balance):
        if self.balance < new_balance:
            print("You cant withorow money, you have not enough money")
        else:
            self.balance=self.balance-new_balance
        
    def show_status(self):
        print(f"You have {self.balance} PLN.")
        print(f"You have {self.account_no} number.")
        
        
bank=Bank()
bank.show_balance()
bank.deposit_money(1125)
bank.show_status()
bank.withdraw_money(745)
bank.show_status()
bank.withdraw_money(1000)
bank.show_status()


#19

rom statistics import median

class Statistics():
    
    def __init__(self):
        self.set_of_numbers=[]
        
        
    def show_numbers(self):
        for i in self.set_of_numbers:
            print(i, end=" ")
            
        
    def add_number(self):
        new_number=int(input("Podaj dowolna liczbe, ktora bedzie dodana do tablicy: "))
        self.set_of_numbers.append(new_number)
        
    def greatest_number(self):
        print("\nNajwieksza liczba to: ", max(self.set_of_numbers))
        
    def smallest_number(self):
        print("Najmniejsza liczba to: ", min(self.set_of_numbers))
        
    
    def aritmetic(self):
        suma=0
        for i in self.set_of_numbers:
            suma+=i
        print("Srednia arytmetyczna to: ", suma/len(self.set_of_numbers))
        
    def mediana(self):
        print("Mediana tych liczb to: ", median(self.set_of_numbers))
            
    def mediana_inna(self):
        self.set_of_numbers.sort()
        if len(self.set_of_numbers) %2!=0: 
            print(f"Mediana to: {self.set_of_numbers[int(len(self.set_of_numbers)/2)]}")
        else:
           medianaa= (self.set_of_numbers[int(len(self.set_of_numbers)/2)-1] + self.set_of_numbers[int(len(self.set_of_numbers)/2)])/2
           print(f"Mediana to: {medianaa}")

                                    
        
        
        
            
stats=Statistics()

stats.show_numbers()
stats.add_number()
stats.add_number()
stats.add_number()
stats.add_number()
stats.add_number()
stats.add_number()
stats.show_numbers()
stats.greatest_number()
stats.smallest_number()
stats.aritmetic()
stats.mediana()
stats.mediana_inna()


#20

from contact import Contact
from contact_list import Contact_list



cont1=Contact("John Brown", "brown@onet.pl", 555234000)
contact_list=Contact_list()
contact_list.add_new_contact(cont1)
cont2=Contact("Anna May", "am@o2.pl", 232000199)
contact_list.add_new_contact(cont2)
cont3=Contact("George Small", "smallg@google.pl", 222999100)
contact_list.add_new_contact(cont3)
contact_list.display_contact_list1()


class Contact():
    
    def __init__(self, name, email, telephone):
        self.name=name
        self.email=email
        self.telephone=telephone
       
    def __repr__(self):
        return self.name + " " + self.email + " " + str(self.telephone)
        

class Contact_list():
    
    def __init__(self):
        self.contact_list=[]
        
        
    def add_new_contact(self, new_contact):
        self.contact_list.append(new_contact)
    
    def display_contact_list(self):
        for contact in self.contact_list: 
            print(contact.name, contact.email, contact.telephone)
            
    def delete_contact(self):
        pass
    
    def display_contact_list1(self): 
        print(self.contact_list)



        
