# Model a system where guests can search for available rooms, 
# make a booking, and check out. The hotel has different room types — Standard, Deluxe, and Suite. 
# Upon checkout, a bill is generated based on the number of nights stayed and any 
# additional services availed (like room service, laundurer, spa, etc.)
from datetime import date

class Bill:
    def __init__(self, name, room_number, room_type, service, number_nights):
        self.__name = name
        self.__room_number = room_number
        self.services = []
        self.services.append(service)
        self.room_type = room_type
        self.nights = number_nights

    def avail_service(self, service_name):
        self.services.append(service_name)

    @property
    def name(self):
        return self.__name
    
    # If the customer wants to get their name changed.
    @name.setter
    def name(self, name):
        self.__name = name
        return f"name changed"
    
    # to prevent unknown access
    @property
    def room_number(self):
        return self.__room_number

    
    def print_bill(self):
        # The entire logic of calculating the bill amount with all the charges.
        room_number = self.room_number
        customer_name = self.name
        pass

    
class Hotel:
    def __init__(self, hotel_name, number_rooms, room_types, services, booked_rooms):
        self.hotel_name = hotel_name 
        self.number_rooms = number_rooms 
        self.room_types = room_types
        self.services = services
        self.booked = []
        self.booked.extend(booked_rooms)
        self.bills = []

    def search_rooms(self, room_number):
        if room_number not in self.booked:
            if room_number <= self.number_rooms:
                return True
        else:
            print(f"Room {room_number} is occupied")
            return False
    
    def book_room(self, name, room_number, room_type, service = "", number_nights = 1):
        if self.search_rooms(room_number):
            self.booked.append(room_number)
            bill = Bill(name, room_number, room_type, service, number_nights)
            self.bills.append(bill)

    def avail_service(self, room_number, service):
        if service in self.services:
            for bill in self.bills:
                if bill.room_number == room_number:
                    bill.avail_service(service)
            else:
                raise ValueError("Room not booked")
        else:
            raise ValueError("Service not available")
        
    def checkout(self, room_number):
        if room_number in self.booked:
            self.booked.remove(room_number)

        for bill in self.bills:
            if bill.room_number == room_number:
                bill.print_bill()
            self.bills.remove(bill)
                


            



