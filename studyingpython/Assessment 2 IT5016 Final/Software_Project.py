class TicketSystem:
    def __init__(self):
        self.tickets = {}
        self.ticket_counter = 2000 #ticket ID counter, so values begin from 2000 onward
        self.open_tickets_count = 0
        self.total_tickets_count = 0
        self.resolved_tickets_count = 0

    #Main menu function to interact with the TicketSystem class
    def main_menu(self):
        while True:
            print("\nWELCOME TO THE TICKETING SYSTEM")
            print("1. OPEN A TICKET")
            print("2. CHECK A TICKET")
            print("3. TICKET LIST")
            print("4. RESPOND TO A TICKET")
            print("5. REOPEN A TICKET")
            print("6. SHOW TICKET INFO")
            print("7. EXIT")
            choice = input("Enter your choice (1-7): ")
            
            #Set up main menu using choice
            if choice == "1":
                self.submit_ticket_menu()
            elif choice == "2":
                self.view_ticket_menu()
            elif choice == "3":
                self.list_tickets_menu()
            elif choice == "4":
                self.respond_to_ticket_menu()
            elif choice == "5":
                self.reopen_ticket_menu()
            elif choice == "6":
                self.show_ticket_info_menu()
            elif choice == "7":
                print("EXITING THE TICKETING SYSTEM.")
                break
            else:
                print("Error. Please select a valid option.")
                
    #New ticket temp
    def submit_ticket_menu(self):
        print("\nOPEN A TICKET")
        name = input("Enter your name: ")
        staff_id = input("Enter your staff ID: ")
        email = input("Enter your email address: ")
        issue_description = input("Describe the issue: ")
        self.submit_ticket(name, staff_id, email, issue_description)

    #to check on an existing ticket for details before responding
    def view_ticket_menu(self):
        print("\nCHECK A TICKET")
        ticket_number = int(input("Enter the ticket number: "))
        print(self.view_ticket(ticket_number))
        
    #list of ticket types
    def list_tickets_menu(self):
        print("\nTICKET LIST")
        print(self.list_tickets())
        
    #responding to tickets, new or reopened
    def respond_to_ticket_menu(self):
        print("\nRESPOND TO A TICKET")
        ticket_number = int(input("Enter the ticket number: "))
        response = input("Enter your response: ")
        self.respond_to_ticket(ticket_number, response)

    #to reopen a resolved ticket due to new issue
    def reopen_ticket_menu(self):
        print("\nREOPEN A TICKET")
        ticket_number = int(input("Enter the ticket number: "))
        self.reopen_ticket(ticket_number)

    #Show status of types of tickets.
    def show_ticket_info_menu(self):
        print("\nSHOW TICKET INFO")
        print(self.show_ticket_info())

    #To submit a New ticket
    def submit_ticket(self, name, staff_id, email, issue_description):
        
        #To store details in the dictionary
        ticket_number = self.ticket_counter
        self.tickets[ticket_number] = {
            'name': name,
            'staff_id': staff_id,
            'email': email,
            'issue_description': issue_description,
            'response': "Not Yet Provided",  # Default response
            'status': 'Open'
        }
        self.ticket_counter += 1
        self.open_tickets_count += 1
        self.total_tickets_count += 1

        #TO generate new password if the issue description contains "Password Change"
        if "Password Change" in issue_description:
            new_password = staff_id[:2] + name[:3]
            print(f'New password generated: {new_password}')
            self.tickets[ticket_number]['response'] = f'New password: {new_password}'
            self.tickets[ticket_number]['status'] = 'Closed'  # Close/Resolve the ticket
            self.open_tickets_count -= 1
            self.resolved_tickets_count += 1

        print(f'Ticket ID {ticket_number} created successfully.')

    #to check on an existing ticket for details before responding
    def view_ticket(self, ticket_number):
        ticket = self.tickets.get(ticket_number)
        if ticket:
            return f'Ticket ID: {ticket_number}\nName: {ticket["name"]}\nStaff ID: {ticket["staff_id"]}\nE-mail: {ticket["email"]}\nIssue Description: {ticket["issue_description"]}\nResponse: {ticket["response"]}\nStatus: {ticket["status"]}'
        else:
            return f'Ticket ID {ticket_number} not found.'
        
    #list of ticket types
    def list_tickets(self):
        if self.total_tickets_count > 0:
            return f"Total Tickets: {self.total_tickets_count}\nOpen Tickets: {self.open_tickets_count}\nResolved Tickets: {self.resolved_tickets_count}"
        else:
            return "No tickets found."
        
    #responding to tickets, new or reopened
    def respond_to_ticket(self, ticket_number, response):
        ticket = self.tickets.get(ticket_number)
        if ticket:
            ticket['response'] = response
            ticket['status'] = 'Closed'
            self.open_tickets_count -= 1
            self.resolved_tickets_count += 1
            print(f'Ticket ID {ticket_number} closed successfully.')
        else:
            print(f'Ticket ID {ticket_number} not found.')
            
    #to reopen a resolved ticket due to new issue
    def reopen_ticket(self, ticket_number):
        ticket = self.tickets.get(ticket_number)
        if ticket:
            ticket['status'] = 'Reopened'
            self.open_tickets_count += 1
            self.resolved_tickets_count -= 1
            print(f'Ticket ID {ticket_number} reopened successfully.')
        else:
            print(f'Ticket ID {ticket_number} not found.')
            
    #Show status of types of tickets.
    def show_ticket_info(self):
        ticket_info = f"Total Tickets: {self.total_tickets_count}\nOpen Tickets: {self.open_tickets_count}"
        if self.resolved_tickets_count:
            ticket_info += f"\nResolved Tickets: {self.resolved_tickets_count}"
        return ticket_info

#main starts here
if __name__ == "__main__":
    ticketsys = TicketSystem()
    ticketsys.main_menu()
