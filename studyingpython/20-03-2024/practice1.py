'''
Age less than 5 = free
under 18 / student = 15
member = 20
public = 30
'''
import random

def calculate_ticket_price(category):
    # ' category ' refers to young, student, member, public (the ticket type)
    prices = {
        'young' : 0,
        'student' : 15,
        'member' : 20,
        'public' : 30,
    }
    chosen_category = prices.get(category)
    return chosen_category

def generate_random_seat_number():
    #generates random seat number between 1 to 100
    randomseatnumber = random.randint(1, 100)
    return randomseatnumber

def generate_event_ticket (name, category):
    #need to generate a new ticket each time 
    ticketprice = calculate_ticket_price(category)
    seatnumber = generate_random_seat_number()

    ticket_info = {
        "name" : name,
        "category" : category,
        "price" : ticketprice,
        "seat" : seatnumber
    }
    return ticket_info

def print_ticket(ticket_info):
    #need to print each ticket
    if ticket_info:
        for key, value in ticket_info.items():
            print(f"{key}: {value}")

    else: 
        print("No ticket information available.")  

#example usage
# ticket = generate_event_ticket("John Doe", "public")     
# print_ticket(ticket)               

#Call the functions        
name = input("Enter your name: ")
category = input("Input ticket category (young, student, member, public): ")  

ticket = generate_event_ticket(name, category)
print_ticket(ticket)